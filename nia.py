import streamlit as st
import time

st.set_page_config(page_title="Nia Portfolio", layout="wide")

# Hide Streamlit header/footer
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Container for full-screen overlay
loading_container = st.empty()

with loading_container.container():
    # Fixed overlay with placeholder for the bar
    st.markdown("""
    <div style='
        position: fixed;
        top:0;
        left:0;
        width:100vw;
        height:100vh;
        background-color:#F5F5F0;
        display:flex;
        flex-direction:column;
        justify-content:center;
        align-items:center;
        z-index:9999;
    '>
        <h1 style='color:#8B5E3C; font-size:48px; margin-bottom:30px;'>Generating dashboards...</h1>
        <div style='width:400px; height:25px; background-color:#DDD; border-radius:12px; overflow:hidden;'>
            <div id='progress-bar' style='width:0%; height:100%; background-color:#A97458; transition: width 0.05s;'></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Use a single st.empty() to animate the inner bar
    bar = st.empty()
    for percent in range(101):
        bar.markdown(f"""
        <div style='width:400px; height:25px; background-color:#DDD; border-radius:12px; overflow:hidden;'>
            <div style='width:{percent}%; height:100%; background-color:#A97458; transition: width 0.05s;'></div>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(0.03)

# Remove the overlay
loading_container.empty()

# Main content
st.success(" Welcome to my Data Science Portfolio!")
st.write("Here goes your portfolio content…")
