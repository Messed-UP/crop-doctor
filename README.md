# Crop Doctor (فصل ڈاکٹر)

AI-powered leaf photo analyzer providing actionable, safe crop guidance for Pakistani smallholder farmers in natural Urdu (with an English toggle), powered by the Gemini API via Google AI Studio and developed with Google Antigravity.

**Hackathon:** Build with Google - CUI Tech Fest FA'26  
**Domain:** Agriculture & Food Security | **SDG:** Goal 2 (Zero Hunger) — also supporting SDG 12 (Responsible Consumption) and SDG 13 (Climate Action)

---

## 🌾 The Real Problem
Over 80% of cultivated land in Pakistan is managed by smallholder farmers who grow staples such as wheat, cotton, rice, sugarcane, maize, and vegetables. When fungal diseases, bacterial blights, or insect pests attack, farmers encounter severe bottlenecks:
1. **Severe Extension Shortage:** Public agriculture extension workers are stretched across expansive districts. In rural Pakistan, having an expert physically inspect a smallholder field can take days or weeks—by which time a pathogen may have wiped out an entire yield.
2. **Pesticide Dealer Conflict of Interest:** Left with no immediate support, farmers take diseased leaves to local commission agents or pesticide shopkeepers. These dealers routinely push expensive, multi-brand chemical cocktails with high profit margins. Farmers end up applying unnecessary pesticides that burn crops, degrade soil biodiversity, and trap families in chronic debt cycles.
3. **Language & Complexity Barriers:** Existing agricultural apps are predominantly in English, filled with academic jargon, or designed around complex dashboards that local farmers cannot understand.
4. **Dangerous Hallucinations in Existing Tools:** Typical AI plant-disease scanners force every uploaded picture into a disease category, even if the image is out of focus, taken in darkness, or shows a non-plant object.

---

## 💡 The Solution
**Crop Doctor** transforms any camera smartphone into a safe, conservative frontline agronomic guide:
- **Natural Urdu Guidance:** Delivered right-to-left in native Nastaliq script (`Noto Nastaliq Urdu`) with simple, farmer-friendly terms (English toggle available with one tap).
- **"Ask, Don't Guess" Philosophy:** If a leaf photo is blurry, dark, or ambiguous, Crop Doctor refuses to hallucinate a disease and asks for a specific better photo (e.g. leaf underside or daylight shot). Non-plant photos are politely rejected.
- **Urgency & Confidence Badges:** Color-coded urgency ratings (`Act Today`, `This Week`, `Monitor`) and conservative confidence indicators (`Low`, `Medium`, `High`) because a single photo can never provide 100% certainty.
- **"Do NOT Do" List:** A prominent warning box alerting farmers to avoid critical errors (such as spraying during high winds, tank-mixing incompatible chemicals, or harvesting immediately after chemical spraying).
- **Generic Safe Remedies Only:** Names generic agronomic practices (sanitation, aeration, drainage) and active chemical ingredients (e.g. copper oxychloride, sulfur)—strictly free of commercial brand names or fixed numerical doses.
- **WhatsApp Summary:** Generates a concise 3-line Urdu bullet summary ready to be shared with village farming groups or local extension officers.
- **Pinned Visible Disclaimer:** Emphasized on every result screen stating that guidance is informational and cannot replace a laboratory diagnosis.

---

## 🚶 Farmer User Journey

```text
  [1. Open App]
        │  Farmer opens the web app on any smartphone browser.
        │  App loads immediately in clean Urdu with daylight-legible light theme.
        ▼
  [2. Upload / Select Leaf Photo]
        │  Farmer uploads a photo of an affected leaf, or selects from sample gallery.
        │  Live image preview appears; "Analyze Leaf" button activates.
        ▼
  [3. Multi-Scenario Intelligent Triage]
        ├─► SCENARIO A: Valid Crop Leaf Photo
        │     • Displays Crop Name & Likely Issue (candidly framed as "Likely").
        │     • Highlights Urgency badge and Confidence level.
        │     • Provides Step-by-step generic cultural and active ingredient guidance.
        │     • Shows "Do NOT Do" avoidance card and future prevention practices.
        │     • Offers copyable WhatsApp summary and triggers for expert consultation.
        │
        ├─► SCENARIO B: Blurry or Low-Light Photo ("Ask, Don't Guess")
        │     • App states: "The photo is too unclear to judge".
        │     • ZERO diagnosis or chemical advice is shown.
        │     • Provides specific retake guidance (e.g., hold closer, focus on lesions, use daylight).
        │
        └─► SCENARIO C: Non-Plant Image
              • App states: "This does not look like a plant leaf".
              • Rejection notice asks the user to upload a clear crop leaf photo.
        ▼
  [4. Safe Action & Community Sharing]
        Farmer avoids harmful pesticide dealer markups, adopts safe cultural practices,
        and forwards the WhatsApp summary to their local extension officer for confirmation.
```

---

## 🏗️ Architecture & Data Flow

