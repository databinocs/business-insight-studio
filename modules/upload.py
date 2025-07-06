import streamlit as st
import pandas as pd

def upload_data():
    st.subheader("📤 Upload CSV File")
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)
            st.session_state.df = df
            st.success("✅ File uploaded successfully!")
            st.dataframe(df.head(10))
        except Exception as e:
            st.error(f"❌ Failed to read file: {e}")
    else:
        st.info("Please upload a CSV to continue.")
