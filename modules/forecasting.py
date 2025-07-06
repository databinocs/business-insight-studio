import streamlit as st
import pandas as pd
from prophet import Prophet
import plotly.graph_objs as go

def run_forecast(df: pd.DataFrame):
    st.header("🔮 Forecasting Module")

    # 1. Chọn cột thời gian và cột giá trị số
    datetime_cols = df.select_dtypes(include=["datetime", "object"]).columns.tolist()
    numeric_cols = df.select_dtypes(include="number").columns.tolist()

    if not datetime_cols or not numeric_cols:
        st.warning("⚠️ No valid datetime or numeric columns available.")
        return

    datetime_col = st.selectbox("🕒 Select time column", datetime_cols)
    value_col = st.selectbox("🎯 Select value column", numeric_cols)

    # 2. Chọn số ngày dự báo
    periods = st.slider("📆 Forecast periods (days)", 7, 180, value=30)

    # 3. Run Forecast
    if st.button("🚀 Run Forecast"):
        try:
            # Tạo bản sao, không ghi đè df gốc
            data = df[[datetime_col, value_col]].dropna().copy()
            data.columns = ['ds', 'y']
            data['ds'] = pd.to_datetime(data['ds'])

            # Khởi tạo và huấn luyện model
            model = Prophet()
            model.fit(data)

            future = model.make_future_dataframe(periods=periods)
            forecast = model.predict(future)

            # 4. Vẽ biểu đồ Actual vs Forecast
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=data['ds'], y=data['y'], mode='lines', name='Actual'))
            fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'], mode='lines', name='Forecast'))

            fig.update_layout(title="📈 Forecast Result", xaxis_title="Date", yaxis_title=value_col)
            st.plotly_chart(fig, use_container_width=True)

            # 5. Xem bảng dữ liệu dự báo
            with st.expander("📋 Forecasted Data"):
                st.dataframe(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(periods))

        except Exception as e:
            st.error(f"❌ Forecasting failed: {e}")
