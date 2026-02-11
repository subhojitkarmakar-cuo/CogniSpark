import streamlit as st
import google.generativeai as genai
from PIL import Image
import time

# --- 1. CORE CONFIGURATION ---
# 👉 Your Master API Key
MASTER_KEY = "AIzaSyBUHE7pfE3ievPC2ij30jXsVSqcY6wVjIg" 
genai.configure(api_key=MASTER_KEY)

# Using Gemini 1.5 Flash for Super Fast Responses
model = genai.GenerativeModel('gemini-1.5-flash')

# --- 2. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="CogniSpark AI",
    page_icon="⚡",
    layout="wide"
)

# --- 3. MASTER CYBERSTYLE UI ---
st.markdown("""
    <style>
    .main { background-color: #050a10; color: #00ffc3; }
    .stTextInput > div > div > input { background-color: #101720; color: #00ffc3; border: 1px solid #00ffc3; }
    .stButton>button { width: 100%; background: linear-gradient(45deg, #00ffc3, #0080ff); color: black; font-weight: bold; border-radius: 8px; border: none; height: 3em; }
    .stButton>button:hover { box-shadow: 0px 0px 20px #00ffc3; transform: scale(1.02); }
    .sidebar .sidebar-content { background-color: #101720; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. SIDEBAR (OPTIONS PANEL) ---
with st.sidebar:
    st.title("⚡ COGNI-CORE v3")
    st.markdown("---")
    mode = st.selectbox("🛠️ SELECT MODE:", [
        "Instant Answer", 
        "Image/Screenshot Analysis", 
        "Deep Research", 
        "Code Explainer"
    ])
    st.info("Status: System Operational ✅")
    st.write("Ready to process neural packets...")

# --- 5. MAIN INTERFACE ---
st.title("🛸 COGNISPARK: NEURAL LINK")
st.write("---")

if mode == "Image/Screenshot Analysis":
    st.subheader("📸 Upload Screenshot or Image")
    uploaded_file = st.file_uploader("Drop your image here...", type=["jpg", "jpeg", "png"])
    user_prompt = st.text_input("📡 Any specific question about this image?", placeholder="e.g. Solve this math problem or explain this graph...")
    
    if st.button("🚀 ANALYZE IMAGE"):
        if uploaded_file:
            img = Image.open(uploaded_file)
            st.image(img, caption="Target Image", width=400)
            with st.status("🧠 Scanning Image Layers...", expanded=True):
                response = model.generate_content([user_prompt if user_prompt else "Analyze this image in detail", img])
                st.markdown("### 💎 AI INSIGHT:")
                st.write(response.text)
        else:
            st.warning("❗ Please upload an image first.")

else:
    st.subheader("📡 Neural Terminal")
    user_query = st.text_area("ENTER COMMAND / QUERY:", placeholder="Type anything you want to know...", height=150)
    
    if st.button("⚡ EXECUTE GENERATION"):
        if user_query:
            with st.status("🛠️ Extracting Knowledge...", expanded=True) as status:
                try:
                    # Logic based on mode
                    final_prompt = f"Mode: {mode}. Query: {user_query}"
                    response = model.generate_content(final_prompt)
                    status.update(label="✅ TASK COMPLETED", state="complete", expanded=False)
                    st.markdown("### 💎 RETRIEVED INTELLIGENCE:")
                    st.success(response.text)
                    st.balloons()
                except Exception as e:
                    st.error(f"⚠️ CORE ERROR: {str(e)}")
        else:
            st.warning("❗ Input terminal is empty.")

# --- FOOTER ---
st.markdown("---")
st.caption("© 2026 CogniSpark Master OS | Developed for High-Speed AI Interaction")
