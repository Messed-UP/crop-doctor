# Crop Doctor (فصل ڈاکٹر) — Pitch & Presentation Guide

**Event:** Build with Google - CUI Tech Fest FA'26  
**Domain:** Agriculture & Food Security | **SDG:** Supports Goal 2 (Zero Hunger)  

---

## ⏱️ 5-Minute Presentation Script (Comprehensive)

### [0:00 - 0:45] Slide 1: The Real Problem
"Respected judges, mentors, and fellow builders.

In rural Pakistan, many smallholder farmers face crop diseases with limited access to timely agricultural experts. When unfamiliar leaf spots threaten a harvest of wheat, cotton, or tomatoes, an extension officer may not be immediately available to inspect the field. Out of urgency, farmers often turn to local pesticide shops, where they may be sold expensive chemical mixtures that can risk crop health or soil quality. Smallholder farmers need a fast, cautious second opinion in their own language before taking action."

### [0:45 - 1:40] Slide 2: Solution & SDG Alignment
"That is why we built **Crop Doctor (فصل ڈاکٹر)**, an AI-powered assistant designed to support smallholder farmers in Pakistan.

Using Google's Gemini 3.5 Flash via Google AI Studio, Crop Doctor turns a smartphone camera into a cautious agronomy guide.

When a farmer submits a leaf photo, the application provides:
1. **Urdu Guidance:** Clear, natural Urdu rendered right-to-left using native Nastaliq script (`Noto Nastaliq Urdu`), with an English toggle.
2. **Urgency & Confidence Indicators:** Visual badges indicating whether action is needed today, this week, or if monitoring is sufficient. The prompt guides the model to use 'medium' or 'low' confidence on single photos unless symptoms are classic.
3. **The 'Do NOT Do' List:** Advises against common harmful practices, such as spraying during high winds or tank-mixing unverified chemicals.
4. **Generic Active Ingredients Only:** Mentions cultural practices and generic active ingredients (like copper oxychloride or sulfur)—avoiding commercial brand names and unverified dosages.
5. **WhatsApp Summary:** Generates a short summary inside an expander that can be copied and forwarded for community discussion.

This directly **supports SDG 2: Zero Hunger**, with possible secondary contributions to SDGs 12 and 13 through responsible chemical use."

### [1:40 - 2:50] Slide 3: Live Demonstration (3 Realistic Scenarios)
"Let us see how Crop Doctor behaves across three test scenarios:

*(Scenario 1: Diseased Leaf)*  
First, we select a test photo of a potato leaf with visible lesions. When we tap 'Analyze', the model evaluates the symptoms: it identifies the crop as potato and notes the issue as **likely late blight**, flagging urgency as 'Act Today'. It suggests cautious cultural practices, mentions generic copper-based ingredients, warns against overhead watering, and formats a short WhatsApp summary in the expander.

