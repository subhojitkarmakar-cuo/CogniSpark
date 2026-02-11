import streamlit as st
import google.generativeai as genai
import time

# --- 1. CONFIGURATION ---
# Your Working API Key
MASTER_KEY = "AIzaSyBUHE7pfE3ievPC2ij30jXsVSqcY6wVjIg" 
genai.configure(api_key=MASTER_KEY)

# --- 2. SMART MODEL SELECTION (Fixes 404 Error) ---
def get_active_model():
    # It attempts to find the best available model for your key
    candidates = ['gemini-1.5-flash-latest', 'gemini-1.5-flash', 'gemini-pro']
    for m in candidates:
        try:
            temp = genai.GenerativeModel(m)
            temp.generate_content("test") # Connection test
            return temp
        except:
            continue
    # Fallback to the first authorized model in your account
    available = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    return genai.GenerativeModel(available[0])

model = get_active_model()

# --- 3. PAGE SETUP & SEO ---
st.set_page_config(
    page_title="CogniSpark | AI Neural Engine",
    page_icon="⚡",
    layout="wide"
)

# HTML for Google Verification & SEO
st.markdown("""
    <div style="display:none;">
        <meta name="google-site-verification" content="M-XoUbvsIR0HE4L_LW90lOg8btmH60yP2gCAEkxXJJo" />
        <meta name="description" content="CogniSpark AI - Advanced Neural Interface for Smart Learning and Analysis.">
    </div>
    """, unsafe_allow_html=True)

# --- 4. CYBER STYLE UI (CSS) ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #00ffc3; }
    .stTextInput > div > div > input { background-color: #161b22; color: #00ffc3; border: 1px solid #00ffc3; border-radius: 10px; }
    .stButton>button { width: 100%; background: linear-gradient(45deg, #00ffc3, #0080ff); color: black; font-weight: bold; border-radius: 10px; border: none; }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0px 0px 15px #00ffc3; }
    </style>
    """, unsafe_allow_html=True)

# --- 5. SIDEBAR ---
with st.sidebar:
    st.title("⚡ SYSTEM STATUS")
    st.code("STATUS: ONLINE\nCORE: NEURAL-LINK-v2\nUSER: AUTHORIZED", language="bash")
    st.markdown("---")
    st.image("https://img.icons8.com/nolan/128/artificial-intelligence.png")

# --- 6. MAIN INTERFACE ---
st.title("🛸 COGNISPARK: NEURAL INTERFACE")
st.write("---")

col1, col2 = st.columns([3, 1])
with col1:
    user_input = st.text_input("📡 TERMINAL_INPUT >", placeholder="Enter your query...")
with col2:
    mode = st.selectbox("🛠️ PROTOCOL:", ["Deep Analysis", "Smart Notes", "Quick Solve", "Root Access"])

if st.button("🚀 EXECUTE GENERATION"):
    if user_input:
        with st.status("🛠️ Injecting Neural Packets...", expanded=True) as status:
            st.write("🔍 Scanning Neural Core...")
            time.sleep(1)
            try:
                prompt = f"System Mode: {mode}. Task: Professional response for: {user_input}"
                response = model.generate_content(prompt)
                status.update(label="✅ TASK COMPLETED", state="complete", expanded=False)
                
                st.markdown("### 💎 RETRIEVED INTELLIGENCE:")
                st.success(response.text)
                st.balloons()
            except Exception as e:
                st.error(f"⚠️ SYSTEM ERROR: {str(e)}")
    else:
        st.warning("❗ INPUT REQUIRED.")

st.markdown("---")
st.caption("© 2026 CogniSpark Master Core | Unauthorized duplication is prohibited.")
                
