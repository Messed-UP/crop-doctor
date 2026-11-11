"""
src/schema.py - Pydantic model for Crop Doctor structured response.
Defines the exact shape of data returned by the Gemini API.
"""

from typing import Literal, List
from pydantic import BaseModel, Field


class CropAnalysis(BaseModel):
    """Structured crop health analysis for leaf photo evaluation."""

    # Plant photo verification
    is_plant_photo: bool = Field(
        description="True if the photo contains a plant leaf or crop part, False otherwise."
    )

    # Crop and issue identification
    crop: str = Field(
        description="Name of the crop identified in the photo (e.g. Wheat, Cotton, Rice, Tomato)."
    )
    likely_problem: str = Field(
        description="Likely disease, pest, or nutrient deficiency (always framed as 'likely', not a diagnosis)."
    )

    # Confidence and urgency indicators
    confidence: Literal["low", "medium", "high"] = Field(
        description="Confidence level of the analysis: 'low', 'medium', or 'high'."
    )
    urgency: Literal["today", "this_week", "monitor"] = Field(
        description="How quickly the farmer needs to act: 'today', 'this_week', or 'monitor'."
    )

    # Photo quality / retake guidance ('Ask, don't guess')
    needs_better_photo: bool = Field(
        default=False,
        description="True if the photo is blurry, too dark, or unclear, requiring a retake."
    )
    better_photo_request: str = Field(
        default="",
        description="Specific polite instruction for retaking the photo (in Urdu and English), empty if not needed."
    )

    # Actionable advice
    treatment_steps: List[str] = Field(
        default_factory=list,
        description="Actionable management steps (generic practices or active ingredients only, no brand names)."
    )
    avoid_list: List[str] = Field(
        default_factory=list,
        description="Harmful or ineffective actions the farmer should avoid."
    )
    prevention_tips: List[str] = Field(
        default_factory=list,
        description="Preventative tips for future crop cycles to stop recurrence."
    )

    # Escalation and sharing
    when_to_see_expert: str = Field(
        default="",
        description="Clear conditions when the farmer must consult an agriculture extension officer."
    )
    whatsapp_summary: str = Field(
        default="",
        description="Short, clean summary in Urdu suitable for sharing via WhatsApp."
    )
