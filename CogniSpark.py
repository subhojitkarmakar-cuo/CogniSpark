import streamlit as st
import google.generativeai as genai
from PIL import Image
import time

# --- ১. কোর কনফিগারেশন (আপনার অরিজিনাল এপিআই কি যুক্ত করা হয়েছে) ---
MASTER_KEY = "AIzaSyBsacLLewat063GPMl2T-UBS90L4SRUS8A" 
genai.configure(api_key=MASTER_KEY)

# --- ২. অটো-ইঞ্জিন হান্টার (যাতে ৪০৪ এরর না আসে) ---
def get_working_engine():
    try:
        # আপনার একাউন্টে কোন মডেলটি সচল আছে তা এটি নিজে থেকে খুঁজে বের করবে
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        # gemini-1.5-flash থাকলে সেটি নেবে, না হলে প্রথম কার্যকরী মডেলটি নেবে
        final_model_name = next((m for m in available_models if "1.5-flash" in m), available_models[0])
        return genai.GenerativeModel(final_model_name)
    except Exception:
        # কোনো কারণে লিস্ট না পেলে ডিফল্ট হিসেবে ফ্ল্যাশ ব্যবহার করবে
        return genai.GenerativeModel('gemini-1.5-flash')

# ইঞ্জিন চালু করা হচ্ছে
model_engine = get_working_engine()

# --- ৩. পেজ ডিজাইন ও ইউজার ইন্টারফেস ---
st.set_page_config(page_title="CogniSpark AI", page_icon="🛸", layout="wide")

# সাইবারপাংক স্টাইল ডিজাইন (CSS)
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

# --- ৪. সাইডবার কন্ট্রোল প্যানেল ---
with st.sidebar:
    st.title("🛸 COGNI-LINK v5")
    st.markdown("---")
    mode = st.radio("SELECT MISSION PROTOCOL:", ["📡 Text Terminal", "📸 Live Camera / Scan"])
    st.markdown("---")
    st.success("SYSTEM: ONLINE ✅")
    st.code(f"ENGINE: {model_engine.model_name.split('/')[-1]}", language="bash")

# --- ৫. মেইন ইন্টারফেস লজিক ---
st.title("🛸 COGNISPARK: NEURAL INTERFACE")
st.write("---")

if mode == "📸 Live Camera / Scan":
    st.subheader("📷 Live Book Scanner")
    # মোবাইল বা পিসির ক্যামেরা সরাসরি ওপেন করবে
    cam_image = st.camera_input("বইয়ের বা সমস্যার ছবি তুলুন")
    
    if cam_image:
        img = Image.open(cam_image)
        st.image(img, caption="Captured Frame", width=400)
        
        user_prompt = st.text_input("📡 আপনি কি এই ছবি সম্পর্কে কিছু জানতে চান?", placeholder="খালি রাখলে এটি অটোমেটিক স্ক্যান করবে...")
        
        if st.button("🚀 INITIATE SCAN ANALYSIS"):
            with st.status("🧠 Analyzing Visual Packets...", expanded=True):
                try:
                    final_prompt = user_prompt if user_prompt else "Explain this image or solve the problems in it in detail."
                    response = model_engine.generate_content([final_prompt, img])
                    st.markdown("### 💎 AI INSIGHTS:")
                    st.info(response.text)
                except Exception as e:
                    st.error(f"❌ SCAN ERROR: {str(e)}")

else:
    st.subheader("📡 Neural Command Terminal")
    query = st.text_area("ENTER YOUR QUERY / COMMAND:", placeholder="আপনার যা ইচ্ছা জিজ্ঞেস করুন...", height=200)
    
    if st.button("⚡ EXECUTE NEURAL LINK"):
        if query:
            with st.status("🛠️ Extracting Knowledge Base...", expanded=True) as status:
                try:
                    # এআই থেকে উত্তর জেনারেট করা হচ্ছে
                    res = model_engine.generate_content(query)
                    status.update(label="✅ GENERATION COMPLETE", state="complete", expanded=False)
                    st.markdown("### 💎 RETRIEVED INTELLIGENCE:")
                    st.success(res.text)
                    st.balloons()
                except Exception as e:
                    st.error(f"⚠️ SYSTEM CRITICAL ERROR: {str(e)}")
        else:
            st.warning("❗ TERMINAL ALERT: Input cannot be empty.")

# --- ৬. ফুটার ---
st.markdown("---")
st.caption("© 2026 CogniSpark Master Core | High-Speed Neural Link Enabled")
