"""
app.py - Streamlit UI for Crop Doctor.
Leaf photo analyzer for Pakistani farmers with Urdu answers.
Calls src.ai for analysis; contains no direct Gemini API logic.
"""

import os
from pathlib import Path
import streamlit as st
from PIL import Image

from src.ai import analyze
from src.schema import CropAnalysis

# Set page title, favicon and layout
st.set_page_config(
    page_title="Crop Doctor - فصل ڈاکٹر",
    page_icon="🌱",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom CSS for Google Fonts, Color Palette (#F6F4EC, #2F6B3A, amber), and RTL styling
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Nastaliq+Urdu:wght@400;700&family=Segoe+UI:wght@400;600;700&display=swap');

    /* Urdu RTL typography */
    .urdu-text {
        font-family: 'Noto Nastaliq Urdu', serif;
        direction: rtl;
        text-align: right;
        line-height: 2.2;
    }

    .urdu-title {
        font-family: 'Noto Nastaliq Urdu', serif;
        direction: rtl;
        text-align: right;
        color: #2F6B3A;
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 0.2rem;
    }

    .urdu-subtitle {
        font-family: 'Noto Nastaliq Urdu', serif;
        direction: rtl;
        text-align: right;
        color: #4B5563;
        font-size: 1.15rem;
        margin-bottom: 1.2rem;
    }

    /* English header styling */
    .en-title {
        color: #2F6B3A;
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 0.2rem;
    }

    .en-subtitle {
        color: #4B5563;
        font-size: 1.1rem;
        margin-bottom: 1.2rem;
    }

    /* Card containers */
    .card {
        background-color: #FFFFFF;
        border-radius: 12px;
        padding: 1.25rem 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 6px rgba(0,0,0,0.06);
        border: 1px solid #E5E7EB;
    }

    /* Badges */
    .badge {
        display: inline-block;
        padding: 0.35rem 0.85rem;
        border-radius: 20px;
        font-size: 0.95rem;
        font-weight: 600;
        margin-right: 0.5rem;
        margin-left: 0.5rem;
        margin-bottom: 0.5rem;
    }

    /* Confidence Badge colors */
    .badge-conf-high {
        background-color: #E8F5E9;
        color: #2F6B3A;
        border: 1px solid #2F6B3A;
    }
    .badge-conf-medium {
        background-color: #FEF3C7;
        color: #B45309;
        border: 1px solid #D97706;
    }
    .badge-conf-low {
        background-color: #FEE2E2;
        color: #991B1B;
        border: 1px solid #DC2626;
    }

    /* Urgency Badge colors */
    .badge-urg-today {
        background-color: #FEE2E2;
        color: #991B1B;
        border: 1px solid #DC2626;
    }
    .badge-urg-this_week {
        background-color: #FEF3C7;
        color: #B45309;
        border: 1px solid #D97706;
    }
    .badge-urg-monitor {
        background-color: #EFF6FF;
        color: #1E40AF;
        border: 1px solid #3B82F6;
    }

    /* Do-Not-Do Warning Card */
    .avoid-card {
        background-color: #FFFBEB;
        border-right: 6px solid #D97706;
        border-left: 1px solid #FCD34D;
        border-top: 1px solid #FCD34D;
        border-bottom: 1px solid #FCD34D;
        border-radius: 10px;
        padding: 1rem 1.25rem;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }

    /* Retake guidance card */
    .retake-card {
        background-color: #FEF2F2;
        border: 1.5px solid #F87171;
        border-radius: 12px;
        padding: 1.5rem;
        margin-top: 1rem;
        margin-bottom: 1.5rem;
    }

    /* Pinned disclaimer */
    .disclaimer-box {
        background-color: #F3F4F6;
        border-top: 2px dashed #9CA3AF;
        padding: 1rem;
        border-radius: 8px;
        margin-top: 2rem;
        font-size: 0.9rem;
        color: #4B5563;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def render_confidence_badge(confidence: str, is_urdu: bool) -> str:
    """Format the HTML badge for confidence level."""
    conf = confidence.lower()
    if conf == "high":
        label = "اعتماد: زیادہ (High)" if is_urdu else "Confidence: High"
        css = "badge-conf-high"
    elif conf == "medium":
        label = "اعتماد: درمیانہ (Medium)" if is_urdu else "Confidence: Medium"
        css = "badge-conf-medium"
    else:
        label = "اعتماد: کم (Low)" if is_urdu else "Confidence: Low"
        css = "badge-conf-low"
    return f'<span class="badge {css}">{label}</span>'


def render_urgency_badge(urgency: str, is_urdu: bool) -> str:
    """Format the HTML badge for urgency level."""
    urg = urgency.lower()
    if urg == "today":
        label = "فوری توجہ: آج ہی" if is_urdu else "Urgency: Act Today"
        css = "badge-urg-today"
    elif urg == "this_week":
        label = "توجہ: اس ہفتے" if is_urdu else "Urgency: This Week"
        css = "badge-urg-this_week"
    else:
        label = "توجہ: نگرانی کریں" if is_urdu else "Urgency: Monitor"
        css = "badge-urg-monitor"
    return f'<span class="badge {css}">{label}</span>'


def main():
    # Initialize session state variables
    if "analysis_result" not in st.session_state:
        st.session_state.analysis_result = None
    if "current_image_bytes" not in st.session_state:
        st.session_state.current_image_bytes = None
    if "current_mime_type" not in st.session_state:
        st.session_state.current_mime_type = "image/jpeg"

    # Top Bar: Language toggle (Urdu default)
    col_title, col_lang = st.columns([3, 1])
    with col_lang:
        lang_choice = st.radio(
            "Language / زبان",
            options=["اردو", "English"],
            index=0,
            horizontal=True,
            label_visibility="collapsed",
        )
    is_urdu = lang_choice == "اردو"
    active_language = "Urdu" if is_urdu else "English"

    # Header section
    if is_urdu:
        st.markdown(
            """
            <div class="urdu-title">🌱 فصل ڈاکٹر (Crop Doctor)</div>
            <div class="urdu-subtitle">پاکستانی کسان بھائیوں کے لیے پودوں کے امراض اور پتوں کا فوری معائنہ</div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <div class="en-title">🌱 Crop Doctor</div>
            <div class="en-subtitle">Leaf photo analyzer and safe action plan for Pakistani farmers</div>
            """,
            unsafe_allow_html=True,
        )

    # -------------------------------------------------------------------------
    # STATE 1: UPLOAD & INPUT
    # -------------------------------------------------------------------------
    st.markdown("---")

    uploader_label = (
        "متاثرہ پودے کے پتے کی تصویر اپلوڈ کریں:"
        if is_urdu
        else "Upload affected crop leaf photo:"
    )

    uploaded_file = st.file_uploader(
        uploader_label,
        type=["jpg", "jpeg", "png", "webp"],
        help="Wheat, Cotton, Rice, Sugarcane, Maize, Tomato, etc.",
    )

    # Check for available public sample images
    samples_dir = Path("samples")
    sample_files = []
    if samples_dir.exists():
        sample_files = [
            f.name for f in samples_dir.glob("*")
            if f.suffix.lower() in [".jpg", ".jpeg", ".png", ".webp"]
        ]

    selected_sample = None
    if sample_files and uploaded_file is None:
        sample_prompt = "یا گیلری سے نمونہ تصویر منتخب کریں:" if is_urdu else "Or choose a sample photo:"
        sample_choice = st.selectbox(
            sample_prompt,
            options=["-- None / کوئی نہیں --"] + sample_files,
            index=0,
        )
        if sample_choice != "-- None / کوئی نہیں --":
            selected_sample = samples_dir / sample_choice

    # Determine active photo source
    if uploaded_file is not None:
        st.session_state.current_image_bytes = uploaded_file.getvalue()
        st.session_state.current_mime_type = uploaded_file.type or "image/jpeg"
        col_img, _ = st.columns([2, 1])
        with col_img:
            st.image(
                uploaded_file,
                caption="Uploaded Photo" if not is_urdu else "اپلوڈ شدہ تصویر",
                use_container_width=True,
            )
    elif selected_sample is not None and selected_sample.exists():
        st.session_state.current_image_bytes = selected_sample.read_bytes()
        ext = selected_sample.suffix.lower()
        st.session_state.current_mime_type = f"image/{ext.replace('.', '').replace('jpg', 'jpeg')}"
        col_img, _ = st.columns([2, 1])
        with col_img:
            st.image(
                str(selected_sample),
                caption=f"Sample: {selected_sample.name}",
                use_container_width=True,
            )
    else:
        st.session_state.current_image_bytes = None

    # Analyze button (disabled until a photo exists)
    has_photo = st.session_state.current_image_bytes is not None
    btn_label = "پتے کا معائنہ کریں 🔍" if is_urdu else "Analyze Leaf 🔍"

    if st.button(btn_label, disabled=not has_photo, type="primary", use_container_width=True):
        spinner_msg = (
            "پتے کا معائنہ کیا جا رہا ہے، براہ کرم انتظار فرمائیں..."
            if is_urdu
            else "Analyzing leaf photo with Gemini... please wait..."
        )
        with st.spinner(spinner_msg):
            try:
                result = analyze(
                    image_bytes=st.session_state.current_image_bytes,
                    mime_type=st.session_state.current_mime_type,
                    language=active_language,
                )
                st.session_state.analysis_result = result
            except Exception as e:
                err_msg = (
                    f"تجزیہ مکمل نہیں ہو سکا: {e}"
                    if is_urdu
                    else f"Analysis could not be completed: {e}"
                )
                st.error(err_msg)

    # -------------------------------------------------------------------------
    # RESULT EVALUATION & RENDERING
    # -------------------------------------------------------------------------
    result: CropAnalysis = st.session_state.analysis_result

    if result is not None:
        st.markdown("---")
        direction_class = "urdu-text" if is_urdu else ""

        # ---------------------------------------------------------------------
        # STATE 3: RETAKE / INADEQUATE PHOTO
        # (If is_plant_photo is False or needs_better_photo is True)
        # Show specific retake message and NO diagnosis/treatment results.
        # ---------------------------------------------------------------------
        if not result.is_plant_photo or result.needs_better_photo:
            retake_title = (
                "⚠️ تصویر ناکافی ہے - دوبارہ تصویر درکار ہے"
                if is_urdu
                else "⚠️ Better Photo Needed - No Diagnosis Made"
            )

            reason_text = ""
            if not result.is_plant_photo:
                reason_text = (
                    "اپلوڈ کی گئی تصویر میں پودے یا پتے کی موجودگی واضح نہیں ہے۔"
                    if is_urdu
                    else "The uploaded image does not appear to contain a crop leaf."
                )

            specific_request = result.better_photo_request or (
                "براہ کرم پتے کی صاف، واضح اور روشنی میں لی گئی تصویر دوبارہ اپلوڈ کریں۔"
                if is_urdu
                else "Please upload a clearer, well-lit photo of the affected leaf."
            )

            tips_header = "بہتر تصویر کے لیے تجاویز:" if is_urdu else "Tips for a better photo:"
            tips_items = [
                "کیمرے کو پتے کے قریب رکھیں تاکہ علامات اور دھبے واضح نظر آئیں۔"
                if is_urdu
                else "Hold camera steady and close to the affected spot or lesion.",
                "اگر کیڑے یا پھپھوندی نیچے ہے تو پتے کا نچلا رخ دکھائیں۔"
                if is_urdu
                else "If pests or mildew are on the underside, show the back of the leaf.",
                "دن کی قدرتی روشنی میں تصویر لیں۔"
                if is_urdu
                else "Capture in natural daylight without strong glare or dark shadows.",
            ]
            tips_html = "".join([f"<li>{t}</li>" for t in tips_items])

            st.markdown(
                f"""
                <div class="retake-card {direction_class}">
                    <h3 style="color: #DC2626; margin-top:0;">{retake_title}</h3>
                    {f'<p style="font-weight:600;">{reason_text}</p>' if reason_text else ''}
                    <div style="background-color: #FFFFFF; padding: 1rem; border-radius: 8px; border: 1px solid #FCA5A5; margin-bottom: 1rem;">
                        <strong>{'درکار تصویر کی تفصیل:' if is_urdu else 'Specific Request:'}</strong>
                        <p style="font-size: 1.1rem; margin-top: 0.3rem; color: #991B1B;">{specific_request}</p>
                    </div>
                    <p><strong>{tips_header}</strong></p>
                    <ul>{tips_html}</ul>
                </div>
                """,
                unsafe_allow_html=True,
            )

        # ---------------------------------------------------------------------
        # STATE 2: VALID RESULT CARD
        # ---------------------------------------------------------------------
        else:
            # Badges header
            conf_badge = render_confidence_badge(result.confidence, is_urdu)
            urg_badge = render_urgency_badge(result.urgency, is_urdu)

            # Identification section
            st.markdown(
                f"""
                <div class="card {direction_class}">
                    <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; margin-bottom: 0.75rem;">
                        <div>
                            <span style="font-size: 1.4rem; font-weight:700; color: #2F6B3A;">
                                {'فصل:' if is_urdu else 'Crop:'} {result.crop}
                            </span>
                        </div>
                        <div>
                            {conf_badge}
                            {urg_badge}
                        </div>
                    </div>
                    <div style="font-size: 1.25rem; font-weight: 600; color: #1F2937; margin-bottom: 0.5rem;">
                        {'امکانی مسئلہ:' if is_urdu else 'Likely Issue:'} 
                        <span style="color: #B45309;">{result.likely_problem}</span>
                    </div>
                    <div style="font-size: 0.9rem; color: #6B7280;">
                        {'نوٹ: یہ حتمی تشخیص نہیں ہے، بلکہ علامات کی بنیاد پر امکانی رہنمائی ہے۔' if is_urdu else 'Note: This is guidance based on observed leaf symptoms, not a certified diagnosis.'}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            # Treatment Steps Card
            if result.treatment_steps:
                steps_header = "مجوزہ محفوظ اقدامات (Treatment Steps)" if is_urdu else "Recommended Safe Actions"
                steps_items = "".join([f"<li style='margin-bottom: 0.5rem;'>{s}</li>" for s in result.treatment_steps])
                st.markdown(
                    f"""
                    <div class="card {direction_class}">
                        <h4 style="color: #2F6B3A; margin-top:0;">✅ {steps_header}</h4>
                        <ol style="padding-right: 1.5rem; padding-left: 1.5rem;">
                            {steps_items}
                        </ol>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            # "Do NOT Do" List (Avoid List)
            if result.avoid_list:
                avoid_header = "یہ غلطیاں ہرگز نہ کریں (What NOT to do)" if is_urdu else "Actions to AVOID (Do Not Do)"
                avoid_items = "".join([f"<li style='margin-bottom: 0.4rem;'>{a}</li>" for a in result.avoid_list])
                st.markdown(
                    f"""
                    <div class="avoid-card {direction_class}">
                        <h4 style="color: #B45309; margin-top:0;">⛔ {avoid_header}</h4>
                        <ul style="padding-right: 1.5rem; padding-left: 1.5rem;">
                            {avoid_items}
                        </ul>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            # Prevention Tips
            if result.prevention_tips:
                prev_header = "آئندہ بچاؤ کی تدابیر (Prevention Tips)" if is_urdu else "Prevention Tips for Next Season"
                prev_items = "".join([f"<li style='margin-bottom: 0.4rem;'>{p}</li>" for p in result.prevention_tips])
                st.markdown(
                    f"""
                    <div class="card {direction_class}">
                        <h4 style="color: #2F6B3A; margin-top:0;">🛡️ {prev_header}</h4>
                        <ul style="padding-right: 1.5rem; padding-left: 1.5rem;">
                            {prev_items}
                        </ul>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            # When to see an expert
            if result.when_to_see_expert:
                expert_header = "زرعی افسر سے کب رابطہ کریں:" if is_urdu else "When to Consult an Agriculture Officer:"
                st.markdown(
                    f"""
                    <div class="card {direction_class}" style="border-left: 4px solid #2F6B3A; border-right: 4px solid #2F6B3A;">
                        <h4 style="color: #1F2937; margin-top:0;">👨‍🌾 {expert_header}</h4>
                        <p style="margin-bottom: 0;">{result.when_to_see_expert}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            # WhatsApp Summary Box
            if result.whatsapp_summary:
                with st.expander("📲 واٹس ایپ خلاصہ (WhatsApp Summary)" if is_urdu else "📲 WhatsApp Summary"):
                    st.code(result.whatsapp_summary, language="text")

        # ---------------------------------------------------------------------
        # PINNED DISCLAIMER (Shown on every result state)
        # ---------------------------------------------------------------------
        disclaimer_text = (
            "⚠️ <strong>ضروری وضاحت:</strong> یہ ایپ صرف عام معلوماتی رہنمائی کے لیے تیار کی گئی ہے اور یہ کوئی مستند یا حتمی تشخیصی لیب رپورٹ نہیں ہے۔ کسی بھی زرعی زہر، کھاد یا سپرے کے استعمال سے قبل اپنے مقامی محکمہ زراعت (فیلڈ آفیسر) سے رہنمائی ضرور لیں۔"
            if is_urdu
            else "⚠️ <strong>Disclaimer:</strong> This application provides general guidance only and is not a certified laboratory diagnosis. Always consult a local agriculture extension officer before purchasing or applying any pesticides or chemical treatments."
        )
        st.markdown(
            f"""
            <div class="disclaimer-box {direction_class}">
                {disclaimer_text}
            </div>
            """,
            unsafe_allow_html=True,
        )


if __name__ == "__main__":
    main()
