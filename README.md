# Crop Doctor

AI-powered crop leaf analysis for Pakistani farmers, with answers in Urdu.

**Hackathon:** Build with Google - CUI Tech Fest FA'26
**Domain:** Agriculture & Food Security | **SDG:** 2 - Zero Hunger

## Problem
(2-3 sentences: who the farmer is, what goes wrong, why expert help is hard to reach.)

## Solution
(Upload a leaf photo, get likely problem, confidence, urgency, treatment steps and a do-not-do list in Urdu. If unsure, the app asks for a better photo instead of guessing.)

## How it works
Photo -> Streamlit app -> Gemini API (image + prompt) -> structured JSON -> Urdu result card

## Google technologies
- Gemini API via Google AI Studio
- (add any others actually used)

## Tools used (disclosure)
See `docs/DISCLOSURE.md`. AI coding assistants: Google Antigravity (list others).

## Responsible AI
Guidance only, not a diagnosis. Confidence shown. Public sample images only. No accuracy claims.

## Run it
```
py -m pip install -r requirements.txt
setx GEMINI_API_KEY "your-key"     (then reopen the terminal)
py -m streamlit run app.py
```

## Team
(names)
