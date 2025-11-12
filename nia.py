import streamlit as st
import time

st.set_page_config(page_title="Nia Portfolio", layout="wide")

# ------------------------------
# Elegant fonts + loading overlay
# ------------------------------
st.markdown("""
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;700&family=Raleway:wght@400;600&display=swap" rel="stylesheet">

    <style>
    /* GLOBAL STYLES */
    html, body, [class*="css"] {
        font-family: 'Raleway', sans-serif !important;
        color: #3C2F2F;
        background-color: #FAF8F6;
    }

    #MainMenu, header, footer {visibility: hidden;}

    /* OVERLAY STYLES */
    .overlay {
        position: fixed;
        top: 0; left: 0;
        width: 100vw; height: 100vh;
        background-color: #F7F5F2;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        z-index: 9999;
        font-family: 'Playfair Display', serif !important; /* <- ensures all overlay text uses Playfair Display */
    }

    /* Loading titles */
    .loading-title, .loading-title span {
        font-family: 'Playfair Display', serif !important;  /* <- override Streamlit fonts */
        color: #5E4630;
        font-size: 42px;
        font-weight: 600;
        margin-bottom: 30px;
        letter-spacing: 0.5px;
        text-align: center;
    }

    /* Animated dots */
    .loading-dots::after {
        content: '';
        display: inline-block;
        width: 1em;
        text-align: left;
        animation: dots 1.2s steps(4, end) infinite;
        font-family: 'Playfair Display', serif !important; /* <- ensure dots inherit correct font */
    }

    @keyframes dots {
        0% { content: ''; }
        25% { content: '.'; }
        50% { content: '..'; }
        75% { content: '...'; }
        100% { content: ''; }
    }

    /* Progress bar */
    .progress-container {
        width: 400px;
        height: 20px;
        background-color: #E7DFD8;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: inset 0 0 4px rgba(0,0,0,0.1);
    }

    .progress-bar {
        width: 0%;
        height: 100%;
        background: linear-gradient(90deg, #C8A27E, #A67C52);
        animation: loadProgress 3s ease-in-out forwards;
        border-radius: 12px;
    }

    @keyframes loadProgress {
        from { width: 0%; }
        to { width: 100%; }
    }
    </style>
""", unsafe_allow_html=True)

# ------------------------------
# Phase 1: Generating dashboards
# ------------------------------
loading_placeholder = st.empty()
with loading_placeholder.container():
    st.markdown("""
    <div class="overlay">
        <h1 class="loading-title">Generating dashboards<span class="loading-dots"></span></h1>
        <div class="progress-container">
            <div class="progress-bar"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
time.sleep(3)

# ------------------------------
# Phase 2: Providing insights
# ------------------------------
loading_placeholder.empty()
with loading_placeholder.container():
    st.markdown("""
    <div class="overlay">
        <h1 class="loading-title">Providing insights<span class="loading-dots"></span></h1>
        <div class="progress-container">
            <div class="progress-bar"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
time.sleep(2.5)

# ------------------------------
# Remove overlay → show main page
# ------------------------------
loading_placeholder.empty()

# ------------------------------
# MAIN PAGE CONTENT
# ------------------------------
st.markdown("""
<div class="w3-animate-opacity" style="text-align:center; margin-top:80px;">
    <h1 style="font-family:'Playfair Display',serif; font-size:46px; color:#4B3B30; font-weight:700;">
        Welcome to My Data Science Portfolio
    </h1>
    <p style="font-family:'Raleway',sans-serif; font-size:18px; color:#5A4B42; max-width:700px; margin:20px auto; line-height:1.6;">
        Explore interactive dashboards, projects, and analytics crafted with precision and powered by Python and Streamlit.
    </p>
</div>
""", unsafe_allow_html=True)
