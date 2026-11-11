# Crop Doctor (فصل ڈاکٹر) — Pitch & Presentation Guide

**Event:** Build with Google - CUI Tech Fest FA'26  
**Presentation Duration:** 3 Minutes  
**Domain:** Agriculture & Food Security | **SDG:** Goal 2 (Zero Hunger)  

---

## ⏱️ 3-Minute Presentation Script

### [0:00 - 0:35] Slide 1: The Problem
"Good morning, judges and fellow innovators.

In Pakistan, over 80% of our farmlands are cultivated by smallholder farmers. When pests or leaf diseases attack their wheat, cotton, or tomatoes, every hour counts. But public agriculture extension officers are stretched thin across vast districts, and it can take days or weeks for an expert to visit a field.

Left stranded, farmers take diseased leaves to local pesticide dealers. What happens next? Dealers often push expensive, multi-brand chemical cocktails that the farmer doesn't need. The results are devastating: crop burns, unnecessary debt, chemical runoff, and lost harvests. Furthermore, existing digital tools are in English and full of technical jargon that our farmers cannot use.

Smallholder farmers don't need another complex dashboard—they need a safe, fast second opinion in their own language."

### [0:35 - 1:10] Slide 2: Solution & SDG 2
"That is why we built **Crop Doctor (فصل ڈاکٹر)**.

Crop Doctor turns a farmer's smartphone into a safe, conservative frontline agronomic guide powered by Google's Gemini 3.5 Flash. 

A farmer snaps a photo of an affected leaf, and within seconds receives:
1. An instant assessment in clear, right-to-left **Urdu** using native Nastaliq script (or English with one tap).
2. A clear **Urgency Badge**—telling them whether action is needed today, this week, or if they should simply monitor.
3. A vital **'Do NOT Do' list**—preventing catastrophic mistakes like spraying during high winds or mixing incompatible chemicals.
4. And most importantly, our core philosophy: **'Ask, Don't Guess'**. When a photo is blurry, dark, or not a plant, Crop Doctor refuses to hallucinate a disease and asks for a specific better photo.

This directly champions **UN Sustainable Development Goal 2: Zero Hunger**, while protecting soil and ecosystems under SDGs 12 and 13."

### [1:10 - 2:10] Slide 3: Live Demonstration
"Let me demonstrate how Crop Doctor behaves in real life:

*(Demo Action 1 - Diseased Leaf)*  
First, we select a real photo of a potato leaf with visible lesions. When we tap 'Analyze', Gemini 3.5 Flash inspects the image and returns a strictly typed JSON structure. Notice the output: it identifies the crop as potato, notes the likely issue as late blight, flags urgency as 'Act Today', lists safe cultural practices and generic active ingredients, and warns against overhead watering. It also prepares a concise 3-line WhatsApp summary.

*(Demo Action 2 - Blurry Photo)*  
Now, what happens if a farmer takes a shaky, out-of-focus photo? Most existing AI apps guess a random disease. Crop Doctor does not. When we submit a blurry photo, the app states clearly: *'The photo is too unclear to judge'*, requests a focused daylight shot, and shows **no diagnostic results**.

*(Demo Action 3 - Non-Plant Photo)*  
Finally, if someone accidentally uploads a photo of shoes or machinery, it immediately responds: *'This does not look like a plant leaf'* and asks for an affected crop leaf. No hallucinations. Pure safety."

### [2:10 - 2:35] Slide 4: Architecture & Google Technologies
"Under the hood, Crop Doctor is built with clean engineering discipline:
- **Streamlit** powers the responsive frontend, locked to a light theme so farmers can read it clearly in direct sunlight.
- **Google Gemini 3.5 Flash** acts as our multimodal reasoning engine via Google AI Studio.
- Using Google's modern `google-genai` SDK, we enforce strict structured outputs via a **Pydantic** schema (`CropAnalysis`). This ensures that every API response conforms to our exact data contract.
- The UI contains zero AI code; all logic is cleanly decoupled into modular Python services."

### [2:35 - 3:00] Slide 5: Responsible AI & Honest Evaluation
"We designed Crop Doctor under strict Responsible AI principles:
- **Guidance, Never Diagnosis:** Every result has an un-dismissible disclaimer reminding farmers that this is early guidance, not a lab certificate.
- **No Commercial Bias or Dosages:** We never name commercial brands, and we never output numerical dosages. Safe application rates depend on field size and weather—so we always mandate following the product label and confirming with a local agriculture officer.
- **Conservative Confidence:** Single leaf photos are capped at medium or low confidence, explicitly listing what other field signs are needed to confirm.
- **Honest Evaluation:** We do not claim unverified 95% accuracy statistics. We tested Crop Doctor by hand on our own real photo samples, documented transparently in our disclosure log.

Crop Doctor empowers Pakistani farmers with immediate, safe, and honest agronomic guidance—protecting crops, livelihoods, and food security. Thank you!"

---

## 📊 5 Slide Outlines

