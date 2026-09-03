# =======================================================
# ----------------- 2. PHOTO RESIZER --------------------
# =======================================================
import streamlit as st
import streamlit.components.v1 as components
from utils import render_icon_html
# --- SEO METADATA ---
st.set_page_config(
    page_title="SSC & Railway Exam Photo Resizer (20KB - 50KB) | OmniTools",
    page_icon="📸",
    layout="wide"
)

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
  st.page_link("omnitools_app.py", label="🏠 Back", use_container_width=True)

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

