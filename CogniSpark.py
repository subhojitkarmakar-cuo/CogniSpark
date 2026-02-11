import streamlit as st
import google.generativeai as genai
from PIL import Image
import time

# --- 1. CORE CONFIGURATION ---
MASTER_KEY = "AIzaSyBsacLLewat063GPMl2T-UBS90L4SRUS8A" 
genai.configure(api_key=MASTER_KEY)

# --- 2. AUTO-ENGINE SELECTOR (Avoids 404 Errors) ---
def get_working_engine():
    try:
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        final_model_name = next((m for m in available_models if "1.5-flash" in m), available_models[0])
        return genai.GenerativeModel(final_model_name)
    except Exception:
        return genai.GenerativeModel('gemini-1.5-flash')

model_engine = get_working_engine()

# --- 3. PAGE CONFIGURATION & UI ---
st.set_page_config(page_title="CogniSpark AI", page_icon="🛸", layout="wide")

# Cyberpunk Style Design (CSS)
st.markdown("""
    <style>
    .main { background-color: #050a10; color: #00ffc3; }
    .stButton>button { 
        width: 100%; 
        background: linear-gradient(45deg, #00ffc3, #0080ff); 
        color: black; 
        font-weight: bold; 
        border-radius: 10px; 
        border: none;
        height: 3.5em;
        transition: 0.3s;
    }
    .stButton>button:hover { 
        box-shadow: 0px 0px 25px #00ffc3; 
        transform: translateY(-2px); 
    }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea { 
        background-color: #101720; 
        color: #00ffc3; 
        border: 1px solid #00ffc3; 
        border-radius: 8px;
    }
    .stMarkdown { font-family: 'Courier New', Courier, monospace; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. SIDEBAR CONTROL PANEL ---
with st.sidebar:
    st.title("🛸 COGNI-LINK v5")
    st.markdown("---")
    mode = st.radio("SELECT MISSION PROTOCOL:", ["📡 Text Terminal", "📸 Live Camera / Scan"])
    st.markdown("---")
    st.success("SYSTEM: ONLINE ✅")
    st.code(f"ENGINE: {model_engine.model_name.split('/')[-1]}", language="bash")

# --- 5. MAIN INTERFACE LOGIC ---
st.title("🛸 COGNISPARK: NEURAL INTERFACE")
st.write("---")

if mode == "📸 Live Camera / Scan":
    st.subheader("📷 Live Book Scanner")
    # Access camera for capturing book/problem images
    cam_image = st.camera_input("Capture an image of the problem or book page")
    
    if cam_image:
        img = Image.open(cam_image)
        st.image(img, caption="Captured Frame", width=400)
        
        user_prompt = st.text_input("📡 Specific instructions for this scan?", placeholder="Leave blank for auto-analysis...")
        
        if st.button("🚀 INITIATE SCAN ANALYSIS"):
            with st.status("🧠 Analyzing Visual Packets...", expanded=True):
                try:
                    final_prompt = user_prompt if user_prompt else "Explain this image or solve the problems shown in it in detail."
                    response = model_engine.generate_content([final_prompt, img])
                    st.markdown("### 💎 AI INSIGHTS:")
                    st.info(response.text)
                except Exception as e:
                    st.error(f"❌ SCAN ERROR: {str(e)}")

else:
    st.subheader("📡 Neural Command Terminal")
    query = st.text_area("ENTER YOUR QUERY / COMMAND:", placeholder="Type your question or request here...", height=200)
    
    if st.button("⚡ EXECUTE NEURAL LINK"):
        if query:
            with st.status("🛠️ Extracting Knowledge Base...", expanded=True) as status:
                try:
                    # Generate AI response
                    res = model_engine.generate_content(query)
                    status.update(label="✅ GENERATION COMPLETE", state="complete", expanded=False)
                    st.markdown("### 💎 RETRIEVED INTELLIGENCE:")
                    st.success(res.text)
                    st.balloons()
                except Exception as e:
                    st.error(f"⚠️ SYSTEM CRITICAL ERROR: {str(e)}")
        else:
            st.warning("❗ TERMINAL ALERT: Input cannot be empty.")

# --- 6. FOOTER ---
st.markdown("---")
st.caption("© 2026 CogniSpark Master Core | High-Speed Neural Link Enabled")
