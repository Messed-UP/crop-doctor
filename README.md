# Crop Doctor (فصل ڈاکٹر)

AI-powered leaf photo analyzer providing actionable, safe crop guidance for Pakistani smallholder farmers in natural Urdu (with an English toggle), powered by the Gemini API.

**Hackathon:** Build with Google - CUI Tech Fest FA'26  
**Domain:** Agriculture & Food Security | **SDG:** Goal 2 (Zero Hunger) — also supporting SDG 12 (Responsible Consumption) and SDG 13 (Climate Action)

---

## 🌾 The Problem
In Pakistan, over 80% of farming land is cultivated by smallholder farmers growing staples like wheat, cotton, rice, sugarcane, maize, and vegetables. When foliar diseases or pests strike, farmers face critical bottlenecks:
1. **Shortage of Extension Officers:** Public agriculture extension officers cannot reach remote villages in time.
2. **Pesticide Dealer Misguidance:** Farmers turn to local pesticide shopkeepers who often recommend expensive, brand-name chemical mixtures that may be unnecessary, ineffective, or harmful to crops and soil.
3. **Language & Literacy Barriers:** Existing plant-care applications provide complex English reports or technical jargon that local farmers cannot interpret.
4. **Dangerous Guesswork:** Existing tools often guess a disease even when an image is out-of-focus or non-crop, leading to incorrect chemical spraying.

---

## 💡 The Solution
**Crop Doctor** turns any smartphone camera into a frontline, conservative agronomy advisor:
- **Instant Urdu Action Plan:** Farmers upload a leaf photo and receive an easy-to-read result rendered right-to-left in clean Urdu script (using `Noto Nastaliq Urdu`), with an instant toggle to English.
- **"Ask, Don't Guess":** If a photo is blurry, dark, or ambiguous, the model refrains from diagnosing and explicitly asks for a better photo (e.g. underside of the leaf or daylight shot). Non-plant photos are politely rejected.
- **Urgency & Confidence Indicators:** Clear visual badges show urgency (`Today`, `This Week`, `Monitor`) and confidence (`Low`, `Medium`, `High`), capped conservatively because single-photo analysis is uncertain.
- **"Do NOT Do" List:** A prominent warning box listing dangerous actions to avoid (e.g. spraying in strong wind, improper chemical mixing, harvesting right after spraying).
- **Generic Safe Advice Only:** Emphasizes cultural sanitation and generic active ingredients only—strictly no brand names and no numerical doses. Always points farmers to confirm with an agriculture officer.
- **WhatsApp Summary:** Prepares a 3-4 line summary ready to copy and share directly with community groups or local officers.
- **Pinned Disclaimer:** Transparently displayed on every screen stating that output is guidance, not a certified lab diagnosis.

---

## 🏗️ Architecture & Data Flow

```text
[Farmer's Leaf Photo]
         │
         ▼
[Streamlit Frontend (app.py)]
  ├── Locked Light Theme (.streamlit/config.toml)
  ├── Bilingual Toggle (Urdu RTL / English)
  └── Image Validation (Upload or Sample Picker)
         │
         ▼
[Backend Service (src/ai.py)]
  ├── Single Model Constant: MODEL_NAME = "gemini-3.5-flash"
  └── Prompt Construction (src/prompts.py)
         │
         ▼
[Google Gemini API (gemini-3.5-flash)]
  ├── Multimodal Leaf Analysis
  ├── Enforced Structured JSON (response_schema=CropAnalysis)
  └── Strict Language Isolation
         │
         ▼
[Pydantic Validation (src/schema.py)]
  └── Validates CropAnalysis Schema
         │
         ▼
[Results Presentation (app.py)]
  ├── State 1: Upload & Image Preview
  ├── State 2: Valid Diagnosis Card (Badges, Steps, Avoid List, Expert Trigger)
  └── State 3: Retake Request ("Ask, Don't Guess" - No Diagnosis Made)
```

---

## 🌐 Google Technologies Used
- **Gemini API (`gemini-3.5-flash`) via Google AI Studio:** Multimodal vision-language model used for image understanding, agronomic symptom reasoning, strict JSON structured outputs, and natural Urdu response generation.
- **`google-genai` Python SDK:** Modern Google GenAI client library communicating with the Gemini API.
- **Google Fonts (`Noto Nastaliq Urdu`):** Native Nastaliq typography providing authentic, readable right-to-left Urdu for Pakistani farmers.

---

## 📁 Repository Structure

```text
crop-doctor/
├── .streamlit/
│   └── config.toml           # Locked light theme config (brand colors & background)
├── docs/
│   ├── DISCLOSURE.md         # Full transparency: AI tools, libraries, samples & manual evaluation
│   ├── PITCH.md              # 3-minute presentation script, 5 slide outlines, 6 judge Q&As
│   └── REQUIREMENTS.md       # Product specifications and hackathon rules
├── samples/                  # Public and real sample photos (healthy, diseased, blurry, non-plant)
├── scripts/
│   └── try_ai.py             # CLI test runner for Gemini analysis (git-ignored)
├── src/
│   ├── __init__.py           # Python package marker
│   ├── ai.py                 # Gemini client initialization, MODEL_NAME constant, analyze()
│   ├── prompts.py            # Prompt engineering, language isolation & safety guardrails
│   └── schema.py             # CropAnalysis Pydantic response model
├── app.py                    # Streamlit web UI (pure UI logic, 3 application states)
├── AGENTS.md                 # Project constraints and agent rules
├── requirements.txt          # Pinned dependencies (google-genai, streamlit, pillow, pydantic)
└── README.md                 # Project overview and run instructions
```

---

## 🚀 How to Run Locally

### Prerequisites
- Python 3.13 (or 3.10+) installed via the `py` launcher.
- A Gemini API key from [Google AI Studio](https://aistudio.google.com/).

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/crop-doctor.git
   cd crop-doctor
   ```

2. **Install dependencies:**
   ```bash
   py -m pip install -r requirements.txt
   ```

3. **Set your Gemini API key:**
   - **Windows (Command Prompt / PowerShell):**
     ```cmd
     setx GEMINI_API_KEY "your-gemini-api-key"
     ```
     *(Close and reopen your terminal window after running `setx`)*
   - **Linux / macOS:**
     ```bash
     export GEMINI_API_KEY="your-gemini-api-key"
     ```

4. **Launch the application:**
   ```bash
   py -m streamlit run app.py
   ```

5. Open `http://localhost:8501` in your browser.

---

## 🛡️ Responsible AI & Safety Principles
- **Guidance, Not Diagnosis:** Every screen features an un-dismissible disclaimer reminding users that Crop Doctor provides early guidance and cannot replace a laboratory diagnosis.
- **No Commercial Bias:** Strictly recommends generic agronomic practices and active ingredients (e.g. copper oxychloride, sulfur). Never recommends commercial brands or chemical trade names.
- **No Numerical Dosages:** Never outputs specific chemical dosages or application rates, preventing crop burns or under-dosage resistance. Always instructs farmers to follow product labels and consult a field officer.
- **Conservative Confidence:** Acknowledges the inherent uncertainty of single-leaf photos; confidence is capped at Medium/Low for typical single shots, and the model lists what extra signs would confirm the problem.
- **Honest Evaluation:** No fabricated accuracy claims (e.g. "98% accurate"). Evaluated transparently on a small manual test sample in `docs/DISCLOSURE.md`.

---

## 👥 Team
- **Project:** Crop Doctor (CUI Tech Fest FA'26)
- **Assisted by:** Google Antigravity (AI Coding Agent)
