import streamlit as st

def export_data(df):
    st.subheader("📥 Export Processed Data")

    if df is None or df.empty:
        st.warning("No data to export.")
        return

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Download CSV", data=csv, file_name="processed_data.csv", mime="text/csv")
