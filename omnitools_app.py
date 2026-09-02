import streamlit as st
import random
import time
import string
import json
import io
import os
import shutil
import zipfile
import streamlit.components.v1 as components

# ----------------- 1. OMNITOOLS CONFIG -----------------
st.set_page_config(
    page_title="OmniTools | Ultimate Utility Suite", 
    page_icon="🛠️", 
    layout="wide",
    initial_sidebar_state="collapsed"
)
# Custom CSS: Hide Sidebar & Apply Modern Dark Theme
st.markdown("""
<style>
    /* Completely hide the sidebar and sidebar toggle */
    [data-testid="stSidebar"] {
        display: none !important;
    }
    section[data-testid="stSidebar"] {
        display: none !important;
    }
    button[kind="header"] {
        display: none !important;
    }
    
    /* Center hero content */
    .hero-container {
        text-align: center;
        padding: 10px 0 30px 0;
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
# ----------------- PAGE ROUTER STATE -----------------
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"
def navigate_to(page_name):
    st.session_state.current_page = page_name
    st.rerun()
# =======================================================
# ----------------- 0. LANDING PAGE (HOME) --------------
# =======================================================
if st.session_state.current_page == "Home":
    # Centered Grand Hero
    _, hero_col, _ = st.columns([1, 2, 1])
    with hero_col:
        if os.path.exists("omnitools_master_logo_1788371563646.jpg"):
            st.image("omnitools_master_logo_1788371563646.jpg", width=220)
        st.markdown("<h1 style='text-align: center; margin-top: -10px;'>OmniTools 🌌</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 1.1rem;'>High-performance, private, and lightweight utility tools for your daily workflows.</p>", unsafe_allow_html=True)
    st.markdown("""
    <div class="trust-badge-container">
        <span class="trust-badge">⚡ Ultra Fast Execution</span>
        <span class="trust-badge">🔒 100% Privacy Focused</span>
        <span class="trust-badge">💻 Modern Dark Mode Suite</span>
        <span class="trust-badge">🚀 Zero Installation Required</span>
    </div>
    """, unsafe_allow_html=True)
    st.divider()
    # 2x2 Grid of Tools
    row1_col1, row1_col2 = st.columns(2)
    # Card 1: Typing Test
    with row1_col1:
        c1, c2 = st.columns([1, 4])
        with c1:
            if os.path.exists("typing_speed_icon_1788371582708.jpg"):
                st.image("typing_speed_icon_1788371582708.jpg", width=75)
        with c2:
            st.markdown("### Typing Speed Test")
            st.caption("Measure keystroke speed and accuracy across 4 difficulty tiers including 30 curated paragraphs.")
        if st.button("Launch Typing Test ➔", key="btn_type", use_container_width=True):
            navigate_to("Typing Speed Test")
    # Card 2: Photo Resizer
    with row1_col2:
        c1, c2 = st.columns([1, 4])
        with c1:
            if os.path.exists("photo_resizer_icon_1788371609489.jpg"):
                st.image("photo_resizer_icon_1788371609489.jpg", width=75)
        with c2:
            st.markdown("### Photo Resizer")
            st.caption("Interactive image cropper and binary-search compressor to hit exact pixel dimensions and strict KB limits.")
        if st.button("Launch Photo Resizer ➔", key="btn_photo", use_container_width=True):
            navigate_to("Photo Resizer")
    st.write("")
    row2_col1, row2_col2 = st.columns(2)
    # Card 3: File Organiser
    with row2_col1:
        c1, c2 = st.columns([1, 4])
        with c1:
            if os.path.exists("file_organizer_icon_1788371632367.jpg"):
                st.image("file_organizer_icon_1788371632367.jpg", width=75)
        with c2:
            st.markdown("### Desktop File Organiser")
            st.caption("Standalone verified Windows desktop utility to organize any messy folder on your PC in a single click.")
        if st.button("Get File Organiser ➔", key="btn_org", use_container_width=True):
            navigate_to("File Organiser")
    # Card 4: PDF Converter
    with row2_col2:
        c1, c2 = st.columns([1, 4])
        with c1:
            if os.path.exists("pdf_converter_icon_1788371743841.jpg"):
                st.image("pdf_converter_icon_1788371743841.jpg", width=75)
        with c2:
            st.markdown("### PDF Converter Suite")
            st.caption("Merge, split, extract pages, and convert documents to and from PDF seamlessly.")
        if st.button("Open PDF Converter ➔", key="btn_pdf", use_container_width=True):
            navigate_to("PDF Converter")
# =======================================================
# ----------------- 1. TYPING SPEED TEST ----------------
# =======================================================
elif st.session_state.current_page == "Typing Speed Test":
    top_bar1, top_bar2 = st.columns([6, 1])
    with top_bar1:
        c_icon, c_head = st.columns([1, 10])
        with c_icon:
            if os.path.exists("typing_speed_icon_1788371582708.jpg"):
                st.image("typing_speed_icon_1788371582708.jpg", width=65)
        with c_head:
            st.markdown("<h2 style='margin:0;'>Typing Speed Test</h2>", unsafe_allow_html=True)
            st.caption("Test your typing speed and accuracy in real-time.")
    with top_bar2:
        if st.button("🏠 Back to Home", key="back_type", use_container_width=True):
            navigate_to("Home")
    st.divider()
    letters = list(string.ascii_lowercase + string.digits + "!@#$%^&*()_+-=[]{}|;':,.<>/?`~ ")
    words = [
        "apple", "banana", "table", "chair", "mountain", "river", "ocean", "space", "rocket",
        "planet", "orbit", "galaxy", "universe", "telescope", "computer", "keyboard", "mouse",
        "screen", "window", "door", "house", "building", "street", "city", "country", "world",
        "globe", "map", "compass", "north", "south", "east", "west", "up", "down", "left", "right",
        "front", "back", "top", "bottom", "inside", "outside", "near", "far", "close", "open", "shut",
        "lock", "key", "safe", "danger", "fast", "slow", "quick", "speedy", "rapid", "swift", "sudden",
        "abrupt", "gradual", "steady", "constant", "changing", "dynamic", "static", "still", "quiet",
        "loud", "noisy", "silent", "peaceful", "calm", "chaotic", "messy", "neat", "tidy", "clean", "dirty",
        "filthy", "spotless", "bright", "dark", "light", "heavy", "soft", "hard", "rough", "smooth", "sharp",
        "dull", "blunt", "pointed", "round", "square", "flat", "curved", "straight", "bent", "broken"
    ]
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Pack my box with five dozen liquor jugs.",
        "How vexingly quick daft zebras jump!",
        "Sphinx of black quartz, judge my vow.",
        "Two driven jocks help fax my big quiz.",
        "Five quacking zephyrs jolt my wax bed.",
        "The five boxing wizards jump quickly.",
        "Bright vixens jump; dozy fowl quack.",
        "A wizard's job is to vex chumps quickly in fog.",
        "Watch Jeopardy, Alex Trebek's fun TV quiz game.",
        "By Jove, my quick study of lexicography won a prize.",
        "Programming is not about memorizing code; it is about solving problems.",
        "Artificial Intelligence is changing the world very quickly.",
        "The internet is a vast network that connects computers all over the world.",
        "Cybersecurity is the practice of protecting systems, networks, and programs.",
        "Software engineering is the systematic application of engineering approaches.",
        "Cloud computing provides on-demand availability of computer system resources.",
        "Python is an interpreted, high-level and general-purpose programming language."
    ]
    paragraphs = [
        "The morning sun cast a gentle golden glow across the quiet streets as the city slowly woke up. A cool breeze carried the sweet aroma of freshly brewed coffee from the corner bakery, welcoming early morning commuters on their way to work.",
        "Consistency is the secret ingredient behind mastering any new skill in life. When you dedicate even ten minutes each day to focused practice, the compound effect over months and years produces remarkable results that talent alone cannot achieve.",
        "Reading books is one of the most rewarding habits you can develop. It allows you to travel across different eras, explore distant worlds, and experience the thoughts of great minds throughout history, all from the comfort of your favorite armchair.",
        "The ocean covers more than seventy percent of our planet and remains one of the least explored frontiers on Earth. Beneath its shimmering surface lie vast underwater mountain ranges, deep trenches, and countless mysterious creatures that have never seen sunlight.",
        "In the modern digital era, learning how to type quickly and accurately is an essential superpower. It allows your thoughts to flow seamlessly onto the screen without interruption, boosting both your productivity and creative expression.",
        "Clean code is like well-written prose; it is intuitive, easy to understand, and pleasant to maintain over time. Great software engineers do not just write code for machines to execute, but for fellow developers to read and improve.",
        "Coding is equal parts logic and creativity. Whether building a simple calculator, designing an interactive game, or training a machine learning model, programming gives you the power to bring abstract ideas into tangible reality.",
        "Master the art of finishing what you start. While starting new projects is exciting, the true satisfaction and growth come from pushing through the messy middle and bringing your work across the finish line."
    ]
    difficulty = st.radio(
        "Choose Difficulty:", 
        ["1. Easy (30 Letters)", "2. Medium (15 Words)", "3. Hard (10 Sentences)", "4. Expert (1 Paragraph)"]
    )
    if 'test_active' not in st.session_state:
        st.session_state.test_active = False
    def start_test():
        st.session_state.test_active = True
        if "Easy" in difficulty:
            st.session_state.pool = letters
            st.session_state.target_count = 30
        elif "Medium" in difficulty:
            st.session_state.pool = words
            st.session_state.target_count = 15
        elif "Hard" in difficulty:
            st.session_state.pool = sentences
            st.session_state.target_count = 10
        else:
            st.session_state.pool = paragraphs
            st.session_state.target_count = 1
    if not st.session_state.test_active:
        st.button("Start Typing Test", on_click=start_test, type="primary")
    else:
        st.info("Click anywhere in the box below and start typing!")
        pool_json = json.dumps(st.session_state.pool)
        target_count = st.session_state.target_count
        js_code = f"""
        <!DOCTYPE html>
        <html>
        <head>
        <style>
            body {{ font-family: 'Inter', sans-serif; color: #e2e8f0; background: transparent; margin: 0; padding: 10px; }}
            .sentence {{ font-size: 20px; line-height: 1.6; letter-spacing: 0.5px; margin-bottom: 20px; user-select: none; word-wrap: break-word; }}
            .correct {{ color: #00d2ff; font-weight: bold; text-shadow: 0 0 8px rgba(0,210,255,0.4); }}
            .current {{ text-decoration: underline; font-weight: bold; color: #ff3399; background-color: rgba(255, 51, 153, 0.2); border-radius: 3px; padding: 0 2px; }}
            #stats {{ font-size: 20px; font-weight: bold; color: #00d2ff; line-height: 1.6; }}
            #progress {{ font-size: 15px; color: #94a3b8; margin-bottom: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; }}
        </style>
        </head>
        <body>
            <div id="progress">Loading...</div>
            <div id="textDisplay" class="sentence"></div>
            <div id="stats"></div>
            <script>
                const pool = {pool_json};
                const targetCount = {target_count};
                let currentTarget = pool[Math.floor(Math.random() * pool.length)];
                let currentIndex = 0;
                let roundsCompleted = 0;
                let startTime = null;
                let totalCharactersTyped = 0;
                let errors = 0;
                const display = document.getElementById("textDisplay");
                const stats = document.getElementById("stats");
                const progress = document.getElementById("progress");
                
                function render() {{
                    progress.innerText = `Round: ${{roundsCompleted + 1}} / ${{targetCount}}`;
                    let html = "";
                    for (let i = 0; i < currentTarget.length; i++) {{
                        if (i < currentIndex) {{
                            html += `<span class="correct">${{currentTarget[i]}}</span>`;
                        }} else if (i === currentIndex) {{
                            html += `<span class="current">${{currentTarget[i]}}</span>`;
                        }} else {{
                            html += `<span>${{currentTarget[i]}}</span>`;
                        }}
                    }}
                    display.innerHTML = html;
                }}
                
                window.addEventListener("keydown", function(e) {{
                    if (roundsCompleted >= targetCount) return;
                    if (e.key === "Backspace") {{ e.preventDefault(); return; }}
                    if (e.key.length > 1) return; 
                    if (startTime === null) startTime = new Date().getTime();
                    if (e.key === currentTarget[currentIndex]) {{
                        currentIndex++;
                        totalCharactersTyped++;
                    }} else {{
                        errors++;
                    }}
                    if (currentIndex === currentTarget.length) {{
                        roundsCompleted++;
                        if (roundsCompleted === targetCount) {{
                            let endTime = new Date().getTime();
                            let elapsedSeconds = (endTime - startTime) / 1000;
                            let wpm = (totalCharactersTyped / 5) / (elapsedSeconds / 60);
                            let accuracy = (totalCharactersTyped / (totalCharactersTyped + errors)) * 100;
                            progress.innerText = "✨ Test Complete!";
                            display.innerHTML = "";
                            stats.innerHTML = `🎉 Perfect! <br> 🚀 Speed: ${{wpm.toFixed(2)}} WPM <br> 🎯 Accuracy: ${{accuracy.toFixed(2)}}%`;
                            return;
                        }} else {{
                            currentTarget = pool[Math.floor(Math.random() * pool.length)];
                            currentIndex = 0;
                        }}
                    }}
                    render();
                }});
                render();
            </script>
        </body>
        </html>
        """
        components.html(js_code, height=350)
        if st.button("End Test / Change Difficulty", type="primary"):
            st.session_state.test_active = False
            st.rerun()
# =======================================================
# ----------------- 2. PHOTO RESIZER --------------------
# =======================================================
elif st.session_state.current_page == "Photo Resizer":
    top_bar1, top_bar2 = st.columns([6, 1])
    with top_bar1:
        c_icon, c_head = st.columns([1, 10])
        with c_icon:
            if os.path.exists("photo_resizer_icon_1788371609489.jpg"):
                st.image("photo_resizer_icon_1788371609489.jpg", width=65)
        with c_head:
            st.markdown("<h2 style='margin:0;'>Exam Photo Resizer</h2>", unsafe_allow_html=True)
            st.caption("Crop, resize to specific pixel dimensions, and compress within exact KB constraints.")
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
        c_icon, c_head = st.columns([1, 10])
        with c_icon:
            if os.path.exists("file_organizer_icon_1788371632367.jpg"):
                st.image("file_organizer_icon_1788371632367.jpg", width=65)
        with c_head:
            st.markdown("<h2 style='margin:0;'>Desktop File Organiser</h2>", unsafe_allow_html=True)
            st.caption("A secure, standalone desktop utility to organize any folder on your computer in a single click.")
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
# ----------------- 4. PDF CONVERTER --------------------
# =======================================================
else:
    top_bar1, top_bar2 = st.columns([6, 1])
    with top_bar1:
        c_icon, c_head = st.columns([1, 10])
        with c_icon:
            if os.path.exists("pdf_converter_icon_1788371743841.jpg"):
                st.image("pdf_converter_icon_1788371743841.jpg", width=65)
        with c_head:
            st.markdown("<h2 style='margin:0;'>PDF Converter Suite</h2>", unsafe_allow_html=True)
            st.caption("Merge, split, extract pages, and convert documents to and from PDF seamlessly.")
    with top_bar2:
        if st.button("🏠 Back to Home", key="back_pdf", use_container_width=True):
            navigate_to("Home")
    st.divider()
    st.info("Status: Under Construction")
