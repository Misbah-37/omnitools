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

# card 5: QR Generator

with row3_col1:
    with st.container(border=True):
        st.markdown("### 📱 QR Code Generator")
        st.write("Create, customize, and securely download high-quality QR codes from any URL or text.")
        st.page_link("pages/5_QR_Generator.py", label="Launch Tool", use_container_width=True)
