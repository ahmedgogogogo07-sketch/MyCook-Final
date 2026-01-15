import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="شيف ماي كوك", layout="wide")

# تهيئة الاتصال
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("المفتاح غير مضبوط في الأسرار")
    st.stop()

st.title("👨‍🍳 شيف ماي كوك")

prompt = st.text_input("ماذا تملك في الثلاجة؟")
if st.button("ابتكر وجبة 🚀"):
    with st.spinner('جاري التفكير...'):
        try:
            response = model.generate_content(f"اقترح وجبة مصرية بـ {prompt}")
            st.info(response.text)
        except Exception as e:
            st.error(f"خطأ: {e}")
          
