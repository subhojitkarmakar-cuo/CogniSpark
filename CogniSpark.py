import streamlit as st
import google.generativeai as genai
import time

# --- ১. কনফিগারেশন এবং এপিআই কী ---
MASTER_KEY = "AIzaSyBUHE7pfE3ievPC2ij30jXsVSqcY6wVjIg" 
genai.configure(api_key=MASTER_KEY)

# --- ২. অটো-মডেল সিলেকশন (যাতে ৪০৪ এরর না আসে) ---
def get_valid_model():
    # এটি আপনার এপিআই কী-তে সচল থাকা সবথেকে ভালো মডেলটি খুঁজে নেবে
    try:
        models = ['gemini-1.5-flash-latest', 'gemini-1.5-flash', 'gemini-pro']
        for m in models:
            try:
                test_model = genai.GenerativeModel(m)
                test_model.generate_content("hi")
                return test_model
            except:
                continue
        # যদি উপরের কোনটি কাজ না করে তবে একাউন্টের প্রথম মডেলটি নেবে
        valid_list = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        return genai.GenerativeModel(valid_list[0])
    except Exception:
        return genai.GenerativeModel('gemini-1.5-flash')

model = get_valid_model()

# --- ৩. পেজ কনফিগারেশন এবং এসইও ---
st.set_page_config(
    page_title="CogniSpark AI | Neural Study Engine",
    page_icon="⚡",
    layout="wide"
)

# গুগল ভেরিফিকেশন ট্যাগ (মেটা ট্যাগ পদ্ধতি)
st.markdown("""
    <head>
        <meta name="google-site-verification" content="M-XoUbvsIR0HE4L_LW90lOg8btmH60yP2gCAEkxXJJo" />
        <meta name="description" content="CogniSpark AI - The ultimate neural study assistant.">
    </head>
    """, unsafe_allow_html=True)

# --- ৪. ইউজার ইন্টারফেস ডিজাইন (CSS) ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #00ffc3; }
    .stTextInput > div > div > input { background-color: #161b22; color: #00ffc3; border: 1px solid #00ffc3; border-radius: 10px; }
    .stButton>button { width: 100%; background: linear-gradient(45deg, #00ffc3, #0080ff); color: black; font-weight: bold; border-radius: 10px; border: none; }
    .stButton>button:hover { transform: scale(1.05); box-shadow: 0px 0px 20px #00ffc3; }
    </style>
    """, unsafe_allow_html=True)

# --- ৫. সাইডবার ---
with st.sidebar:
    st.title("⚡ SYSTEM STATUS")
    st.code("STATUS: ONLINE\nCORE: NEURAL-v2\nUSER: AUTHORIZED", language="bash")
    st.image("https://img.icons8.com/nolan/128/artificial-intelligence.png")

# --- ৬. মেইন ইন্টারফেস ---
st.title("🛸 COGNISPARK: NEURAL INTERFACE")
st.write("---")

user_input = st.text_input("📡 TERMINAL_INPUT >", placeholder="আপনার প্রশ্নটি এখানে লিখুন...")

if st.button("🚀 EXECUTE GENERATION"):
    if user_input:
        with st.status("🛠️ Processing Neural Data...", expanded=True) as status:
            try:
                response = model.generate_content(user_input)
                status.update(label="✅ SUCCESS", state="complete", expanded=False)
                st.markdown("### 💎 RESULT:")
                st.success(response.text)
                st.balloons()
            except Exception as e:
                st.error(f"⚠️ ERROR: {str(e)}")
    else:
        st.warning("❗ ইনপুট খালি রাখা যাবে না।")

st.markdown("---")
st.caption("© 2026 CogniSpark | All Rights Reserved")
