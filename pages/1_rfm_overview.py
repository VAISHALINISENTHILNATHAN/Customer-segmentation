#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import plotly.express as px
import modules.rfm_processing as rp

st.title("📊 RFM Overview")

df = rp.load_and_clean_data("data/online_retail_II.csv")
rfm = rp.create_rfm(df)

# KPIs
c1, c2, c3 = st.columns(3)
c1.metric("Avg Recency", f"{rfm['Recency'].mean():.1f} days")
c2.metric("Avg Frequency", f"{rfm['Frequency'].mean():.1f}")
c3.metric("Avg Monetary", f"${rfm['Monetary'].mean():.1f}")

st.divider()

st.subheader("Distribution Plots")

fig1 = px.histogram(rfm, x="Recency", nbins=50, title="Recency Distribution")
fig2 = px.histogram(rfm, x="Frequency", nbins=50, title="Frequency Distribution")
fig3 = px.histogram(rfm, x="Monetary", nbins=50, title="Monetary Distribution")

st.plotly_chart(fig1, use_container_width=True)
st.plotly_chart(fig2, use_container_width=True)
st.plotly_chart(fig3, use_container_width=True)


# In[ ]:




