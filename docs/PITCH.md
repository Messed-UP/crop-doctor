# Crop Doctor (فصل ڈاکٹر) — Pitch & Presentation Guide

**Event:** Build with Google - CUI Tech Fest FA'26  
**Domain:** Agriculture & Food Security | **SDG:** Goal 2 (Zero Hunger)  

---

## ⏱️ 5-Minute Presentation Script (Comprehensive)

### [0:00 - 1:00] Slide 1: The Real Problem
"Respected judges, mentors, and fellow builders.

Imagine you are Muhammad Akram, a smallholder farmer in rural Punjab cultivating four acres of wheat and tomatoes. One morning, you notice dark brown, water-soaked lesions spreading across your tomato leaves. In 48 hours, this disease could destroy your season's harvest—and with it, your family's annual income.

What can Akram do?
Government agriculture extension officers are dedicated, but there is only one officer for every several thousand farms. They simply cannot visit every field in time. 

So Akram plucks a leaf, visits the nearest rural market, and shows it to a local pesticide dealer. What happens? That dealer is a salesman on commission. He hands Akram an expensive, multi-chemical cocktail of branded pesticides with high profit margins. Akram pays money he doesn't have, sprays the crop, and risks chemical burn, pesticide resistance, and toxic runoff.

Existing smartphone apps don't solve this: they are in English, filled with academic jargon, and worst of all—when you show them a blurry leaf, they guess a random disease with fake 99% confidence. 

Smallholder farmers don't need another English dashboard. They need an honest, safe second opinion in their own language."

### [1:00 - 1:55] Slide 2: Solution & SDG Alignment
"That is why we built **Crop Doctor (فصل ڈاکٹر)**.

Crop Doctor turns any basic smartphone into a frontline, conservative agronomy guide powered by Google's Gemini 3.5 Flash via Google AI Studio.

When Akram snaps a photo of a leaf, he receives an immediate action plan:
1. **Native Urdu First:** Written in conversational, localized Urdu using native Nastaliq script (`Noto Nastaliq Urdu`), with an instant English toggle.
2. **Urgency & Confidence Badges:** Clearly tells him whether action is needed today, this week, or if he should simply monitor. Confidence is capped conservatively because a single photo can never give 100% certainty.
3. **The 'Do NOT Do' List:** Alerts him against catastrophic mistakes, like spraying during high winds, tank-mixing incompatible chemicals, or harvesting right after spraying.
4. **Generic Active Ingredients Only:** We recommend cultural practices and generic active ingredients like copper oxychloride or sulfur—never expensive commercial brands.
5. **The WhatsApp Summary:** Formats a 3-line summary ready to share with his village farming group or local extension worker.

This directly champions **UN Sustainable Development Goal 2: Zero Hunger**, while reducing chemical runoff under SDGs 12 and 13."

### [1:55 - 3:15] Slide 3: Live Demonstration (3 Realistic Scenarios)
"Let us see Crop Doctor in action across three realistic field scenarios:

*(Scenario 1: Diseased Leaf)*  
First, we select a real photo of a potato leaf with visible lesions. Akram taps 'Analyze'. Within seconds, Gemini 3.5 Flash returns a structured result: Crop identified as Potato; Likely issue identified as Late Blight; Urgency flagged as 'Act Today'. Notice the treatment steps: remove infected lower leaves, avoid overhead watering, and consider generic copper-based sprays. Most importantly, look at the Avoid list: *Do not spray in strong winds, do not harvest immediately*. And here is the clean WhatsApp summary ready to forward.

