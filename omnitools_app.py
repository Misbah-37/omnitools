import streamlit as st

# 1. Core Config
st.set_page_config(
    page_title="OmniTools | Backend Engine", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Universal Sidebar & Header Erasure
st.markdown("""
<style>
    /* Completely kill the Streamlit sidebar and top header */
    [data-testid="stSidebar"] { display: none !important; }
    section[data-testid="stSidebar"] { display: none !important; }
    button[kind="header"] { display: none !important; }
    header { display: none !important; }
</style>
""", unsafe_allow_html=True)

# 3. Silent Placeholder
st.markdown(
    "<h3 style='text-align: center; color: #94a3b8; margin-top: 50px;'>⚙️ OmniTools Backend Engine Online</h3>", 
    unsafe_allow_html=True
)
