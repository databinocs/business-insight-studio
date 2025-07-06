import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import plotly.express as px
import matplotlib.pyplot as plt

def run_segmentation(df: pd.DataFrame):
    st.header("👥 Segmentation Studio")

    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    selected_cols = st.multiselect("Select features for clustering", numeric_cols)

    if len(selected_cols) < 2:
        st.info("Please select at least two numeric columns.")
        return

    X = df[selected_cols].dropna()
    if X.empty:
        st.error("Selected columns have only missing values.")
        return

    X_scaled = StandardScaler().fit_transform(X)

    # 📌 Optional: Elbow method
    if st.checkbox("🤖 Suggest optimal number of clusters (Elbow Method)"):
        st.info("Running Elbow Method...")
        inertias = []
        Ks = list(range(2, 11))
        for k in Ks:
            km = KMeans(n_clusters=k, random_state=42)
            km.fit(X_scaled)
            inertias.append(km.inertia_)

        fig_elbow, ax = plt.subplots()
        ax.plot(Ks, inertias, marker='o')
        ax.set_xlabel("Number of clusters (K)")
        ax.set_ylabel("Inertia")
        ax.set_title("Elbow Method for Optimal K")
        st.pyplot(fig_elbow)

    # Số cụm người dùng chọn
    n_clusters = st.slider("Select number of clusters", 2, 10, 3)

    model = KMeans(n_clusters=n_clusters, random_state=42)
    labels = model.fit_predict(X_scaled)

    result_df = df.copy()
    result_df.loc[X.index, "cluster"] = labels.astype(int)
    st.session_state.df = result_df

    st.success("✅ Clustering completed!")

    # PCA cho trực quan
    pca = PCA(n_components=2)
    components = pca.fit_transform(X_scaled)
    plot_df = pd.DataFrame(components, columns=["PC1", "PC2"])
    plot_df["cluster"] = labels.astype(str)

    fig = px.scatter(
        plot_df, x="PC1", y="PC2", color="cluster",
        title="Clusters Visualization (PCA)"
    )
    st.plotly_chart(fig, use_container_width=True)

    # 🧠 Cluster Profiling
    with st.expander("📊 Cluster Profiling (Feature Summary by Group)"):
        profile = result_df.groupby("cluster")[selected_cols].mean().round(2)
        st.dataframe(profile)

    with st.expander("📋 Clustered Data Preview"):
        st.dataframe(result_df.head(10))
