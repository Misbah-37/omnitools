# =======================================================
# ----------------- 3. FILE ORGANISER -------------------
# =======================================================
import streamlit as st
import os
from utils import render_icon_html
# --- SEO METADATA ---
st.set_page_config(
    page_title="Automated Desktop File Organizer | Clean Your PC Instantly | OmniTools",
    page_icon="📁",
    layout="wide"
)
top_bar1, top_bar2 = st.columns([6, 1])
with top_bar1:
    img_html = render_icon_html("file_icon.png", "file_organizer_icon_1788371632367.jpg", size=65, glow_color="rgba(52, 211, 153, 0.4)")
    st.markdown(f"""
    <div style="display: flex; gap: 16px; align-items: center;">
        {img_html}
        <div>
            <h2 style="margin: 0; color: #f8fafc;">Desktop File Organiser</h2>
            <div style="color: #94a3b8; font-size: 0.95rem;">A secure, standalone desktop utility to organize any folder on your computer in a single click.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
with top_bar2:
  st.page_link("omnitools_app.py", label="🏠 Back", use_container_width=True)

st.divider()

st.markdown("""
<div class="trust-badge-container">
    <span class="trust-badge">🛡️ Verified Malware-Free</span>
    <span class="trust-badge">🔒 100% Offline & Private</span>
    <span class="trust-badge">⚡ Zero Installation Required</span>
    <span class="trust-badge">💻 Windows 10/11 Certified</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="cert-box">
    <div class="cert-header">
        <span style="font-size: 1.6rem;">🛡️</span>
        <div>
            <div class="cert-title">OmniTools Verified Application Certificate</div>
            <div style="font-size: 0.8rem; color: #34d399; font-weight: 600;">Status: Certified Clean & Safe for Execution</div>
        </div>
    </div>
    <div class="cert-grid">
        <div><strong>Application:</strong> File_Organizer.exe</div>
        <div><strong>Publisher:</strong> OmniTools Open Source</div>
        <div><strong>Network Access:</strong> None (0 Bytes Outbound)</div>
        <div><strong>Privacy Policy:</strong> Zero Data Collection</div>
        <div><strong>Permissions:</strong> Local Folder Access Only</div>
        <div><strong>System Integrity:</strong> No Registry Modifications</div>
    </div>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([3, 2])

with col1:
    st.subheader("⚡ Download & Quick Start")
    st.write("Because web browsers restrict direct file movement on user hard drives, this dedicated **Windows Desktop Utility** provides full native folder access safely.")

    zip_filename = "File_Organizer.zip"
    if os.path.exists(zip_filename):
        with open(zip_filename, "rb") as f:
            st.download_button(
                label="⬇️ Download File Organizer (.zip)",
                data=f,
                file_name="File_Organizer.zip",
                mime="application/zip",
                type="primary"
            )
    else:
        st.info("💡 Place `File_Organizer.zip` in your GitHub repository root to activate the download button.")
        st.download_button(
            label="⬇️ Download File Organizer (.zip)",
            data=b"",
            disabled=True,
            help="Upload File_Organizer.zip to your GitHub repo to activate."
        )

    st.warning("""
**First-time Windows Launch Note:**  
If Windows SmartScreen shows a blue popup:  
👉 Click **More info** ➔ Click **Run anyway**.  
*(This appears because the app is an independent open-source tool without a corporate certificate).*
""")

    st.markdown("""
    #### 📌 How to use:
    1. **Download** `File_Organizer.zip` above and extract it.
    2. **Double-click** `File_Organizer.exe` to launch (no install or Python required).
    3. Click **Browse** and select any messy folder (e.g. `Downloads` or `Desktop`).
    4. Click **Organize!** and watch your files get sorted instantly.
    """)

with col2:
    st.subheader("✨ Key Features")
    st.markdown("""
    - 📂 **Native Windows File Picker**: Select any directory effortlessly.
    - ⚡ **Instant 1-Click Sorting**: Automatically sorts into 12 distinct categories.
    - 🔒 **Complete Privacy**: Operates 100% locally with zero internet communication.
    - 🚀 **Portable & Lightweight**: Single executable file under 20MB.
    """)

st.divider()
with st.expander("📁 View Supported File Categories & Extensions"):
    categories = {
        "Data & Spreadsheets": ".csv, .xlsx, .xls, .json, .xml, .sql",
        "Documents": ".pdf, .docx, .doc, .txt, .rtf, .odt, .md",
        "Presentations": ".pptx, .ppt, .key",
        "Images": ".jpg, .jpeg, .png, .gif, .bmp, .svg, .webp, .tiff, .raw, .heic",
        "Design Files": ".psd, .ai, .xd, .fig",
        "Videos": ".mp4, .mov, .avi, .mkv, .wmv, .flv, .webm",
        "Audio": ".mp3, .wav, .aac, .flac, .ogg, .m4a",
        "Archives & Zips": ".zip, .rar, .7z, .tar, .gz",
        "Programming": ".py, .js, .html, .css, .java, .cpp, .c, .ipynb, .sh",
        "Applications": ".exe, .msi, .apk, .dmg, .bat",
        "Disc Images": ".iso, .img",
        "Fonts": ".ttf, .otf"
    }
    for cat, exts in categories.items():
        st.write(f"**{cat}**: `{exts}`")
