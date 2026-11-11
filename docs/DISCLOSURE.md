# Disclosure (fill in during the event)

## AI tools used to write code
- Google Antigravity (AI coding agent) - used for: architecture scaffolding, Pydantic schema, safe prompt engineering, Gemini API integration, and Streamlit UI with Urdu RTL support.
- Other assistant(s) - used for:
- Design/slides tools (only if used, e.g. Canva) - used for:

## AI models and APIs in the product
- Gemini API (model: gemini-3.5-flash) via Google AI Studio - leaf analysis and Urdu response

## Libraries
- Python 3.13, Streamlit, Pillow, google-genai, pydantic

## Images / datasets
| File | Source (URL) | License / note |
|---|---|---|
| samples/blurry_1.jpg | own photo | taken by team |
| samples/disease_1.jpg | own photo | taken by team |
| samples/healthy_1.jpg | own photo | taken by team |
| samples/non_plant_1.jpg | own photo | taken by team |
| samples/your_photo_1.webp | own photo | taken by team |

## Mini evaluation (by hand, small public sample)
## Mini evaluation (by hand, small sample of our own photos)

| Image | What the photo is (our knowledge) | App output | Plausible? | Notes |
|---|---|---|---|---|
| samples/disease_1.jpg | Potato leaf with visible lesions (disease name unverified) | Potato, likely late blight, act today, avoid list shown | Plausible, disease name unverified | Single-photo diagnosis is uncertain; confidence capped after fix |
| samples/healthy_1.jpg | Healthy leaf | Grapevine, healthy, monitor, no chemical treatment | Yes | No disease invented |
| samples/blurry_1.jpg | Blurry leaf photo | No diagnosis, asked for a clearer photo | Yes | Message wording fixed to "too unclear" |
| samples/non_plant_1.jpg | Shoes | Rejected, asked for a leaf photo, no results | Yes | Plants in the background did not fool it |
| samples/your_photo_1.webp | (fill in) | (not tested yet) | (fill in) | Test it or delete this row |

Summary: plausible answers on 4 of 4 tested images. Small sample of our own photos, not a validation study. No accuracy percentage is claimed.

## Limitations
- Not a diagnosis. Accuracy not formally validated.
- Results depend on photo quality and may be wrong.
