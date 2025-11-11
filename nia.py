import streamlit as st
import time

st.set_page_config(page_title="Nia Portfolio", layout="wide")

# Inject global style and animation
st.markdown("""
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">

    <style>
    /* Override Streamlit’s default font */
    html, body, [class*="css"]  {
        font-family: 'Poppins', sans-serif !important;
        color: #2B2B2B;
    }

    #MainMenu, header, footer {visibility: hidden;}

    /* Overlay styling */
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
    }

    /* Loading title */
    .loading-title {
        color: #5A3825;
        font-size: 42px;
        font-weight: 600;
        margin-bottom: 30px;
        letter-spacing: 0.5px;
    }

    /* Animated dots */
    .loading-dots::after {
        content: '';
        animation: dots 1.2s steps(4, end) infinite;
    }

    @keyframes dots {
        0% { content: ''; }
        25% { content: '.'; }
        50% { content: '..'; }
        75% { content: '...'; }
        100% { content: ''; }
    }

    /* Progress container + bar */
    .progress-container {
        width: 400px;
        height: 20px;
        background-color: #E0DAD2;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: inset 0 0 3px rgba(0,0,0,0.1);
    }

    .progress-bar {
        width: 0%;
        height: 100%;
        background: linear-gradient(90deg, #A97458, #8B5E3C);
        animation: loadProgress 3s ease-in-out forwards;
        border-radius: 12px;
    }

    @keyframes loadProgress {
        from { width: 0%; }
        to { width: 100%; }
    }
    </style>
""", unsafe_allow_html=True)

# Show overlay
loading_placeholder = st.empty()

with loading_placeholder.container():
    st.markdown("""
    <div class="overlay">
        <h1 class="loading-title">
            Generating dashboards<span class="loading-dots"></span>
        </h1>
        <div class="progress-container">
            <div class="progress-bar"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Let CSS animation play for 3s
time.sleep(3.2)

# Remove overlay
loading_placeholder.empty()

# Main content
st.markdown("""
<div class="w3-animate-opacity" style="text-align:center; margin-top:80px;">
    <h1 style="font-weight:600; font-size:40px; color:#3C2A21;">Welcome to My Data Science Portfolio</h1>
    <p style="font-size:18px; color:#555;">Explore interactive dashboards, projects, and analytics powered by Python and Streamlit.</p>
</div>
""", unsafe_allow_html=True)