*(Scenario 2: Blurry Photo — 'Ask, Don't Guess')*  
Now, what happens when a farmer takes a shaky, out-of-focus photo in the field? Traditional AI apps guess a disease and prescribe toxic chemicals. Watch Crop Doctor: when we upload a blurry leaf, the app states clearly: *'The photo is too unclear to judge'*. It gives specific advice—hold the camera steady, take it in daylight, show the underside of the leaf—and it shows **zero diagnosis**. We refuse to guess when a farmer's livelihood is at stake.

*(Scenario 3: Non-Plant Rejection)*  
Finally, what if someone accidentally snaps a shoe or farming tool? The app rejects it immediately: *'This does not look like a plant leaf'*, asking for an affected crop leaf. No hallucinations. Pure safety."

### [3:15 - 4:05] Slide 4: System Architecture & Google Technologies
"Behind this interface is an enterprise-grade, resilient architecture:
- **Streamlit Frontend:** Clean, modular, and locked to a custom light theme (`.streamlit/config.toml`) so farmers can read it clearly in harsh outdoor sunlight.
- **Multimodal AI with Gemini 3.5 Flash:** We leverage Google AI Studio to inspect the image, reason over visual symptoms, and translate advice into natural Urdu.
- **Resilient Retry & Fallback Engine:** To handle unpredictable rural connectivity and temporary upstream errors (503s or 429s), `src/ai.py` automatically retries the primary model up to 3 times with exponential backoff (2s, 4s, 8s). If the primary model remains unavailable, it automatically switches to our fallback model, **Gemini 2.5 Flash**.
- **Contract Enforcement with Pydantic:** Using the `google-genai` SDK's structured output schema, every response strictly adheres to our `CropAnalysis` Pydantic model.
- **Zero AI in the UI:** `app.py` contains strictly UI presentation logic; AI orchestration is completely decoupled in `src/ai.py`."

### [4:05 - 5:00] Slide 5: Responsible AI, Limitations & Impact
"We built Crop Doctor with farmer safety as our non-negotiable priority:
- **Guidance, Not Certified Diagnosis:** Every screen features an un-dismissible disclaimer reminding farmers that this is early decision support, not a laboratory culture.
- **No Dosages or Commercial Bias:** We never output numerical doses because safe application rates depend on sprayer calibration, crop growth stage, and local weather. We always direct farmers to the product label and their local extension officer.
- **Honest Evaluation:** We do not invent marketing statistics like '98% accurate'. We evaluated Crop Doctor by hand on our own test photos, documenting every result in `docs/DISCLOSURE.md`.
- **Acknowledged Limitations:** We openly recognize that single leaf photos cannot detect soil root rot, vascular wilt, or complex multi-pathogen infections.

Crop Doctor empowers Pakistani smallholders with honest, safe, and immediate agricultural guidance—protecting crops, soil, and farmers' livelihoods. Thank you!"

---

## ⚡ 3-Minute Presentation Script (Fast & Punchy)

### [0:00 - 0:40] Problem & Context
"Judges, over 80% of Pakistani agriculture is farmed by smallholders. When foliar diseases strike wheat, cotton, or tomatoes, government extension officers are too overwhelmed to visit in time.

Farmers are forced to consult local pesticide dealers, who often recommend expensive, branded chemical cocktails that burn crops and trap families in debt. Existing apps don't help: they are in English, full of jargon, and guess wildly on blurry photos. Smallholder farmers need a safe second opinion in their own language."

### [0:40 - 1:20] Solution & Features
"We created **Crop Doctor (فصل ڈاکٹر)**, powered by Google's Gemini 3.5 Flash via Google AI Studio.

In seconds, a farmer snaps a leaf photo and receives:
1. Actionable advice in native right-to-left **Urdu** (or English with one tap).
2. Clear **Urgency & Confidence Badges** (`Act Today`, `This Week`, `Monitor`).
3. A vital **'Do NOT Do' list** preventing dangerous mistakes like spraying in high winds or mixing chemicals.
4. **Generic active ingredients only**—zero commercial brand names and zero unmeasured doses.
5. And our core principle: **'Ask, Don't Guess'**. When a photo is blurry or unclear, Crop Doctor refuses to diagnose and asks for a specific better photo.

This directly advances **SDG 2: Zero Hunger** while safeguarding soil under SDGs 12 and 13."

### [1:20 - 2:15] Live Demonstration
"Here is how Crop Doctor performs in live testing:

1. **Diseased Leaf:** On a potato leaf with blight lesions, it identifies the crop, flags urgency as 'Act Today', recommends generic copper fungicide and pruning, warns against overhead watering, and formats a 3-line WhatsApp summary.
2. **Blurry Leaf ('Ask, Don't Guess'):** On an out-of-focus leaf, traditional apps guess a disease. Crop Doctor clearly states *'The photo is too unclear to judge'*, requests a focused daylight shot, and shows **zero diagnosis**.
3. **Non-Plant Photo:** When shown a shoe, it rejects it immediately: *'This does not look like a plant leaf'*. No hallucinations."

### [2:15 - 3:00] Architecture & Responsible AI
"Under the hood:
- **Decoupled Architecture:** Streamlit frontend with a locked light theme for daylight reading, orchestrated with the `google-genai` SDK and validated by Pydantic.
- **Enterprise Resilience:** Up to 3 retries with exponential backoff (2s, 4s, 8s) on transient errors, with an automatic fallback to **Gemini 2.5 Flash**.
- **Responsible AI:** Guidance only, no commercial brand bias, no numerical dosages, conservative confidence capping, and an honest manual evaluation log in `docs/DISCLOSURE.md` with zero invented accuracy statistics.

Crop Doctor puts safe, honest agricultural expertise directly into the hands of Pakistani farmers. Thank you!"

---

## 📊 5 Slide Outlines

### Slide 1: The Problem
- **Headline:** The Crisis in Pakistan’s Fields
- **Key Points:**
  - 80%+ of cultivated land farmed by smallholders (wheat, cotton, rice, sugarcane, maize, tomato).
  - Severe shortage of agricultural extension officers in remote rural areas.
  - Farmers depend on local pesticide dealers who push costly, unnecessary brand-name chemical mixtures.
  - Existing digital solutions are in English, complex, and guess wildly on poor-quality photos.
- **Visuals:** Photo of a Pakistani farmer inspecting damaged crops; graphic illustrating the pesticide dealer markup and debt cycle.

### Slide 2: Solution & SDG Alignment
- **Headline:** Crop Doctor (فصل ڈاکٹر) — Safe, Localized Guidance
- **Key Points:**
  - Multimodal leaf reasoning powered by Gemini 3.5 Flash via Google AI Studio.
  - Native Urdu interface (RTL Nastaliq) with instant English toggle.
  - Key output features: Urgency Badge, "Do NOT Do" list, Generic safe remedies, WhatsApp summary.
  - Core safety principle: "Ask, Don't Guess" (refuses to diagnose blurry photos).
  - Aligned with **SDG 2 (Zero Hunger)**, **SDG 12 (Responsible Consumption)**, **SDG 13 (Climate Action)**.
- **Visuals:** High-resolution screenshot of the Streamlit Urdu interface showing badges, treatment steps, and "Avoid" box.

### Slide 3: Live Demo
- **Headline:** Safe in Every Scenario
- **Key Points:**
  - **Scenario A (Diseased Leaf):** Plausible identification, urgency indicator, generic active ingredients, and WhatsApp share card.
  - **Scenario B (Blurry Leaf):** "Photo is too unclear to judge" -> specific retake guidance, zero diagnosis shown.
  - **Scenario C (Non-Plant):** "This does not look like a plant leaf" -> polite retake prompt, zero hallucinations.
- **Visuals:** Three-panel comparative graphic showing the three distinct application states.

### Slide 4: System Architecture & Resilience
- **Headline:** Robust, Decoupled Architecture
- **Key Points:**
  - **Frontend:** Streamlit with locked light theme (`.streamlit/config.toml`) for sunlight legibility.
  - **AI Engine:** Google Gemini 3.5 Flash (`google-genai` Python SDK).
  - **Resilience:** Automatic 3-stage retry backoff (2s, 4s, 8s) + fallback to Gemini 2.5 Flash on 503/429 errors.
  - **Contract Enforcement:** Pydantic `CropAnalysis` schema ensuring 100% structured JSON outputs.
  - **Strict Language Isolation:** Guaranteed pure Urdu or pure English per selection without mixing.
- **Visuals:** Architecture diagram showing: Image -> Streamlit UI -> src/ai.py (Retry & Fallback) -> Gemini API -> Pydantic Schema -> UI.

### Slide 5: Responsible AI & Limitations
- **Headline:** Built for Farmer Safety, Not Hype
- **Key Points:**
  - **Guidance, Not Diagnosis:** Pinned disclaimer on every result; always emphasizes extension officer verification.
  - **No Commercial Brands or Doses:** Generic active ingredients only; avoids chemical burns and pesticide resistance.
  - **Conservative Confidence:** Single-photo confidence capped; identifies supplementary field checks needed.
  - **Honest Evaluation & Limitations:** Evaluated manually on real sample photos in `docs/DISCLOSURE.md`; acknowledges single-leaf foliar scope and internet dependency. Zero invented accuracy statistics.
- **Visuals:** Snapshot of the manual evaluation table and pinned disclaimer box.

---

## ❓ 6 Likely Judge Questions & Honest Answers

### 1. "How can you be sure the AI won't hallucinate a disease and ruin a farmer's crop?"
**Answer:**  
"We built safety into the core prompt and schema rather than treating it as an afterthought. First, we enforce 'Ask, don't guess'—if an image is blurry or symptoms are ambiguous, Gemini returns `needs_better_photo=True` and the app refuses to display any diagnosis. Second, confidence on single photos is conservatively capped at medium or low, and the model lists what extra field observations are required. Third, we never output specific chemical dosages or brand names—only generic sanitation and standard active ingredients. Finally, every result features an un-dismissible disclaimer advising the farmer to confirm with an agriculture officer."

### 2. "Why didn't you train a custom computer vision model (like a CNN/ResNet) on a plant disease dataset?"
**Answer:**  
"Traditional CNN classifiers suffer from a major flaw in production: they are forced to pick one of $N$ predetermined disease classes. If a farmer uploads an out-of-focus leaf, a healthy leaf with dirt, or an unindexed crop, a standard CNN will still output a high-confidence false diagnosis. Gemini 3.5 Flash provides open-world multimodal understanding: it recognizes whether the subject is a plant leaf, reasons about image blurriness, understands multiple co-occurring symptoms, outputs structured JSON, and generates localized explanations in Urdu without training separate translation layers."

### 3. "What is your measured accuracy percentage?"
**Answer:**  
"We deliberately do not claim an unverified accuracy percentage like '95% accurate'. True diagnostic accuracy in agronomy requires laboratory culturing and controlled field trials across diverse agro-ecological zones, which cannot be measured during a hackathon. Instead, we evaluated our application by hand on a transparent set of real test photos documented in `docs/DISCLOSURE.md`. In our evaluation, the app produced plausible recommendations on all tested samples, properly refused to diagnose a blurry photo, and correctly rejected non-plant photos without hallucinating."

### 4. "Why don't you prescribe exact chemical doses (e.g. 50 grams per 20 liters of water)?"
**Answer:**  
"Prescribing exact chemical doses from a single photo is dangerous and irresponsible. The safe dosage of any agricultural chemical depends heavily on the crop's precise growth stage, formulation concentration from local suppliers, sprayer calibration, soil moisture, and ambient temperature. Giving fixed numbers risks chemical burn or pesticide resistance. We intentionally limit advice to generic active ingredients, instruct the farmer to read the product label, and emphasize confirming application rates with a local extension officer."

### 5. "How will smallholder farmers with low literacy or limited connectivity use this?"
**Answer:**  
"We focused heavily on accessibility:
1. The app requires zero text input—farmers just tap to upload or snap a photo and tap 'Analyze'.
2. The interface uses natural, spoken Urdu rendered in native Nastaliq script with visual color-coded badges for urgency and confidence.
3. For farmers who cannot read, the 3-line WhatsApp summary can be forwarded directly into village WhatsApp groups or sent to younger family members and extension workers for quick voice explanation.
4. For network resilience, our backend includes automatic exponential retries and fallback models."

### 6. "Why did you build this as a Streamlit web app rather than a native mobile app or WhatsApp bot?"
**Answer:**  
"For the hackathon, a Streamlit web app was the fastest way to deliver a zero-install, responsive experience that works on any smartphone browser or laptop. However, because our architecture is strictly decoupled—all Gemini integration and Pydantic validation live in `src/ai.py` and `src/schema.py` without UI coupling—this exact backend can be connected to a Twilio or Meta WhatsApp Business API webhook in less than a day."