### Slide 1: The Problem
- **Headline:** The Crisis in Pakistan’s Fields
- **Key Points:**
  - 80%+ of cultivated land farmed by smallholders (wheat, cotton, rice, sugarcane, maize, tomato).
  - Severe shortage of agricultural extension officers in remote rural areas.
  - Farmers depend on local pesticide dealers who push costly, unnecessary brand-name chemical mixtures.
  - Existing digital solutions are in English, complex, and guess wildly on poor-quality photos.
- **Visuals:** Photo of a Pakistani farmer inspecting damaged crops; flow showing pesticide dealer markup cycle.

### Slide 2: Solution & SDG Alignment
- **Headline:** Crop Doctor (فصل ڈاکٹر) — Safe, Localized Guidance
- **Key Points:**
  - Multimodal leaf reasoning powered by Gemini 3.5 Flash.
  - Native Urdu interface (RTL Nastaliq) with instant English toggle.
  - Key output features: Urgency Badge, "Do NOT Do" list, Generic safe remedies.
  - Core safety principle: "Ask, Don't Guess" (no wild guesses on blurry photos).
  - Aligned with **SDG 2 (Zero Hunger)**, **SDG 12 (Responsible Consumption)**, **SDG 13 (Climate Action)**.
- **Visuals:** High-resolution screenshot of the Streamlit Urdu interface with badges and "Avoid" box.

### Slide 3: Live Demo
- **Headline:** Safe in Every Scenario
- **Key Points:**
  - **Scenario A (Diseased Leaf):** Plausible identification, urgency indicator, generic active ingredients, and WhatsApp share card.
  - **Scenario B (Blurry Leaf):** "Photo is too unclear to judge" -> specific retake guidance, zero diagnosis shown.
  - **Scenario C (Non-Plant):** "This does not look like a plant leaf" -> polite retake prompt, zero hallucinations.
- **Visuals:** Split screen showing the three app states: Valid Result, Unclear Photo Retake, Non-Plant Retake.

### Slide 4: System Architecture
- **Headline:** Robust, Decoupled Architecture
- **Key Points:**
  - **Frontend:** Streamlit with locked light theme (`.streamlit/config.toml`) for sunlight legibility.
  - **AI Engine:** Google Gemini 3.5 Flash (`google-genai` Python SDK).
  - **Contract Enforcement:** Pydantic `CropAnalysis` schema ensuring 100% structured JSON outputs.
  - **Strict Language Isolation:** Guaranteed pure Urdu or pure English per selection without mixing.
- **Visuals:** Clean architecture diagram showing Data Flow: Image -> Streamlit -> src/ai.py -> Gemini 3.5 Flash -> Pydantic Schema -> UI.

### Slide 5: Responsible AI & Evaluation
- **Headline:** Built for Farmer Safety, Not Hype
- **Key Points:**
  - **No Commercial Brands:** Recommends generic active ingredients only (e.g. copper oxychloride, sulfur).
  - **No Doses:** Never outputs grams/liters; always directs to product label and local extension officers.
  - **Conservative Confidence:** Single photo confidence is capped; suggests complementary field checks.
  - **Honest Evaluation:** Evaluated manually on real sample photos in `docs/DISCLOSURE.md`; zero invented accuracy statistics.
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
"We deliberately do not claim an unverified accuracy percentage like '95% accurate'. True diagnostic accuracy in agronomy requires laboratory culturing and controlled field trials, which cannot be measured during a hackathon. Instead, we evaluated our application by hand on a transparent set of real test photos documented in `docs/DISCLOSURE.md`. In our evaluation, the app produced plausible recommendations on all tested samples, properly refused to diagnose a blurry photo, and correctly rejected non-plant photos without hallucinating."

### 4. "Why don't you prescribe exact chemical doses (e.g. 50 grams per 20 liters of water)?"
**Answer:**  
"Prescribing exact chemical doses from a single photo is dangerous and irresponsible. The safe dosage of any agricultural chemical depends heavily on the crop's precise growth stage, formulation concentration from local suppliers, sprayer calibration, soil moisture, and ambient temperature. Giving fixed numbers risks chemical burn or pesticide resistance. We intentionally limit advice to generic active ingredients, instruct the farmer to read the product label, and emphasize confirming application rates with a local extension officer."

### 5. "How will smallholder farmers with low literacy or limited connectivity use this?"
**Answer:**  
"We focused heavily on accessibility:
1. The app requires zero text input—farmers just tap to upload or snap a photo and tap 'Analyze'.
2. The interface uses natural, spoken Urdu rendered in native Nastaliq script with visual color-coded badges for urgency and confidence.
3. For farmers who cannot read, the 3-line WhatsApp summary can be forwarded directly into village WhatsApp groups or sent to younger family members and extension workers for quick voice explanation."

### 6. "Why did you build this as a Streamlit web app rather than a native mobile app or WhatsApp bot?"
**Answer:**  
"For the hackathon, a Streamlit web app was the fastest way to deliver a zero-install, responsive experience that works on any smartphone browser or laptop. However, because our architecture is strictly decoupled—all Gemini integration and Pydantic validation live in `src/ai.py` and `src/schema.py` without UI coupling—this exact backend can be connected to a Twilio or Meta WhatsApp Business API webhook in less than a day."
