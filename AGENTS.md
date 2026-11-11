# AGENTS.md - Rules for the AI coding agent (Antigravity)

Project: **Crop Doctor** - leaf photo analyzer for Pakistani farmers, Urdu answers, powered by the Gemini API.
Hackathon: Build with Google (CUI Tech Fest FA'26). Read `docs/REQUIREMENTS.md` before writing code.

## You MAY
- Create and edit files inside this repo only.
- Write Python for: `app.py` (Streamlit UI), `src/ai.py` (Gemini call), `src/prompts.py` (prompt text), `src/schema.py` (response shape). Optional features get their own new file in `src/`.
- Install packages with `py -m pip install ...` and record them in `requirements.txt`.
- Run the app with `py -m streamlit run app.py`.
- Run `git status`, `git add .`, `git commit -m "<clear message>"` after each working feature.
- Run `git pull` before `git push`.
- Update `README.md` and `docs/DISCLOSURE.md` as features are added.
- Explain any code in plain language when asked.

## You MUST
- Read the Gemini key ONLY from the `GEMINI_API_KEY` environment variable.
- Keep the model name in ONE place (`src/ai.py`, constant `MODEL_NAME`).
- Return structured JSON from Gemini (schema in `docs/REQUIREMENTS.md`) and validate it before showing it.
- Show a visible disclaimer on every result: guidance only, not a confirmed diagnosis.
- Show confidence and urgency on every result.
- If confidence is low or the photo is unclear, ask for a specific better photo instead of guessing.
- Name generic practices or active ingredients only, never brand names, and always say to confirm with an agriculture officer.
- Wrap every API call in try/except and show a friendly error message.
- Keep code simple and commented so a beginner can explain it on stage.
- Use `py`, never plain `python`.
- app.py only calls other modules; no AI logic inside it.

## You MUST NOT
- Write, print, log or commit any API key or secret.
- Commit `.env`, keys, or personal data.
- Run `git push --force`, `git reset --hard`, `git clean`, or delete branches.
- Delete or overwrite files outside this repo.
- Add accuracy claims (like "95% accurate") that were not measured.
- Present output as a medical, professional or verified diagnosis.
- Add a database, login, mobile app, new frameworks, or paid services.
- Add Google Search grounding or any new Google Cloud service without asking first.
- Install anything outside `docs/REQUIREMENTS.md` without asking first.
- Use images or datasets that are private or have no known public source.

## Ask the human first before
- Changing the folder structure.
- Adding any dependency or Google Cloud service.
- Doing anything that costs money.
- Any command you are unsure is safe.

## Commit style
Short and specific, for example: `add gemini call with structured output`, `add urgency badge`.
