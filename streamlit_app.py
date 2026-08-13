import streamlit as st
import pandas as pd
import numpy as np

# إعدادات الصفحة
st.set_page_config(
    page_title="GDP Dashboard",
    page_icon="🌍",
    layout="wide"
)

st.title("🌎 GDP Dashboard")
st.write("لوحة مؤشرات الناتج المحلي الإجمالي التجريبية.")

# إنشاء بيانات تجريبية (أو يمكنك ربطها بملف بيانات حقيقي في مجلد data)
@st.cache_data
def load_data():
    # بيانات افتراضية للتوضيح
    data = pd.DataFrame({
        'Year': [2021, 2022, 2023, 2024, 2025],
        'Country A': [100, 105, 110, 118, 125],
        'Country B': [80, 85, 88, 95, 102],
        'Country C': [200, 210, 215, 230, 245]
    })
    return data

df = load_data()

# شريط جانبي للاختيار
st.sidebar.header("إعدادات العرض")
selected_country = st.sidebar.selectbox("اختر الدولة:", ['Country A', 'Country B', 'Country C'])

# عرض البيانات والرسوم البيانية
st.sub_header(f"بيانات الناتج المحلي لـ {selected_country}")
st.line_chart(df.set_index('Year')[selected_country])

st.write("جدول البيانات الكامل:")
st.dataframe(df)
