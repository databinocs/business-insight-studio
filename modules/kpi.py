import streamlit as st
import pandas as pd
import plotly.express as px

def show_kpis():
    st.header("📊 Dashboard Overview")

    df = st.session_state.get("df")
    if df is None:
        st.warning("⚠️ Please upload a CSV file first.")
        return

    st.subheader("📌 Dataset Summary")
    st.write(f"🔢 Rows: `{df.shape[0]}` | 📁 Columns: `{df.shape[1]}`")

    with st.expander("🔍 Preview Data"):
        st.dataframe(df.head(10))

    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    if not numeric_cols:
        st.warning("⚠️ No numeric columns found.")
        return

    st.subheader("📊 Statistical Summary")
    stat_df = df[numeric_cols].agg(['mean', 'min', 'max']).T
    stat_df.columns = ['Mean', 'Min', 'Max']
    st.dataframe(stat_df.style.format("{:.2f}"))

    st.subheader("📈 Visualizations")
    selected_col = st.selectbox("Select numeric column", numeric_cols)
    chart_type = st.radio("Chart type", ["Histogram", "Line", "Box", "Scatter"])

    fig = None
    if chart_type == "Histogram":
        fig = px.histogram(df, x=selected_col, nbins=30, title=f"Distribution of {selected_col}")
    elif chart_type == "Line":
        fig = px.line(df, y=selected_col, title=f"{selected_col} over index")
    elif chart_type == "Box":
        fig = px.box(df, y=selected_col, title=f"Boxplot of {selected_col}")
    elif chart_type == "Scatter":
        x_col = st.selectbox("Select x-axis (numeric)", [col for col in numeric_cols if col != selected_col])
        fig = px.scatter(df, x=x_col, y=selected_col, title=f"{selected_col} vs {x_col}")

    if fig:
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("🔗 Correlation Heatmap")
    corr = df[numeric_cols].corr()
    st.dataframe(corr.style.background_gradient(cmap="RdBu", axis=None))
