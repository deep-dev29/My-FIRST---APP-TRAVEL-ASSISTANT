import streamlit as st 
from google import genai
from dotenv import load_dotenv
import time
load_dotenv()
client = genai.Client()

st.set_page_config(page_title="  Travel Assistant", page_icon="✈️", layout="wide")

# Advanced Animated & Glowing Header HTML/CSS
st.markdown("""
<style>
    /* Continuous Gradient Movement Keyframes */
    @keyframes gradient-flow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Soft Breathing Glow Effect for Border */
    @keyframes pulse-glow {
        0% { box-shadow: 0 0 15px rgba(0, 242, 254, 0.3); }
        50% { box-shadow: 0 0 30px rgba(0, 242, 254, 0.7); }
        100% { box-shadow: 0 0 15px rgba(0, 242, 254, 0.3); }
    }

    /* Live Animated Heading */
    .live-glow-title {
        font-size: 3.8rem !important;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(270deg, #00f2fe, #4facfe, #00c6ff, #00f2fe);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradient-flow 6s ease infinite;
        letter-spacing: 2px;
        margin-bottom: 0px;
        filter: drop-shadow(0 0 12px rgba(0, 242, 254, 0.6));
    }

    /* Subtitle Tagline */
    .live-glow-subtitle {
        text-align: center;
        font-size: 1.15rem;
        color: #FF0055;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin-top: -5px;
        margin-bottom: 25px;
        font-weight: 500;
    }

    /* Glowing Feature Box */
    .animated-glow-box {
        background: rgba(15, 23, 42, 0.8);
        border: 1px solid rgba(0, 242, 254, 0.5);
        border-radius: 16px;
        padding: 16px 20px;
        text-align: center;
        color: #9D4EDD;
        font-weight: 600;
        animation: pulse-glow 3s infinite ease-in-out;
        max-width: 800px;
        margin: 0 auto 30px auto;
        backdrop-filter: blur(10px);
    }

    .badge-item {
        display: inline-block;
        margin: 0 12px;
        color:#00F2FE;
    }
</style>

<!-- Header Markup -->
<h1 class="live-glow-title">✈️  TRAVEL ASSISTANT</h1>
<div class="live-glow-subtitle">✦ Smart • Seamless • Live Travel Assistant ✦</div>

<div class="animated-glow-box">
    <span class="badge-item">🗺️ AI Itinerary Engine</span> • 
    <span class="badge-item">🏨 Smart Stays</span> • 
    <span class="badge-item">⚡ Real-Time Flight Insights</span>
</div>
""", unsafe_allow_html=True)
# Custom CSS & HTML Prompt Card
st.markdown("""
<style>
    .prompt-container {
        background: rgba(15, 23, 42, 0.75);
        border: 1px solid rgba(56, 189, 248, 0.4);
        border-radius: 16px;
        padding: 24px;
        margin: 20px 0;
        box-shadow: 0 10px 30px rgba(0, 242, 254, 0.15);
        backdrop-filter: blur(12px);
    }
    
    .prompt-title {
        font-size: 1.6rem;
        font-weight: 800;
        background: linear-gradient(90deg, #38bdf8, #818cf8, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 6px;
    }

    .prompt-subtitle {
        color: #94a3b8;
        font-size: 0.95rem;
        margin-bottom: 18px;
    }
</style>

<div class="prompt-container">
    <div class="prompt-title">🌍 Where is your next adventure heading?</div>
    <div class="prompt-subtitle">Type any city, island, or dream spot below to unlock your custom trip.</div>
</div>
""", unsafe_allow_html=True)

# Aapka Input Code
destination = st.text_input(
    label="Destination Search",
    placeholder="e.g. Kyoto, Amalfi Coast, Switzerland, Bali...",
    label_visibility="collapsed"
)

# Custom Styling for Trip Options
st.markdown("""
<style>
    .section-title {
        color: #38bdf8;
        font-size: 1.2rem;
        font-weight: 700;
        margin-top: 25px;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# --- Trip Preferences Section ---
st.markdown('<div class="section-title">⚙️ Customize Your Trip Details</div>', unsafe_allow_html=True)

# 2 Columns Layout for Input Controls
col1, col2 = st.columns(2)

with col1:
    # 1. Trip Duration Slider
    days = st.slider(
        "🗓️ Trip Duration (Days):",
        min_value=1,
        max_value=30,
        value=5,
        help="Select the total number of days for your trip."
    )

with col2:
    # 2. Budget Category Selector
    budget = st.selectbox(
        "💰 Travel Budget Category:",
        options=[
            "🎒 Backpacker / Economy (Budget-Friendly)",
            "⚖️ Balanced / Standard (Mid-Range)",
            "💎 Luxury / Premium (Five-Star Experience)"
        ],
        index=1,
        help="Choose your preferred spending style."
    )
st.markdown("""
<style>
    .section-title {
        color: #38bdf8;
        font-size: 1.2rem;
        font-weight: 700;
        margin-top: 25px;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Section Title
st.markdown('<div class="section-title">👥 Who is traveling with you?</div>', unsafe_allow_html=True)

# Travel Companion Selection (Horizontal Buttons)
travel_group = st.radio(
    label="Select your travel squad:",
    options=[
        "🎒 Solo ",
        "👨‍👩‍👧‍👦 Family ",
        "🎉 Friends ",
        "👩‍❤️‍👨 Couple "
    ],
    index=1,
    horizontal=True,
    label_visibility="collapsed"
)
prompt =f""" You are a travel planner, user is saying he/she wants  to go to {destination}for {days},he is  on budget of type {budget}. Travel type is  {travel_group} .plan a tripo and share answer in bullets"""
st.markdown("""

""", unsafe_allow_html=True)

# Button Logic & Action
if st.button("🚀 Plan My Trip"):
    if 'destination' in locals() and not destination.strip():
        st.warning("⚠️ Pehle destination ka naam likhein!")
    else:
        interaction = client.interactions.create(
                model="gemini-3.5-flash-lite",
                input=destination)
        with st.spinner("✨ AI aapka travel plan ready kar raha hai...", show_time=True):
            time.sleep(2)
            st.balloons()
            st.success("🎉 Trip Plan Ready!")
            st.write(interaction.output_text)
