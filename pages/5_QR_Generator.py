import streamlit as st
import qrcode
from io import BytesIO

st.set_page_config(page_title="QR Code Generator | OmniTools", page_icon="qr_icon.png", layout="wide")

top_bar1, top_bar2 = st.columns([6, 1])
with top_bar1:
    st.markdown("##  QR Code Generator\nGenerate and download custom QR codes instantly.")
with top_bar2:
    st.page_link("omnitools_app.py", label="🏠 Back", use_container_width=True)
st.divider()

col1, col2 = st.columns([1.2, 1])
with col1:
    qr_data = st.text_area("URL or Text to encode:", placeholder="https://example.com")
    c1, c2 = st.columns(2)
    with c1: 
        fill_color = st.color_picker("QR Color", "#000000")
    with c2: 
        back_color = st.color_picker("Background", "#FFFFFF")

with col2:
    if qr_data:
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(qr_data)
        qr.make(fit=True)
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        buf = BytesIO()
        img.save(buf, format="PNG")
        st.image(buf.getvalue(), width=250)
        st.download_button("⬇️ Download (PNG)", buf.getvalue(), "qr.png", "image/png", use_container_width=True)
    else:
        st.info("Enter a URL or text on the left to generate your QR code.")
