#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import modules.rfm_processing as rp

st.title("📈 Automated Insights & Reporting")

df = rp.load_and_clean_data("data/online_retail_II.csv")
rfm = rp.create_rfm(df)
rfm_scaled, _ = rp.scale_rfm(rfm)
rfm, _ = rp.cluster_rfm(rfm, rfm_scaled, 4)  # default k=4
profile = rp.cluster_profile(rfm)

st.subheader("Cluster Insights")

for _, row in profile.iterrows():
    st.markdown(f"""
### Cluster {row['Cluster']}
- **Recency Mean:** {row['RecencyMean']} days  
- **Frequency Mean:** {row['FrequencyMean']}  
- **Monetary Mean:** ${row['MonetaryMean']}  
- **Customers:** {row['NumCustomers']}

#### Interpretation:
- {"🔥 High-value repeat customers" if row['MonetaryMean'] > profile['MonetaryMean'].mean() else "🧊 Low-value customer segment"}
- {"💡 Active recent shoppers" if row['RecencyMean'] < profile['RecencyMean'].mean() else "⚠️ Customers needing reactivation"}

---
""")


# In[ ]:




