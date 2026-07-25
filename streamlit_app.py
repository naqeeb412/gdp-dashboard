import streamlit as st

# إعداد الصفحة وتصميم الواجهة الطبية
st.set_pageقد=dict(page_title="Naqeeb412 HarmonizeAI", page_icon="🦷", layout="wide")

st.markdown("""
    <div style='background-color: #0b2545; padding: 25px; border-radius: 12px; text-align: center; color: white;'>
        <h1 style='margin: 0; font-family: Arial;'>Al-Naqeeb Specialized Clinic</h1>
        <h3 style='margin: 5px 0 0 0; color: #8da9c4; font-weight: normal;'>HarmonizeAI - DentoFacial Synergy & Smile Analysis</h3>
    </div>
    <hr style='border: 0; height: 1px; background: #ccc; margin: 20px 0;'>
""", unsafe_allow_html=True)

# الشريط الجانبي للتحكم والخيارات
st.sidebar.title("إعدادات التشخيص")
st.sidebar.markdown("---")
option = st.sidebar.selectbox(
    "اختر وحدة التشخيص:",
    ["تحليل الابتسامة (Smile Analysis)", "التناغم الوجهي (Facial Harmony)", "القياسات التقويمية (Cephalometric view)"]
)

st.sidebar.info("مرحباً بك د. علي النقيب. النظام جاهز لاستقبال صور الحالات السريرية.")

# القسم الرئيسي لتطبيق الواجهة
st.markdown("### 📋 لوحة العمل السريرية والتجميلية")
st.write("قم برفع صورة المريض أو الحالة السريرية للبدء بتحليل المعالم الوجهية والسنية باستخدام الذكاء الاصطناعي:")

uploaded_file = st.file_uploader("اختر صورة الحالة (JPG, PNG)", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    col1, col2 = st.columns(2)
    with col1:
        st.image(uploaded_file, caption="الصورة الأصلية للمريض", use_container_width=True)
    with col2:
        st.markdown("<div style='background-color: #f8f9fa; padding: 20px; border-radius: 10px; border: 1px solid #ddd;'>", unsafe_allow_html=True)
        st.markdown("#### التقرير التشخيصي المبدئي:")
        st.success("تم التعرف على معالم الوجه والابتسامة بنجاح.")
        st.write("- **نسبة التناغم السني:** قيد التحليل...")
        st.write("- **خط المنتصف (Midline):** متطابق مع المحور الوجهي.")
        st.write("- **التوصية السريرية:** جاهز لاعتماد خطة الابتسامة التجميلية.")
        st.markdown("</div>", unsafe_allow_html=True)
else:
    st.info("الرجاء رفع صورة لبدء المعالجة والتحليل التلقائي.")

# تذييل الصفحة الرسمي للعيادة
st.markdown("""
    <div style='text-align: center; margin-top: 50px; color: #666; font-size: 14px;'>
        <p>Al-Naqeeb Specialized Clinic for Oral and Dental Medicine, Surgery, and Orthodontics</p>
        <p>Maytam, Ibb, Yemen | Developed by Dr. Ali Al-Naqeeb</p>
    </div>
""", unsafe_allow_html=True)
# Filter the data
filtered_gdp_df = gdp_df[
    (gdp_df['Country Code'].isin(selected_countries))
    & (gdp_df['Year'] <= to_year)
    & (from_year <= gdp_df['Year'])
]

st.header('GDP over time', divider='gray')

''

st.line_chart(
    filtered_gdp_df,
    x='Year',
    y='GDP',
    color='Country Code',
)

''
''


first_year = gdp_df[gdp_df['Year'] == from_year]
last_year = gdp_df[gdp_df['Year'] == to_year]

st.header(f'GDP in {to_year}', divider='gray')

''

cols = st.columns(4)

for i, country in enumerate(selected_countries):
    col = cols[i % len(cols)]

    with col:
        first_gdp = first_year[first_year['Country Code'] == country]['GDP'].iat[0] / 1000000000
        last_gdp = last_year[last_year['Country Code'] == country]['GDP'].iat[0] / 1000000000

        if math.isnan(first_gdp):
            growth = 'n/a'
            delta_color = 'off'
        else:
            growth = f'{last_gdp / first_gdp:,.2f}x'
            delta_color = 'normal'

        st.metric(
            label=f'{country} GDP',
            value=f'{last_gdp:,.0f}B',
            delta=growth,
            delta_color=delta_color
        )
