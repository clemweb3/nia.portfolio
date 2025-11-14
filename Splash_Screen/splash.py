# Splash Screen
import streamlit as st
import time

def run_splash():
    """Shows the splash screen only once per session."""
    
    loading_placeholder = st.empty()
    
    # ------------------------------
    # Elegant fonts + loading overlay
    # ------------------------------
    st.markdown("""
        <!-- Google Fonts -->
        <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;700&family=Raleway:wght@400;600&display=swap" rel="stylesheet">

        <style>
        html, body, [class*="css"] {
            font-family: 'Raleway', sans-serif !important;
            color: #3C2F2F;
            background-color: #FAF8F6;
        }

        /* IMPORTANT: Do NOT hide global header/footer menu anymore */
        /* This was breaking the sidebar */
        /* #MainMenu, header, footer {visibility: hidden;} */

        /* Instead, hide scroll + structure when overlay is active */
        body {
            overflow: hidden;
        }

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
            font-family: 'Playfair Display', serif !important;
        }

        /* Loading title */
        .loading-title {
            font-family: 'Playfair Display', serif !important;
            color: #5E4630 !important;
            font-size: 42px;
            font-weight: 600;
            margin-bottom: 30px;
            letter-spacing: 0.5px;
            text-align: center;
            overflow: hidden;
        }

        /* Dots */
        .loading-dots::after {
            content: '...';
            color: #5E4630 !important;
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
    # Remove overlay + restore scroll
    # ------------------------------
    loading_placeholder.empty()
    st.markdown("<style>body {overflow: auto !important;}</style>", unsafe_allow_html=True)
