import streamlit as st
import pandas as pd

from modules.upload import upload_data
from modules.segmentation import run_segmentation
from modules.forecasting import run_forecast
from modules.kpi import show_kpis
from modules.export import export_data

st.set_page_config(page_title="Business Insight Studio", layout="wide")
st.title("📊 Business Insight Studio")

if "df" not in st.session_state:
    st.session_state.df = None

menu = st.sidebar.radio("📂 Navigate", [
    "Upload", "Segmentation", "Forecasting", "KPIs", "Export"
])

if menu == "Upload":
    upload_data()

# Chỉ gọi các module còn lại khi có dữ liệu
elif st.session_state.get("df") is None:
    st.warning("⚠️ Please upload a CSV file first.")

else:
    df = st.session_state.df  # lấy ra một lần

    if menu == "Segmentation":
        run_segmentation(df)
    elif menu == "Forecasting":
        run_forecast(df)
    elif menu == "KPIs":
        show_kpis()
    elif menu == "Export":
        export_data(df)
    elif menu == "AI Explainer":
        run_ai_explainer()
