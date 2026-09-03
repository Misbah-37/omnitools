import os
import base64

def find_image(png_name, jpg_name):
    if os.path.exists(png_name):
        return png_name
    if os.path.exists(jpg_name):
        return jpg_name
    return None

def render_icon_html(png_name, jpg_name, size=75, glow_color="rgba(0, 210, 255, 0.4)"):
    path = find_image(png_name, jpg_name)
    if path:
        with open(path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
            mime = "image/png" if path.endswith(".png") else "image/jpeg"
            return f"<img src='data:{mime};base64,{b64}' style='width:{size}px; height:{size}px; filter: drop-shadow(0 8px 16px {glow_color}); margin-bottom: 8px; object-fit: contain;' />"
    return ""
