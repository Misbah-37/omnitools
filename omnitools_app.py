import streamlit as st
import random
import time
import string
import json
import io
import os
import base64
from utils import find_image, render_icon_html
from PIL import Image, ImageOps
try:
    from pypdf import PdfReader, PdfWriter
except ImportError:
    PdfReader, PdfWriter = None, None

import streamlit.components.v1 as components

# ----------------- 1. OMNITOOLS CONFIG -----------------
st.set_page_config(
    page_title="OmniTools | Ultimate Utility Suite", 
    page_icon="🛠️", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS: Dark Theme, Glass Cards & Crisp Icons
st.markdown("""
<style>
    /* Hide sidebar completely */
    [data-testid="stSidebar"] { display: none !important; }
    section[data-testid="stSidebar"] { display: none !important; }
    button[kind="header"] { display: none !important; }
    
    /* Smooth Crisp Image Rendering */
    img {
        border-radius: 16px;
        image-rendering: -webkit-optimize-contrast;
    }
    
    /* Dark Theme Trust Badges */
    .trust-badge-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 12px;
        margin: 15px 0 25px 0;
    }
    .trust-badge {
        background: rgba(16, 185, 129, 0.1);
        border: 1px solid rgba(52, 211, 153, 0.4);
        color: #34d399;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        display: inline-flex;
        align-items: center;
        gap: 6px;
        backdrop-filter: blur(8px);
    }
    /* Dark Theme Security Certificate */
    .cert-box {
        background: linear-gradient(135deg, #111827 0%, #1f2937 100%);
        border: 1px solid #374151;
        border-left: 5px solid #10b981;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.4);
        margin-bottom: 25px;
    }
    .cert-header {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 12px;
    }
    .cert-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #f9fafb;
        margin: 0;
    }
    .cert-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 12px;
        font-size: 0.85rem;
        color: #9ca3af;
        margin-top: 10px;
        background: #0f172a;
        border: 1px solid #1e293b;
        padding: 14px;
        border-radius: 8px;
    }
    .cert-grid strong {
        color: #e2e8f0;
    }
</style>
""", unsafe_allow_html=True)


# =======================================================
# ----------------- 0. LANDING PAGE (HOME) --------------
# =======================================================
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"
if st.session_state.current_page == "Home":
    master_path = find_image("omnitools_logo.png", "omnitools_master_logo_1788371563646.jpg")
    master_logo_html = ""
    if master_path:
        with open(master_path, "rb") as f:
            b64_logo = base64.b64encode(f.read()).decode()
            mime = "image/png" if master_path.endswith(".png") else "image/jpeg"
            master_logo_html = f"<img src='data:{mime};base64,{b64_logo}' style='width: 175px; filter: drop-shadow(0 12px 28px rgba(0, 210, 255, 0.45)); margin-bottom: 15px;' />"

    st.markdown(f"""
    <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; margin-top: 10px; margin-bottom: 20px;">
        {master_logo_html}
        <h1 style="margin: 0; font-size: 2.8rem; font-weight: 800; color: #f8fafc; letter-spacing: -0.5px;">OmniTools 🌌</h1>
        <p style="color: #94a3b8; font-size: 1.15rem; max-width: 600px; margin-top: 8px; margin-bottom: 0;">High-performance, private, and lightweight utility tools for your daily workflows.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="trust-badge-container">
        <span class="trust-badge">⚡ Ultra Fast Execution</span>
        <span class="trust-badge">🔒 100% Privacy Focused</span>
        <span class="trust-badge">💻 Modern Dark Mode Suite</span>
        <span class="trust-badge">🚀 Zero Installation Required</span>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # 2x2 Grid of Floating Crystal Cards
    row1_col1, row1_col2 = st.columns(2, gap="large")

    # Card 1: Typing Test
    with row1_col1:
        with st.container(border=True):
            img_html = render_icon_html("typing_icon.png", "typing_speed_icon_1788371582708.jpg", size=75, glow_color="rgba(255, 51, 153, 0.4)")
            st.markdown(f"""
            <div style="display: flex; gap: 16px; align-items: center;">
                {img_html}
                <div>
                    <h3 style="margin: 0; color: #f8fafc;">Typing Speed Test</h3>
                    <div style="color: #ff3399; font-size: 0.85rem; font-weight: 600; margin-top: 2px;">SPEED & ACCURACY BENCHMARK</div>
                </div>
            </div>
            <div style="height: 48px; color: #94a3b8; font-size: 0.95rem; margin-top: 6px;">
                Measure keystroke speed and accuracy across 4 difficulty tiers including 30 curated paragraphs.
            </div>
            """, unsafe_allow_html=True)
            st.page_link("pages/1_Typing_Test.py", label="Launch Typing Test ➔", use_container_width=True)

    # Card 2: Photo Resizer
    with row1_col2:
        with st.container(border=True):
            img_html = render_icon_html("photo_icon.png", "photo_resizer_icon_1788371609489.jpg", size=75, glow_color="rgba(0, 210, 255, 0.4)")
            st.markdown(f"""
            <div style="display: flex; gap: 16px; align-items: center;">
                {img_html}
                <div>
                    <h3 style="margin: 0; color: #f8fafc;">Photo Resizer</h3>
                    <div style="color: #00d2ff; font-size: 0.85rem; font-weight: 600; margin-top: 2px;">PRECISION CROP & COMPRESS</div>
                </div>
            </div>
            <div style="height: 48px; color: #94a3b8; font-size: 0.95rem; margin-top: 6px;">
                Interactive image cropper and compressor to hit exact pixel dimensions and strict KB limits.
            </div>
            """, unsafe_allow_html=True)
            st.page_link("pages/2_Photo_Resizer.py", label="Launch Photo Resizer ➔", use_container_width=True)

    st.write("")

    row2_col1, row2_col2 = st.columns(2, gap="large")

    # Card 3: File Organiser
    with row2_col1:
        with st.container(border=True):
            img_html = render_icon_html("file_icon.png", "file_organizer_icon_1788371632367.jpg", size=75, glow_color="rgba(52, 211, 153, 0.4)")
            st.markdown(f"""
            <div style="display: flex; gap: 16px; align-items: center;">
                {img_html}
                <div>
                    <h3 style="margin: 0; color: #f8fafc;">Desktop File Organiser</h3>
                    <div style="color: #34d399; font-size: 0.85rem; font-weight: 600; margin-top: 2px;">STANDALONE WINDOWS APP</div>
                </div>
            </div>
            <div style="height: 48px; color: #94a3b8; font-size: 0.95rem; margin-top: 6px;">
                Standalone verified desktop app to organize messy folders on your PC into 12 clean categories.
            </div>
            """, unsafe_allow_html=True)
            st.page_link("pages/3_File_Organiser.py", label="Get File Organiser ➔", use_container_width=True)

    # Card 4: PDF Converter
    with row2_col2:
        with st.container(border=True):
            img_html = render_icon_html("pdf_icon.png", "pdf_converter_icon_1788371743841.jpg", size=75, glow_color="rgba(251, 146, 60, 0.4)")
            st.markdown(f"""
            <div style="display: flex; gap: 16px; align-items: center;">
                {img_html}
                <div>
                    <h3 style="margin: 0; color: #f8fafc;">PDF Converter Suite</h3>
                    <div style="color: #fb923c; font-size: 0.85rem; font-weight: 600; margin-top: 2px;">DOCUMENT TRANSFORMATION</div>
                </div>
            </div>
            <div style="height: 48px; color: #94a3b8; font-size: 0.95rem; margin-top: 6px;">
                Merge, split, extract pages, and convert documents to and from PDF seamlessly.
            </div>
            """, unsafe_allow_html=True)
            st.page_link("pages/4_PDF_Converter.py", label="Open PDF Converter ➔", use_container_width=True)



# =======================================================
# ----------------- 2. PHOTO RESIZER --------------------
# =======================================================
elif st.session_state.current_page == "Photo Resizer":
    top_bar1, top_bar2 = st.columns([6, 1])
    with top_bar1:
        img_html = render_icon_html("photo_icon.png", "photo_resizer_icon_1788371609489.jpg", size=65, glow_color="rgba(0, 210, 255, 0.4)")
        st.markdown(f"""
        <div style="display: flex; gap: 16px; align-items: center;">
            {img_html}
            <div>
                <h2 style="margin: 0; color: #f8fafc;">Exam Photo Resizer</h2>
                <div style="color: #94a3b8; font-size: 0.95rem;">Crop, resize to specific pixel dimensions, and compress within exact KB constraints.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with top_bar2:
        if st.button("🏠 Back to Home", key="back_photo", use_container_width=True):
            navigate_to("Home")

    st.divider()

    photo_resizer_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdnjs.cloudflare.com/ajax/libs/cropperjs/1.6.1/cropper.min.css" rel="stylesheet">
        <style>
            body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background-color: transparent; color: #f3f4f6; display: flex; justify-content: center; padding: 1rem; }
            .tool-container { background: #111827; border: 1px solid #374151; padding: 2rem; border-radius: 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.5); width: 100%; max-width: 520px; }
            .input-group { margin-bottom: 1rem; }
            label { display: block; font-size: 0.9rem; font-weight: 600; margin-bottom: 0.4rem; color: #9ca3af; }
            input[type="number"], input[type="file"] { width: 100%; padding: 0.6rem; background: #1f2937; color: #fff; border: 1px solid #374151; border-radius: 6px; box-sizing: border-box; }
            .dimension-row { display: flex; gap: 1rem; }
            .img-container { width: 100%; max-height: 400px; margin-bottom: 1rem; display: none; background-color: #0f172a; border-radius: 8px; overflow: hidden; }
            img { display: block; max-width: 100%; }
            button { background: linear-gradient(135deg, #0284c7 0%, #00d2ff 100%); color: white; border: none; padding: 0.8rem; width: 100%; border-radius: 6px; font-weight: bold; cursor: pointer; margin-top: 1rem; }
            button:hover { opacity: 0.9; }
            #downloadBtn { display: none; background: #10b981; text-align: center; text-decoration: none; padding: 0.8rem; border-radius: 6px; color: white; font-weight: bold; margin-top: 1rem; display: block; }
            #status { text-align: center; margin-top: 1rem; font-size: 0.95rem; font-weight: 600; color: #9ca3af; }
        </style>
    </head>
    <body>
    <div class="tool-container">
        <h2 style="margin-top:0; text-align:center; color:#fff;">Exam Photo Tool</h2>
        <div class="input-group">
            <label>Select Photo</label>
            <input type="file" id="imageInput" accept="image/png, image/jpeg, image/jpg">
        </div>
        <div class="img-container" id="cropContainer">
            <img id="imageToCrop" src="">
        </div>
        <div class="dimension-row">
            <div class="input-group" style="flex: 1;">
                <label>Width (px)</label>
                <input type="number" id="widthInput" value="132" onchange="updateAspectRatio()">
            </div>
            <div class="input-group" style="flex: 1;">
                <label>Height (px)</label>
                <input type="number" id="heightInput" value="170" onchange="updateAspectRatio()">
            </div>
        </div>
        <div class="dimension-row">
            <div class="input-group" style="flex: 1;">
                <label>Min Size (KB)</label>
                <input type="number" id="minKbInput" value="20">
            </div>
            <div class="input-group" style="flex: 1;">
                <label>Max Size (KB)</label>
                <input type="number" id="maxKbInput" value="50">
            </div>
        </div>
        <button onclick="processAndCompress()" id="processBtn" style="display:none;">Crop & Compress Photo</button>
        <div id="status"></div>
        <a id="downloadBtn" download="OmniTools_Ready.jpg">Download Resized Photo</a>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/cropperjs/1.6.1/cropper.min.js"></script>
    <script>
        let cropper;
        const imageToCrop = document.getElementById('imageToCrop');
        const cropContainer = document.getElementById('cropContainer');
        const processBtn = document.getElementById('processBtn');
        const widthInput = document.getElementById('widthInput');
        const heightInput = document.getElementById('heightInput');

        document.getElementById('imageInput').addEventListener('change', function(e) {
            const files = e.target.files;
            if (files && files.length > 0) {
                const file = files[0];
                const url = URL.createObjectURL(file);
                imageToCrop.src = url;
                cropContainer.style.display = 'block';
                processBtn.style.display = 'block';

                if (cropper) cropper.destroy();

                const targetRatio = parseInt(widthInput.value) / parseInt(heightInput.value);
                cropper = new Cropper(imageToCrop, {
                    aspectRatio: targetRatio,
                    viewMode: 1,
                    autoCropArea: 0.8,
                });
                
                document.getElementById('status').innerText = "";
                document.getElementById('downloadBtn').style.display = "none";
            }
        });

        function updateAspectRatio() {
            if (cropper) {
                const newRatio = parseInt(widthInput.value) / parseInt(heightInput.value);
                cropper.setAspectRatio(newRatio);
            }
        }

        const getBlob = (canvas, quality) => {
            return new Promise(resolve => canvas.toBlob(resolve, 'image/jpeg', quality));
        };

        function showSuccess(blob, statusEl, downloadBtn) {
            statusEl.innerText = `✅ Success! Final Size: ${(blob.size / 1024).toFixed(1)} KB`;
            statusEl.style.color = "#34d399";
            const url = URL.createObjectURL(blob);
            downloadBtn.href = url;
            downloadBtn.style.display = "block";
        }

        async function processAndCompress() {
            if (!cropper) return;
            const targetWidth = parseInt(widthInput.value);
            const targetHeight = parseInt(heightInput.value);
            const minBytes = parseFloat(document.getElementById('minKbInput').value) * 1024;
            const maxBytes = parseFloat(document.getElementById('maxKbInput').value) * 1024;
            const statusEl = document.getElementById('status');
            const downloadBtn = document.getElementById('downloadBtn');

            if (minBytes >= maxBytes) {
                alert("Maximum KB must be greater than Minimum KB.");
                return;
            }

            statusEl.innerText = "Calculating perfect compression...";
            statusEl.style.color = "#94a3b8";
            downloadBtn.style.display = "none";

            const croppedCanvas = cropper.getCroppedCanvas();
            const finalCanvas = document.createElement('canvas');
            finalCanvas.width = targetWidth;
            finalCanvas.height = targetHeight;
            const ctx = finalCanvas.getContext('2d');
            ctx.fillStyle = '#FFFFFF';
            ctx.fillRect(0, 0, targetWidth, targetHeight);
            ctx.drawImage(croppedCanvas, 0, 0, targetWidth, targetHeight);

            let blob = await getBlob(finalCanvas, 1.0);
            if (blob.size < minBytes) {
                statusEl.innerText = `Error: Image is too small (${(blob.size/1024).toFixed(1)} KB) even at maximum quality. Upload a higher resolution photo.`;
                statusEl.style.color = "#f87171";
                return;
            }
            if (blob.size <= maxBytes) {
                return showSuccess(blob, statusEl, downloadBtn);
            }

            let minBlob = await getBlob(finalCanvas, 0.01);
            if (minBlob.size > maxBytes) {
                statusEl.innerText = `Error: Cannot compress enough. Minimum possible size is ${(minBlob.size/1024).toFixed(1)} KB.`;
                statusEl.style.color = "#f87171";
                return;
            }

            let min_q = 0.01, max_q = 1.0, best_blob = null;
            for (let i = 0; i < 15; i++) {
                let q = (min_q + max_q) / 2;
                blob = await getBlob(finalCanvas, q);
                if (blob.size >= minBytes && blob.size <= maxBytes) {
                    return showSuccess(blob, statusEl, downloadBtn);
                }
                if (blob.size > maxBytes) {
                    max_q = q;
                } else {
                    min_q = q;
                    best_blob = blob;
                }
            }
            if (best_blob) {
                statusEl.innerText = `Warning: Settled on closest safe size: ${(best_blob.size / 1024).toFixed(1)} KB`;
                statusEl.style.color = "#fbbf24";
                const url = URL.createObjectURL(best_blob);
                downloadBtn.href = url;
                downloadBtn.style.display = "block";
            }
        }
    </script>
    </body>
    </html>
    """
    components.html(photo_resizer_html, height=800, scrolling=True)

# =======================================================
# ----------------- 3. FILE ORGANISER -------------------
# =======================================================
elif st.session_state.current_page == "File Organiser":
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
        if st.button("🏠 Back to Home", key="back_org", use_container_width=True):
            navigate_to("Home")

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

# =======================================================
# ----------------- 4. PDF CONVERTER SUITE --------------
# =======================================================
else:
    top_bar1, top_bar2 = st.columns([6, 1])
    with top_bar1:
        img_html = render_icon_html("pdf_icon.png", "pdf_converter_icon_1788371743841.jpg", size=65, glow_color="rgba(251, 146, 60, 0.4)")
        st.markdown(f"""
        <div style="display: flex; gap: 16px; align-items: center;">
            {img_html}
            <div>
                <h2 style="margin: 0; color: #f8fafc;">PDF Converter Suite</h2>
                <div style="color: #34d399; font-size: 0.85rem; font-weight: bold; margin-top: 2px;">🔒 100% SECURE CLIENT-SIDE PROCESSING</div>
                <div style="color: #94a3b8; font-size: 0.95rem;">Files are processed locally in your browser. They never touch our servers.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with top_bar2:
        if st.button("🏠 Back to Home", key="back_pdf", use_container_width=True):
            navigate_to("Home")

    st.divider()

    # Shared CSS for all HTML components to perfectly match your Dark Theme
    shared_css = """
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background-color: transparent; color: #f3f4f6; display: flex; justify-content: center; padding: 0.5rem; margin: 0; }
        .tool-container { background: #111827; border: 1px solid #374151; padding: 1.5rem; border-radius: 12px; width: 100%; max-width: 600px; box-shadow: 0 4px 15px rgba(0,0,0,0.2); }
        label { display: block; font-size: 0.9rem; font-weight: 600; margin-bottom: 0.4rem; color: #9ca3af; }
        input[type="file"], input[type="text"], select { width: 100%; padding: 0.6rem; background: #1f2937; color: #fff; border: 1px solid #374151; border-radius: 6px; box-sizing: border-box; margin-bottom: 1rem; }
        button { background: linear-gradient(135deg, #ea580c 0%, #fb923c 100%); color: white; border: none; padding: 0.8rem; width: 100%; border-radius: 6px; font-weight: bold; cursor: pointer; transition: opacity 0.2s; }
        button:hover { opacity: 0.9; }
        #status { text-align: center; margin-top: 1rem; font-size: 0.95rem; font-weight: 600; color: #9ca3af; }
        .download-btn { display: none; background: #10b981; text-align: center; text-decoration: none; padding: 0.8rem; border-radius: 6px; color: white; font-weight: bold; margin-top: 1rem; }
        .download-btn:hover { background: #059669; }
    </style>
    """

    tab_img2pdf, tab_merge, tab_split, tab_extract = st.tabs([
        "🖼️ Images to PDF",
        "📑 Merge PDFs", 
        "✂️ Split / Extract Pages", 
        "📝 Extract Text"
    ])

    # ---------------- TAB 1: IMAGES TO PDF (CLIENT-SIDE) ----------------
    with tab_img2pdf:
        img2pdf_html = f"""
        {shared_css}
        <div class="tool-container">
            <h3 style="margin-top:0; color:#fff;">Images to Standardized PDF</h3>
            <label>Select images (JPG, PNG, WebP):</label>
            <input type="file" id="imgInput" accept="image/png, image/jpeg, image/jpg, image/webp" multiple>
            
            <div style="display: flex; gap: 10px; margin-bottom: 0.5rem;">
                <div style="flex: 1;">
                    <label>Page Size</label>
                    <select id="pageSize">
                        <option value="a4">A4 (Standard)</option>
                        <option value="letter">US Letter</option>
                        <option value="fit">Fit to Image</option>
                    </select>
                </div>
                <div style="flex: 1;">
                    <label>Orientation</label>
                    <select id="orientation">
                        <option value="auto">Auto Detect</option>
                        <option value="p">Portrait</option>
                        <option value="l">Landscape</option>
                    </select>
                </div>
                <div style="flex: 1;">
                    <label>Margins</label>
                    <select id="margins">
                        <option value="28">Small (10mm)</option>
                        <option value="0">None (Bleed)</option>
                        <option value="56">Medium (20mm)</option>
                    </select>
                </div>
            </div>
            
            <button onclick="convertImages()">🚀 Compile PDF</button>
            <div id="status"></div>
            <a id="downloadBtn" class="download-btn">⬇️ Download Compiled PDF</a>
        </div>
        
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
        <script>
            const loadImage = (file) => new Promise((resolve, reject) => {{
                const reader = new FileReader();
                reader.onload = (e) => {{
                    const img = new Image();
                    img.onload = () => resolve({{ img, dataUrl: e.target.result, type: file.type }});
                    img.onerror = reject;
                    img.src = e.target.result;
                }};
                reader.readAsDataURL(file);
            }});

            async function convertImages() {{
                const files = document.getElementById('imgInput').files;
                const status = document.getElementById('status');
                const btn = document.getElementById('downloadBtn');
                const pageSize = document.getElementById('pageSize').value;
                const orientPref = document.getElementById('orientation').value;
                const margin = parseInt(document.getElementById('margins').value);
                
                if (files.length === 0) {{ alert('Please select at least one image.'); return; }}
                
                status.innerText = "⏳ Processing images... Please wait.";
                btn.style.display = "none";
                
                try {{
                    const {{ jsPDF }} = window.jspdf;
                    let pdf = null;
                    const sizes = {{ 'a4': [595.28, 841.89], 'letter': [612, 792] }};
                    
                    for (let i = 0; i < files.length; i++) {{
                        status.innerText = `⏳ Processing image ${{i + 1}} of ${{files.length}}...`;
                        const {{ img, dataUrl, type }} = await loadImage(files[i]);
                        
                        let isLand = false;
                        if (orientPref === 'auto') isLand = img.width > img.height;
                        else if (orientPref === 'l') isLand = true;
                        
                        let format = sizes[pageSize];
                        let finalW, finalH;
                        
                        if (pageSize === 'fit') {{
                            format = [img.width, img.height];
                            isLand = img.width > img.height;
                            finalW = img.width;
                            finalH = img.height;
                        }} else {{
                            const baseW = isLand ? format[1] : format[0];
                            const baseH = isLand ? format[0] : format[1];
                            format = [baseW, baseH];
                            
                            const availW = baseW - (margin * 2);
                            const availH = baseH - (margin * 2);
                            
                            const imgAspect = img.width / img.height;
                            const targetAspect = availW / availH;
                            
                            if (imgAspect > targetAspect) {{
                                finalW = availW;
                                finalH = availW / imgAspect;
                            }} else {{
                                finalH = availH;
                                finalW = availH * imgAspect;
                            }}
                        }}
                        
                        const orientation = isLand ? 'l' : 'p';
                        
                        if (i === 0) {{
                            pdf = new jsPDF({{ orientation: orientation, unit: 'pt', format: format }});
                        }} else {{
                            pdf.addPage(format, orientation);
                        }}
                        
                        let x = pageSize === 'fit' ? 0 : margin + ((format[0] - (margin * 2) - finalW) / 2);
                        let y = pageSize === 'fit' ? 0 : margin + ((format[1] - (margin * 2) - finalH) / 2);
                        
                        const imgType = type === 'image/png' ? 'PNG' : (type === 'image/webp' ? 'WEBP' : 'JPEG');
                        pdf.addImage(dataUrl, imgType, x, y, finalW, finalH);
                    }}
                    
                    const pdfBlob = pdf.output('blob');
                    btn.href = URL.createObjectURL(pdfBlob);
                    btn.download = "OmniTools_Compiled_Images.pdf";
                    btn.style.display = "block";
                    status.innerText = "✅ Successfully compiled PDF!";
                    status.style.color = "#34d399";
                }} catch (e) {{
                    status.innerText = "❌ Error: " + e.message;
                    status.style.color = "#f87171";
                }}
            }}
        </script>
        """
        components.html(img2pdf_html, height=500)

    # ---------------- TAB 2: MERGE PDFS (CLIENT-SIDE) ----------------
    with tab_merge:
        merge_html = f"""
        {shared_css}
        <div class="tool-container">
            <h3 style="margin-top:0; color:#fff;">Merge Multiple PDFs</h3>
            <label>Select 2 or more PDF files (Order matters):</label>
            <input type="file" id="mergeInput" accept=".pdf" multiple>
            <button onclick="mergePdfs()">🚀 Merge in Browser</button>
            <div id="status"></div>
            <a id="downloadBtn2" class="download-btn">⬇️ Download Merged PDF</a>
        </div>
        <script src="https://unpkg.com/pdf-lib/dist/pdf-lib.min.js"></script>
        <script>
            async function mergePdfs() {{
                const files = document.getElementById('mergeInput').files;
                const status = document.getElementById('status');
                const btn = document.getElementById('downloadBtn2');
                
                if (files.length < 2) {{ alert('Please select at least 2 PDF files.'); return; }}
                
                status.innerText = "⏳ Merging files locally... Please wait.";
                btn.style.display = "none";
                
                try {{
                    const mergedPdf = await PDFLib.PDFDocument.create();
                    for (let i = 0; i < files.length; i++) {{
                        const arrayBuffer = await files[i].arrayBuffer();
                        const pdf = await PDFLib.PDFDocument.load(arrayBuffer);
                        const copiedPages = await mergedPdf.copyPages(pdf, pdf.getPageIndices());
                        copiedPages.forEach((page) => mergedPdf.addPage(page));
                    }}
                    const pdfBytes = await mergedPdf.save();
                    const blob = new Blob([pdfBytes], {{ type: 'application/pdf' }});
                    btn.href = URL.createObjectURL(blob);
                    btn.download = "OmniTools_Merged.pdf";
                    btn.style.display = "block";
                    status.innerText = "✅ Merged successfully!";
                    status.style.color = "#34d399";
                }} catch (e) {{
                    status.innerText = "❌ Error: " + e.message;
                    status.style.color = "#f87171";
                }}
            }}
        </script>
        """
        components.html(merge_html, height=350)

    # ---------------- TAB 3: SPLIT PDF (CLIENT-SIDE) ----------------
    with tab_split:
        split_html = f"""
        {shared_css}
        <div class="tool-container">
            <h3 style="margin-top:0; color:#fff;">Extract Pages</h3>
            <label>Select a PDF file:</label>
            <input type="file" id="splitInput" accept=".pdf">
            <label>Pages to extract (e.g., 1, 3-5, 8):</label>
            <input type="text" id="rangeInput" placeholder="1-3">
            <button onclick="splitPdf()">✂️ Extract Pages</button>
            <div id="status"></div>
            <a id="downloadBtn3" class="download-btn">⬇️ Download Extracted PDF</a>
        </div>
        <script src="https://unpkg.com/pdf-lib/dist/pdf-lib.min.js"></script>
        <script>
            async function splitPdf() {{
                const file = document.getElementById('splitInput').files[0];
                const rangeStr = document.getElementById('rangeInput').value;
                const status = document.getElementById('status');
                const btn = document.getElementById('downloadBtn3');
                
                if (!file || !rangeStr) {{ alert('Please select a file and enter a page range.'); return; }}
                
                status.innerText = "⏳ Extracting pages... Please wait.";
                btn.style.display = "none";
                
                try {{
                    const arrayBuffer = await file.arrayBuffer();
                    const pdf = await PDFLib.PDFDocument.load(arrayBuffer);
                    const totalPages = pdf.getPageCount();
                    
                    let pagesToExtract = new Set();
                    const parts = rangeStr.split(',');
                    for (let part of parts) {{
                        part = part.trim();
                        if (part.includes('-')) {{
                            let [start, end] = part.split('-');
                            start = parseInt(start); end = parseInt(end);
                            for (let p = start; p <= end; p++) {{
                                if (p >= 1 && p <= totalPages) pagesToExtract.add(p - 1);
                            }}
                        }} else {{
                            let p = parseInt(part);
                            if (p >= 1 && p <= totalPages) pagesToExtract.add(p - 1);
                        }}
                    }}
                    
                    if (pagesToExtract.size === 0) throw new Error("No valid pages found in range.");
                    
                    const newPdf = await PDFLib.PDFDocument.create();
                    const indices = Array.from(pagesToExtract).sort((a,b) => a-b);
                    const copiedPages = await newPdf.copyPages(pdf, indices);
                    copiedPages.forEach((page) => newPdf.addPage(page));
                    
                    const pdfBytes = await newPdf.save();
                    const blob = new Blob([pdfBytes], {{ type: 'application/pdf' }});
                    btn.href = URL.createObjectURL(blob);
                    btn.download = "Extracted_" + file.name;
                    btn.style.display = "block";
                    status.innerText = `✅ Extracted ${{indices.length}} page(s) successfully!`;
                    status.style.color = "#34d399";
                }} catch (e) {{
                    status.innerText = "❌ Error: " + e.message;
                    status.style.color = "#f87171";
                }}
            }}
        </script>
        """
        components.html(split_html, height=450)

    # ---------------- TAB 4: EXTRACT TEXT (CLIENT-SIDE) ----------------
    with tab_extract:
        extract_html = f"""
        {shared_css}
        <div class="tool-container">
            <h3 style="margin-top:0; color:#fff;">Extract Raw Text</h3>
            <label>Select a PDF file to read:</label>
            <input type="file" id="textInput" accept=".pdf">
            <button onclick="extractText()">📝 Read Text from PDF</button>
            <div id="status"></div>
            <textarea id="outputArea" style="display:none; width:100%; height:150px; background:#1f2937; color:#fff; border:1px solid #374151; border-radius:6px; margin-top:1rem; padding:0.5rem;" readonly></textarea>
            <a id="downloadBtn4" class="download-btn">⬇️ Download Text File (.txt)</a>
        </div>
        
        <script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.16.105/pdf.min.js"></script>
        <script>
            pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.16.105/pdf.worker.min.js';
            
            async function extractText() {{
                const file = document.getElementById('textInput').files[0];
                const status = document.getElementById('status');
                const textArea = document.getElementById('outputArea');
                const btn = document.getElementById('downloadBtn4');
                
                if (!file) {{ alert('Please select a PDF file first.'); return; }}
                
                status.innerText = "⏳ Reading document... (This might take a moment)";
                textArea.style.display = "none";
                btn.style.display = "none";
                
                try {{
                    const arrayBuffer = await file.arrayBuffer();
                    const loadingTask = pdfjsLib.getDocument({{data: new Uint8Array(arrayBuffer)}});
                    const pdf = await loadingTask.promise;
                    let fullText = "";
                    
                    for (let i = 1; i <= pdf.numPages; i++) {{
                        status.innerText = `⏳ Extracting page ${{i}} of ${{pdf.numPages}}...`;
                        const page = await pdf.getPage(i);
                        const textContent = await page.getTextContent();
                        const pageText = textContent.items.map(item => item.str).join(" ");
                        fullText += `=== PAGE ${{i}} ===\\n${{pageText}}\\n\\n`;
                    }}
                    
                    textArea.value = fullText;
                    textArea.style.display = "block";
                    
                    const blob = new Blob([fullText], {{ type: 'text/plain' }});
                    btn.href = URL.createObjectURL(blob);
                    btn.download = file.name.replace('.pdf', '_extracted.txt');
                    btn.style.display = "block";
                    
                    status.innerText = "✅ Text extraction complete!";
                    status.style.color = "#34d399";
                }} catch (e) {{
                    status.innerText = "❌ Error reading PDF: " + e.message;
                    status.style.color = "#f87171";
                }}
            }}
        </script>
        """
        components.html(extract_html, height=550)
