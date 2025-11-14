# app.py
import streamlit as st
from Splash_Screen.splash import run_splash  # make sure folder is Splash_Screen

# ------------------------------
# Set page configuration FIRST
# ------------------------------
st.set_page_config(page_title="Nia Portfolio", layout="wide")

# ------------------------------
# Run splash screen only once per session
# ------------------------------
if 'loaded' not in st.session_state:
    st.session_state.loaded = True
    run_splash()

# ------------------------------
# Main portfolio content
# ------------------------------
st.markdown("""
<div style="text-align:center; margin-top:50px;">
    <h1 style="font-family:'Playfair Display', serif; font-size:46px; color:#4B3B30; font-weight:700;">
        Welcome to My Data Science Portfolio
    </h1>
    <p style="font-family:'Raleway', sans-serif; font-size:18px; color:#5A4B42; max-width:700px; margin:20px auto; line-height:1.6;">
        Explore interactive dashboards, projects, and analytics crafted with precision and powered by Python and Streamlit.
    </p>
</div>
""", unsafe_allow_html=True)
s