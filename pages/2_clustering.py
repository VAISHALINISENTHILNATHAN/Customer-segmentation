#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import plotly.express as px
import modules.rfm_processing as rp

st.title("🎯 Customer Segmentation using K-Means")

df = rp.load_and_clean_data("data/online_retail_II.csv")
rfm = rp.create_rfm(df)
rfm_scaled, scaler = rp.scale_rfm(rfm)

k = st.slider("Select number of clusters (k)", 2, 12, 4)

rfm, model = rp.cluster_rfm(rfm, rfm_scaled, k)
rfm, pca = rp.add_pca(rfm, rfm_scaled)

st.subheader("PCA Cluster Plot")

fig = px.scatter(
    rfm,
    x="PCA1",
    y="PCA2",
    color="Cluster",
    hover_data=["CustomerID", "Monetary"],
    title=f"PCA Cluster Projection (k={k})"
)

st.plotly_chart(fig, use_container_width=True)

profile = rp.cluster_profile(rfm)

st.subheader("Cluster Profiles")
st.dataframe(profile)

st.download_button("Download RFM Segments", rfm.to_csv(index=False), "rfm_segments.csv")


# In[ ]:




