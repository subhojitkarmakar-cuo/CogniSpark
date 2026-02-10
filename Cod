import streamlit as st
import google.generativeai as genai
import time

# --- CONFIGURATION & SECURITY ---
MASTER_KEY = "AIzaSyBsacLLewat063GPMl2T-UBS90L4SRUS8A" 

genai.configure(api_key=MASTER_KEY)
model = genai.GenerativeModel('gemini-pro')

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="CogniSpark | AI Neural Engine",
    page_icon="⚡",
    layout="wide"
)

# --- CYBER HACKER STYLE CSS ---
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: #00ffc3;
    }
    .stTextInput > div > div > input {
        background-color: #161b22;
        color: #00ffc3;
        border: 1px solid #00ffc3;
        border-radius: 10px;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(45deg, #00ffc3, #0080ff);
        color: black;
        font-weight: bold;
        border: none;
        border-radius: 10px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0px 0px 15px #00ffc3;
    }
    .stMarkdown {
        font-family: 'Courier New', Courier, monospace;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR INTERFACE ---
with st.sidebar:
    st.title("⚡ SYSTEM STATUS")
    st.code("STATUS: ONLINE\nCORE: NEURAL-LINK-v2\nUSER: AUTHORIZED\nENC: SH-512", language="bash")
    st.markdown("---")
    st.image("https://img.icons8.com/nolan/128/artificial-intelligence.png")
    st.info("CogniSpark OS is running on Master Mode.")

# --- MAIN INTERFACE ---
st.title("🛸 COGNISPARK: NEURAL INTERFACE")
st.write("---")

col1, col2 = st.columns([3, 1])

with col1:
    user_input = st.text_input("📡 TERMINAL_INPUT >", placeholder="Enter your query to bypass complexity...")

with col2:
    mode = st.selectbox("🛠️ PROTOCOL:", ["Deep Analysis", "Smart Notes", "Quick Solve", "Root Access"])

if st.button("🚀 EXECUTE GENERATION"):
    if user_input:
        with st.status("🛠️ Injecting Neural Packets...", expanded=True) as status:
            st.write("🔍 Scanning Global Databases...")
            time.sleep(1)
            st.write("🧠 Decrypting AI Core...")
            time.sleep(1)
            st.write("🛡️ Compiling Results...")
            
            try:
                # Engineering the Prompt
                system_prompt = f"Mode: {mode}. Task: Provide a high-level, professional, and detailed response for: {user_input}. Use markdown headers and logical structure."
                response = model.generate_content(system_prompt)
                
                status.update(label="✅ TASK COMPLETED", state="complete", expanded=False)
                
                # --- MASTER OUTPUT ---
                st.markdown("### 💎 RETRIEVED INTELLIGENCE:")
                st.success(response.text)
                st.balloons()
                
            except Exception as e:
                st.error(f"⚠️ SYSTEM CRITICAL ERROR: {str(e)}")
    else:
        st.warning("❗ ACCESS DENIED: Input field is empty.")

# --- FOOTER ---
st.markdown("---")
st.caption("© 2026 CogniSpark Master Core | Unauthorized duplication is prohibited.")
