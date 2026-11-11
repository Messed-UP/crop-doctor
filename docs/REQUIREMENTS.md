# Crop Doctor - Requirements (v2)

## 1. Pitch
A farmer uploads a leaf photo and gets a safe, cheap, Urdu action plan in seconds: likely problem, how urgent it is, what to do, what NOT to do. When the AI is unsure, it asks for a better photo instead of guessing.

## 2. Hackathon fit
- Domain: Agriculture & Food Security
- SDG: SDG 2 (Zero Hunger); also supports SDG 12 and 13
- User: smallholder farmers in Pakistan (wheat, cotton, rice, sugarcane, maize, tomato and similar)

## 3. Core (build first, includes Tier 1)
- [ ] Upload a leaf photo (jpg / png)
- [ ] Send photo + prompt to the Gemini API
- [ ] Gemini returns structured JSON (see schema below)
- [ ] Result in Urdu (English toggle) in a clean card, right-to-left
- [ ] Confidence badge (low / medium / high)
- [ ] Urgency badge (today / this week / monitor)
- [ ] "Do not do" list
- [ ] "Ask, don't guess": low confidence or blurry photo -> request a specific better photo, show no diagnosis
- [ ] Not-a-plant photo -> polite retake message
- [ ] Visible disclaimer on every result: guidance only, not a confirmed diagnosis
- [ ] Friendly error message if the API fails
- [ ] 10-12 public sample images in `samples/` (sources in DISCLOSURE.md)
- [ ] Runs with `py -m streamlit run app.py`

### Schema (CropAnalysis)
is_plant_photo (bool), crop (str), likely_problem (str), confidence (low|medium|high),
urgency (today|this_week|monitor), needs_better_photo (bool), better_photo_request (str),
treatment_steps (list[str]), avoid_list (list[str]), prevention_tips (list[str]),
when_to_see_expert (str), whatsapp_summary (str)

## 4. Tier 2 (only after core passes all tests, one at a time)
1. [ ] WhatsApp "Copy summary" button
2. [ ] Mini evaluation table in DISCLOSURE.md (done by hand on the sample images)
3. [ ] Read-aloud of the Urdu result (src/tts.py)

## 5. Tier 3 (only if well ahead; ask first)
- [ ] Google Search grounding with sources. Check in AI Studio that it works together with JSON output first.

Hard stop for new features at the 3:20 mark.

## 6. Non-functional
- Result in about 15 seconds on normal internet
- Readable on laptop and phone browsers
- Urdu displays correctly (right-to-left, Noto Nastaliq Urdu)
- Code simple enough to explain every file

## 7. Technology (all disclosed)
- Gemini API via Google AI Studio (main Google technology)
- Python 3.13, Streamlit, Pillow, google-genai, pydantic
- Antigravity / other AI coding assistants; Canva or Figma only if actually used

## 8. Responsible AI
- "Likely" and "guidance" wording only; never a diagnosis
- Generic practices or active ingredients only, no brand names; always "confirm with an agriculture officer"
- Confidence shown; low confidence asks for a better photo
- Public sample images only; no private data
- No accuracy claims. Evaluation stated honestly: small public sample, not a validation study

## 9. Rule compliance
- Core development happens during the competition period
- No previously completed project reused
- External images/datasets disclosed
- README and slides list all AI tools used

## 10. Done means
A stranger uploads a sample leaf, gets a sensible Urdu action plan with urgency, avoid list and disclaimer; a blurry photo gets a request for a better one; the repo has README, disclosure list and a clean commit history.
