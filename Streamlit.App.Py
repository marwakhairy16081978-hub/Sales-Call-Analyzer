import streamlit as st
from google import genai

# ==================== إعداد الصفحة ====================
st.set_page_config(
    page_title="محلل مكالمات المبيعات الذكي",
    page_icon="📞",
    layout="wide"
)

st.title("📞 محلل مكالمات المبيعات بالذكاء الاصطناعي")
st.write("قم برفع ملف نصي يحتوي على نص مكالمة المبيعات، وسيقوم النظام بتحليله واستخراج النقاط الهامة.")

# ==================== إدخال مفتاح API ====================
st.sidebar.header("🔑 إعدادات Gemini API")
api_key = st.sidebar.text_input(
    "أدخل مفتاح Gemini API الخاص بك:",
    type="password",
    help="احصل على المفتاح من https://aistudio.google.com/app/apikeys"
)

# ==================== رفع الملف ====================
st.header("📁 رفع ملف المكالمة")
uploaded_file = st.file_uploader(
    "اختر ملف نصي للمكالمة (TXT)",
    type=["txt"],
    help="الملف يجب أن يكون بصيغة .txt فقط"
)

if uploaded_file is not None and api_key:
    # قراءة محتوى الملف
    call_text = uploaded_file.read().decode("utf-8")
    
    with st.expander("📄 عرض نص المكالمة الأصلي", expanded=False):
        st.text_area("نص المكالمة", call_text, height=200, disabled=True)
        
    if st.button("🚀 بدء التحليل الشامل", type="primary", use_container_width=True):
        with st.spinner("جاري تحليل مكالمة باستخدام Gemini 2.5 Flash..."):
            try:
                client = genai.Client(api_key=api_key)
                
                prompt = f"""
                قم بتحليل مكالمات المبيعات التالية بدقة واحترافية علامية. قدم التحليل باللغة العربية ويتضمن:

                1. ملخص تنفيذي للمكالمة.
                2. أبرز نقاط الألم واحتياجات العميل.
                3. الاعتراضات التي أبداها العميل وكيف تم التعامل معها.
                4. تقي<|eos|>
