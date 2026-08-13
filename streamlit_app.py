import streamlit as st
import pandas as pd

st.set_page_config(page_title="GDP Dashboard", page_icon="🌍", layout="wide")

st.title("🌎 GDP Dashboard")
st.markdown("لوحة مؤشرات الناتج المحلي الإجمالي وتحليل النمو الاقتصادي.")

# بيانات تجريبية
data = pd.DataFrame({
    'Year': [2021, 2022, 2023, 2024, 2025],
    'Country A': [100, 105, 110, 118, 125],
    'Country B': [80, 85, 88, 95, 102],
    'Country C': [200, 210, 215, 230, 245]
})

st.sidebar.header("إعدادات العرض")
selected_country = st.sidebar.selectbox("اختر الدولة:", ['Country A', 'Country B', 'Country C'])

st.subheader(f"معدل نمو الناتج المحلي لـ {selected_country}")
st.line_chart(data.set_index('Year')[selected_country])

st.markdown("---")
st.subheader("جدول البيانات الكامل")
st.dataframe(data, use_container_width=True)
