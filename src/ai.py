"""
src/ai.py - Gemini API integration for Crop Doctor leaf photo analysis.
Handles client setup, image + prompt dispatch, and structured output parsing.
"""

import os
from typing import Optional
from google import genai
from google.genai import types

from src.schema import CropAnalysis
from src.prompts import build_prompt

# Model name is defined in ONE place as required by project rules
MODEL_NAME = "gemini-3.5-flash"


def analyze(image_bytes: bytes, mime_type: str = "image/jpeg", language: str = "Urdu") -> CropAnalysis:
    """
    Analyze a crop leaf photo using the Gemini API and return structured results.
    
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

    # 2. Build system/instruction prompt
    prompt = build_prompt(language=language)

    # 3. Call Gemini API inside try/except block
    try:
        # Client automatically reads GEMINI_API_KEY from environment
        client = genai.Client()

        # Prepare image part from raw bytes
        image_part = types.Part.from_bytes(
            data=image_bytes,
            mime_type=mime_type,
        )

        # Dispatch request with structured response schema
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=[image_part, prompt],
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=CropAnalysis,
            ),
        )

        # 4. Extract and validate structured response
        if response.parsed and isinstance(response.parsed, CropAnalysis):
            return response.parsed
        
        if response.text:
            return CropAnalysis.model_validate_json(response.text)

        raise ValueError("Received an empty response from the Gemini API.")

    except Exception as e:
        # Wrap all potential network, authentication, or parsing errors in a friendly message
        raise RuntimeError(
            f"Leaf analysis could not be completed at this moment. Details: {e}"
        ) from e
