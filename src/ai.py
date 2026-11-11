"""
src/ai.py - Gemini API integration for Crop Doctor leaf photo analysis.
Handles client setup, image + prompt dispatch, structured output parsing,
and resilient retry logic with fallback model support.
"""

import os
import time
from typing import List
from google import genai
from google.genai import types

from src.schema import CropAnalysis
from src.prompts import build_prompt

# Primary and fallback model constants
MODEL_NAME = "gemini-3.5-flash"
FALLBACK_MODEL = "gemini-2.5-flash"

# Retry delays in seconds for transient errors
RETRY_DELAYS = [2, 4, 8]


def _is_retryable(error: Exception) -> bool:
    """
    Determine whether an error is transient and safe to retry.
    Transient errors include 503 UNAVAILABLE, 429 rate limits, and network timeouts.
    Non-retryable errors include invalid API keys, bad requests, and authentication failures.
    """
    # 1. Inspect HTTP status code if present
    code = getattr(error, "code", None)
    if code in [429, 500, 502, 503, 504]:
        return True
    if code in [400, 401, 403, 404]:
        return False

    # 2. Standard Python network timeout and connection exceptions
    if isinstance(error, (TimeoutError, ConnectionError)):
        return True

    # 3. String-based matching on error description
    err_str = str(error).lower()

    # Immediate non-retryable conditions
    non_retryable_markers = [
        "invalid key",
        "api_key_invalid",
        "unauthenticated",
        "permission_denied",
        "invalid_argument",
        "bad request",
        "400",
        "401",
        "403",
        "not_found",
        "404",
    ]
    if any(marker in err_str for marker in non_retryable_markers):
        return False

    # Transient / retryable conditions
    retryable_markers = [
        "503",
        "429",
        "unavailable",
        "resource_exhausted",
        "timeout",
        "timed out",
        "overloaded",
        "rate limit",
        "quota",
        "connection reset",
        "502",
        "504",
    ]
    if any(marker in err_str for marker in retryable_markers):
        return True

    return False


def _generate(client: genai.Client, model: str, contents: list) -> CropAnalysis:
    """Execute a single generate_content call against a specific model."""
    response = client.models.generate_content(
        model=model,
        contents=contents,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=CropAnalysis,
        ),
    )

    if response.parsed and isinstance(response.parsed, CropAnalysis):
        return response.parsed

    if response.text:
        return CropAnalysis.model_validate_json(response.text)

    raise ValueError("Received an empty response from the Gemini API.")


def analyze(image_bytes: bytes, mime_type: str = "image/jpeg", language: str = "Urdu") -> CropAnalysis:
    """
    Analyze a crop leaf photo using the Gemini API and return structured results.
    Retries up to 3 times on transient errors, with an automatic single fallback.
    
    Args:
        image_bytes: Raw bytes of the uploaded leaf photo.
        mime_type: MIME type of the image (e.g. 'image/jpeg', 'image/png').
        language: Output language for text fields ('Urdu' or 'English').
        
    Returns:
        Validated CropAnalysis Pydantic model instance.
        
    Raises:
        RuntimeError: Friendly error message if analysis fails or API key is missing.
    """
    # 1. Verify GEMINI_API_KEY is present
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY environment variable is not set. "
            "Please set your Gemini API key in the environment before running the app."
        )

    # 2. Build system/instruction prompt and contents
    prompt = build_prompt(language=language)
    image_part = types.Part.from_bytes(
        data=image_bytes,
        mime_type=mime_type,
    )
    contents = [image_part, prompt]

    # Initialize Gemini client
    client = genai.Client()
    last_error: Exception = None

    # 3. Try primary model: initial attempt + up to 3 retries (waits: 2, 4, 8 seconds)
    for delay in [0] + RETRY_DELAYS:
        if delay > 0:
            time.sleep(delay)
        try:
            return _generate(client, MODEL_NAME, contents)
        except Exception as e:
            last_error = e
            # Stop immediately on non-retryable errors (invalid key, bad request)
            if not _is_retryable(e):
                break

    # 4. If primary model fails on transient errors, attempt FALLBACK_MODEL once
    if last_error is not None and _is_retryable(last_error):
        try:
            return _generate(client, FALLBACK_MODEL, contents)
        except Exception as e:
            last_error = e

    # 5. All attempts failed: format friendly error, guaranteeing no API key is exposed
    err_detail = str(last_error)
    if api_key and api_key in err_detail:
        err_detail = err_detail.replace(api_key, "[REDACTED]")

    raise RuntimeError(
        f"Leaf analysis could not be completed at this moment. Details: {err_detail}"
    ) from last_error