```text
[Farmer Leaf Photo (JPG/PNG/WEBP)]
               │
               ▼
   [Streamlit Frontend (app.py)]
     ├── Light Theme Lock (.streamlit/config.toml)
     ├── Language Toggle (Urdu RTL / English)
     └── Image Preview & Validation
               │
               ▼
      [Backend Service (src/ai.py)]
        ├── Prompt Builder (src/prompts.py)
        │     ├── Strict Language Isolation (No mixing)
        │     ├── Generic Practices & Active Ingredients Only (No brands/doses)
        │     └── "Ask, Don't Guess" quality triggers
        │
        ├── Resilient Dispatch:
        │     ├── Primary Model: MODEL_NAME = "gemini-3.5-flash"
        │     ├── Exponential Backoff: Retries up to 3 times (waits: 2s, 4s, 8s) on 503/429
        │     └── Fallback Model: FALLBACK_MODEL = "gemini-2.5-flash" (1 attempt if primary fails)
        │
        ├── Pydantic Contract Enforcement:
        │     └── response_schema = CropAnalysis (src/schema.py)
        │
        └── API Key Sanitization:
              └── Strips/redacts sensitive keys from all error traces
               │
               ▼
   [Results Rendering (app.py)]
     ├── State 1: Upload & Image Selection
     ├── State 2: Valid Diagnostic Card with RTL Urdu Styling
     └── State 3: Separated Retake Guidance (No Diagnosis)
```

---

## 🌐 Google Technologies Used
- **Gemini API via Google AI Studio (`gemini-3.5-flash` & `gemini-2.5-flash`):**
  - **Gemini 3.5 Flash:** Primary multimodal engine for zero-shot leaf symptom reasoning, non-plant detection, image clarity assessment, and structured JSON output.
  - **Gemini 2.5 Flash:** Automatic fallback model ensuring system uptime during upstream transient errors.
  - **`google-genai` Python SDK:** Modern official Google GenAI SDK utilizing structured JSON schemas (`response_schema=CropAnalysis`).
- **Google Antigravity:** AI coding agent used throughout development for architectural scaffolding, Pydantic data modeling, safe prompt engineering, and RTL UI implementation.
- **Google Fonts (`Noto Nastaliq Urdu`):** High-quality native Nastaliq typography providing authentic, legible Urdu for Pakistani farmers.

---

## 📁 Repository Structure

```text
crop-doctor/
├── .streamlit/
│   └── config.toml           # Locked light theme config (daylight readable: #F6F4EC, #2F6B3A)
├── docs/
│   ├── DISCLOSURE.md         # Full transparency: AI tools, models, libraries, samples & manual evaluation
│   ├── PITCH.md              # 5-minute script, 3-minute script, 5 slide outlines, 6 judge Q&As
│   └── REQUIREMENTS.md       # Product specifications and hackathon guidelines
├── samples/                  # Real test photos (healthy, diseased, blurry, non-plant)
├── scripts/
│   └── try_ai.py             # CLI runner for quick Gemini leaf analysis (git-ignored)
├── src/
│   ├── __init__.py           # Python package marker
│   ├── ai.py                 # Gemini client, retry logic, fallback model, analyze()
│   ├── prompts.py            # Prompt engineering, language isolation, safety guardrails
│   └── schema.py             # CropAnalysis Pydantic data model
├── app.py                    # Streamlit web UI (pure UI logic, 3 application states)
├── AGENTS.md                 # Project rules, constraints, and instructions
├── requirements.txt          # Pinned dependencies (google-genai, streamlit, pillow, pydantic)
└── README.md                 # Complete project documentation
```

---

## 🚀 How to Run Locally

### Prerequisites
- Python 3.13 (or 3.10+) installed with the `py` launcher.
- A Gemini API key from [Google AI Studio](https://aistudio.google.com/).

### Installation & Launch

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
     *(Close and reopen your terminal after running `setx`)*
   - **Linux / macOS:**
     ```bash
     export GEMINI_API_KEY="your-gemini-api-key"
     ```

4. **Launch the application:**
   ```bash
   py -m streamlit run app.py
   ```

5. Open your browser at `http://localhost:8501`.

---

## ⚠️ Limitations & Responsible AI
- **Guidance, Not Certified Diagnosis:**
- Crop Doctor gives guidance only. It is not a confirmed diagnosis.
- Results depend on photo quality, lighting and crop type, and may be wrong.
- Tested only on a small set of our own photos; accuracy has not been validated.
- It does not replace a local agriculture officer, especially for severe or fast-spreading problems.
- Treatment suggestions are generic; always follow the product label and local advice.
 Crop Doctor is designed as an early decision-support aid. It does not replace laboratory tissue culturing, microscopic spore analysis, or official extension officer field visits.
- **No Accuracy Claims:** We do not claim arbitrary or unverified diagnostic statistics (e.g. "98% accurate"). Formal agronomic validation requires multi-season field trials across diverse agro-ecological zones. Our evaluation in `docs/DISCLOSURE.md` represents a qualitative manual check on our own sample images.
- **Single-Leaf Foliar Scope:** Single-photo inspection cannot detect systemic root-knot nematodes, subterranean crown rot, vascular wilt, or complex multi-pathogen co-infections.
- **Lighting & Photo Quality Sensitivity:** Severe shadows, intense glare, or low camera resolution degrade visual cues. To mitigate this, our "Ask, Don't Guess" rule actively refuses analysis on unclear images.
- **Generic Ingredients Only:** We intentionally avoid commercial trade names and specific chemical dosages. Exact dosages require adjustments for crop growth phase, water volume, and local weather conditions; farmers must follow the manufacturer's container label and verify with an agriculture officer.
- **Connectivity Dependency:** Requires an active internet connection to communicate with the Gemini API.

---

## 👥 Team
- **Project:** Crop Doctor (Build with Google - CUI Tech Fest FA'26)
- **Built with:** Google Antigravity & Google Gemini API