*(Scenario 2: Blurry Photo — 'Ask, Don't Guess')*  
Now, what happens if an image is out-of-focus or taken in poor light? Instead of guessing, Crop Doctor is designed to hold back: it shows *'The photo is too unclear to judge'*, requests a clearer daylight shot, and shows **no diagnosis**. In our tests, this prevents guesswork when an image is inadequate.

*(Scenario 3: Non-Plant Image)*  
Finally, if someone uploads an image that is not a plant—such as shoes—the model responds: *'This does not look like a plant leaf'* and asks for an affected crop leaf. In our tests, this helped avoid hallucinated plant diseases."

### [2:50 - 3:45] Slide 4: System Architecture & Google Technologies
"Crop Doctor was built with a decoupled and resilient architecture:
- **Built with Google Antigravity:** We developed the entire codebase using Google Antigravity as our AI coding assistant for architecture scaffolding, Pydantic modeling, and prompt engineering.
- **Frontend in Streamlit:** Styled with a locked light theme (`.streamlit/config.toml`) to ensure readability outdoors in bright daylight.
- **AI Models & Resilience:** The backend in `src/ai.py` calls our primary model, **`gemini-3.5-flash`**. If temporary upstream errors occur (such as 503 or 429), it retries up to 3 times with backoff waits of 2, 4, and 8 seconds. If retries are exhausted, it automatically attempts a single fallback call to **`gemini-2.5-flash`**.
- **Contract Validation:** Responses are validated against our Pydantic `CropAnalysis` schema using the `google-genai` SDK's structured outputs.
- **Decoupled Code:** `app.py` contains strictly UI presentation logic, keeping AI calls isolated in `src/ai.py`."

### [3:45 - 4:45] Slide 5: Responsible AI, Limitations & Evaluation
"We built Crop Doctor with farmer safety as a central guideline:
- **Guidance, Not Certified Diagnosis:** Every result displays an un-dismissible disclaimer stating that this is guidance, not a lab confirmation, and reminds farmers to consult a local agriculture officer.
- **No Dosages or Commercial Brands:** We avoid numerical chemical dosages because safe application depends on local formulation, sprayer calibration, and crop stage.
- **Prompt-Guided Caution:** The prompt explicitly guides the model to use tentative language ('likely') and to avoid claiming diagnostic certainty.
- **Honest Evaluation:** We do not claim unverified statistical accuracy percentages. In `docs/DISCLOSURE.md`, we recorded our qualitative evaluation by hand on our own test photos.
- **Known Limitations:** A single leaf photo cannot diagnose subterranean root problems or complex multi-pathogen infections, and requires internet connectivity to reach the Gemini API.

Crop Doctor is designed to provide cautious, accessible, and local-language agricultural guidance. Thank you!"

---

## ⚡ 3-Minute Presentation Script (Fast & Punchy)

### [0:00 - 0:35] Problem & Context
"Judges, many smallholder farmers across Pakistan have limited access to agricultural extension experts when crop diseases strike. 

When leaf lesions appear on wheat, cotton, or tomatoes, farmers often have to rely on local pesticide shops, where they may be sold costly chemical mixtures that can risk crop health or soil quality. Existing apps are often in English and full of technical jargon. Farmers need a fast, cautious second opinion in their own language before spraying."

### [0:35 - 1:15] Solution & Features
"We built **Crop Doctor (فصل ڈاکٹر)**, powered by Google's Gemini 3.5 Flash via Google AI Studio and developed using Google Antigravity.

In seconds, a farmer uploads a leaf photo and receives:
1. Actionable advice in native right-to-left **Urdu** (with an English toggle).
2. Clear **Urgency Badges** (`Act Today`, `This Week`, `Monitor`) and calibrated confidence.
3. A vital **'Do NOT Do' list** highlighting mistakes like spraying in strong winds.
4. **Generic active ingredients only**—avoiding commercial brand names and unverified dosages.
5. And our core principle: **'Ask, Don't Guess'**. When a photo is blurry, the app refuses to diagnose and asks for a better photo.
6. A copyable **WhatsApp summary** inside an expander for community discussion.

This **supports SDG 2: Zero Hunger**, with possible secondary contributions to SDGs 12 and 13."

### [1:15 - 2:05] Live Demonstration
"Here is how Crop Doctor performs across three test scenarios:

1. **Diseased Leaf:** On a potato leaf with lesions, it identifies the crop, notes **likely late blight**, flags urgency as 'Act Today', suggests generic cultural practices and active ingredients, warns against overhead watering, and formats a WhatsApp summary.
2. **Blurry Leaf ('Ask, Don't Guess'):** On an out-of-focus leaf, the app states *'The photo is too unclear to judge'*, requests a focused daylight photo, and shows **no diagnosis**.
3. **Non-Plant Photo:** When shown a shoe, it responds: *'This does not look like a plant leaf'*. In our tests, it avoided hallucinating diseases on non-plant images."

### [2:05 - 2:50] Architecture & Responsible AI
"Under the hood:
- **Built with Google Antigravity:** Used for codebase scaffolding, schema modeling, and prompt refinement.
- **Resilient AI Pipeline:** Built on **`gemini-3.5-flash`** with up to 3 automatic retries (2s, 4s, 8s) on transient errors, plus a fallback to **`gemini-2.5-flash`**.
- **Structured Validation:** Enforced through a Pydantic `CropAnalysis` schema using the `google-genai` SDK.
- **Responsible AI:** Guidance only, no commercial brand bias, no numerical dosages, and an honest manual evaluation log in `docs/DISCLOSURE.md` without invented accuracy statistics.

Crop Doctor aims to provide cautious, helpful guidance for farmers who need it most. Thank you!"

---

## 📊 5 Slide Outlines

### Slide 1: The Problem
- **Headline:** Agricultural Challenges in Pakistan's Fields
- **Key Points:**
  - Many smallholder farmers face crop health issues with limited access to agriculture extension experts [ADD SOURCED STAT].
  - Farmers often depend on local pesticide shops, where they may purchase unneeded or expensive brand-name chemical mixtures.
  - Inappropriate chemical spraying can damage soil and reduce farm income.
  - Many existing digital tools are in English, complex, or attempt to guess diseases even on poor-quality photos.
- **Visuals:** Photo of a Pakistani farmer inspecting damaged crops; diagram showing the gap between field symptoms and expert advice.

### Slide 2: Solution & SDG Alignment
- **Headline:** Crop Doctor (فصل ڈاکٹر) — Safe, Localized Guidance
- **Key Points:**
  - Multimodal leaf reasoning powered by Gemini 3.5 Flash via Google AI Studio.
  - Native Urdu interface (RTL Nastaliq) with an instant English toggle.
  - Key output features: Urgency Badge, "Do NOT Do" list, Generic safe remedies, WhatsApp summary expander.
  - Core safety principle: "Ask, Don't Guess" (refuses to diagnose blurry photos).
  - **Supports SDG 2 (Zero Hunger)**, with possible secondary contributions to **SDG 12** and **SDG 13**.
- **Visuals:** Screenshot of the Streamlit Urdu interface showing badges, treatment steps, and "Avoid" box.

### Slide 3: Live Demo
- **Headline:** Practical Behavior in Three Scenarios
- **Key Points:**
  - **Scenario A (Diseased Leaf):** Plausible identification of potato leaf with likely late blight, urgency indicator, generic cultural and active ingredient advice, and WhatsApp summary.
  - **Scenario B (Blurry Leaf):** "Photo is too unclear to judge" -> specific retake guidance, zero diagnosis shown.
  - **Scenario C (Non-Plant):** "This does not look like a plant leaf" -> polite retake prompt, avoiding guesswork.
- **Visuals:** Three-panel graphic showing: Valid Result, Unclear Photo Retake, Non-Plant Retake.

### Slide 4: System Architecture & Resilience
- **Headline:** Decoupled Architecture Built with Google Antigravity
- **Key Points:**
  - **Built with Google Antigravity:** AI coding agent used to scaffold the project, structure Pydantic models, and iterate on prompts.
  - **Frontend:** Streamlit with locked light theme (`.streamlit/config.toml`) for sunlight legibility.
  - **AI Engine & Resilience:** Google Gemini 3.5 Flash (`MODEL_NAME`) with 3 retry backoffs (2s, 4s, 8s) and automatic fallback to Gemini 2.5 Flash (`FALLBACK_MODEL`).
  - **Contract Validation:** Pydantic `CropAnalysis` schema ensuring validated JSON outputs via `google-genai` SDK.
  - **Prompt Guidance:** The prompt guides the model to maintain strict language isolation without mixing Urdu and English.
- **Visuals:** Architecture diagram: Image -> Streamlit UI -> src/ai.py (Retry & Fallback) -> Gemini API -> Pydantic Schema -> UI.

### Slide 5: Responsible AI & Limitations
- **Headline:** Cautious Design & Honest Boundaries
- **Key Points:**
  - **Guidance, Not Diagnosis:** Pinned disclaimer on every result; always emphasizes extension officer verification.
  - **No Commercial Brands or Doses:** Generic active ingredients only; avoids chemical burn and resistance risks.
  - **Prompt-Guided Caution:** Single-photo confidence is guided toward medium or low; identifies supplementary field checks needed.
  - **Honest Evaluation & Limitations:** Evaluated qualitatively on our own test photos in `docs/DISCLOSURE.md`; acknowledges single-leaf foliar scope and internet dependency. No invented accuracy statistics.
- **Visuals:** Snapshot of the manual evaluation table and pinned disclaimer box.

---

## ❓ 6 Likely Judge Questions & Honest Answers

### 1. "How can you be sure the AI won't hallucinate a disease and ruin a farmer's crop?"
**Answer:**  
"We built caution directly into the prompt and schema design. First, we instruct the model to 'Ask, don't guess'—if an image is blurry or symptoms are unclear, it sets `needs_better_photo=True`, and the application suppresses any diagnostic output. Second, the prompt guides the model to use medium or low confidence for single photos and suggest supplementary observations (such as checking the underside of the leaf or roots). Third, we do not provide brand names or exact chemical doses—only generic active ingredients and cultural practices. Finally, every result prominently directs the farmer to confirm with an agriculture extension officer."

### 2. "Why didn't you train a custom computer vision model (like a CNN/ResNet) on a plant disease dataset?"
**Answer:**  
"Traditional CNN classifiers are typically trained on closed-set classes and may struggle with out-of-distribution inputs like non-plant objects, blurry photos, or complex co-occurring symptoms without extensive retraining. Gemini 3.5 Flash provides multimodal reasoning: in our tests, it can evaluate image clarity, assess whether a photo shows a plant leaf, follow structured Pydantic schemas, and explain reasoning in natural Urdu without requiring separate translation pipelines."

### 3. "What is your measured accuracy percentage?"
**Answer:**  
"We do not claim an unverified accuracy percentage like '95% accurate'. Scientifically validating agronomic diagnostic accuracy requires controlled field trials and laboratory testing across multiple seasons and regions. Instead, we performed a qualitative manual check on our own sample images, documented transparently in `docs/DISCLOSURE.md`. In our tests, the model provided plausible guidance on the clear diseased sample, avoided guessing on the blurry photo, and correctly rejected the non-plant image."

### 4. "Why don't you prescribe exact chemical doses (e.g. 50 grams per 20 liters of water)?"
**Answer:**  
"Prescribing specific chemical dosages from a single photo is risky. Safe application rates depend on the exact chemical formulation available locally, crop growth stage, sprayer calibration, ambient temperature, and soil conditions. Giving fixed dosage numbers could lead to chemical burn or ineffective treatment. We intentionally limit recommendations to generic active ingredients, instruct farmers to read the container label, and advise verifying rates with a local extension officer."

### 5. "How will smallholder farmers with low literacy or limited connectivity use this?"
**Answer:**  
"We prioritized straightforward usability:
1. The app requires no text entry—farmers simply tap to upload or select a photo and tap 'Analyze'.
2. Guidance is presented in natural Urdu script with visual color-coded badges for urgency and confidence.
3. The short WhatsApp summary in the expander can be shared with community farming groups, younger family members, or local extension workers for voice explanation.
4. For network resilience, our backend includes automatic retries and a fallback model."

### 6. "Why did you build this as a Streamlit web app rather than a native mobile app or WhatsApp bot?"
**Answer:**  
"For the hackathon, Streamlit enabled us to rapidly build and demonstrate a responsive web application that works on both mobile and desktop browsers. Because our AI orchestration and schema validation in `src/ai.py` and `src/schema.py` are strictly separated from the presentation layer, the same backend can be connected to messaging channels like WhatsApp or mobile APIs as a future extension."
