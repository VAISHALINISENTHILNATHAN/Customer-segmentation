#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
import datetime as dt

# -------------------------------------------------------------
# LOAD + CLEAN DATA (CSV)
# -------------------------------------------------------------
def load_and_clean_data(path="data/online_retail_II.csv"):
    df = pd.read_csv(path)

    df = df.dropna(subset=["Customer ID"])
    df = df[(df["Quantity"] > 0) & (df["Price"] > 0)].copy()

    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    df["Customer ID"] = df["Customer ID"].astype(int)
    df["TotalPrice"] = df["Quantity"] * df["Price"]

    return df


# -------------------------------------------------------------
# RFM CREATION
# -------------------------------------------------------------
def create_rfm(df):
    snapshot_date = df["InvoiceDate"].max() + dt.timedelta(days=1)

    rfm = (
        df.groupby("Customer ID")
        .agg({
            "InvoiceDate": lambda x: (snapshot_date - x.max()).days,
            "Invoice": "nunique",
            "TotalPrice": "sum"
        })
        .reset_index()
    )

    rfm.columns = ["CustomerID", "Recency", "Frequency", "Monetary"]
    return rfm


# -------------------------------------------------------------
# SCALING
# -------------------------------------------------------------
def scale_rfm(rfm):
    scaler = StandardScaler()
    rfm_scaled = scaler.fit_transform(rfm[["Recency", "Frequency", "Monetary"]])
    return rfm_scaled, scaler


# -------------------------------------------------------------
# EVALUATE K RANGE
# -------------------------------------------------------------
def evaluate_k(rfm_scaled, k_min=2, k_max=10):
    sse = []
    sil = []
    k_values = range(k_min, k_max + 1)

    for k in k_values:
        model = KMeans(n_clusters=k, random_state=42)
        model.fit(rfm_scaled)

        sse.append(model.inertia_)
        sil.append(silhouette_score(rfm_scaled, model.labels_))

    return list(k_values), sse, sil


# -------------------------------------------------------------
# FINAL CLUSTERING
# -------------------------------------------------------------
def cluster_rfm(rfm, rfm_scaled, k):
    model = KMeans(n_clusters=k, random_state=42)
    labels = model.fit_predict(rfm_scaled)

    rfm["Cluster"] = labels.astype(str)
    return rfm, model


# -------------------------------------------------------------
# PCA PROJECTION
# -------------------------------------------------------------
def add_pca(rfm, rfm_scaled):
    pca = PCA(n_components=2)
    comps = pca.fit_transform(rfm_scaled)

    rfm["PCA1"] = comps[:, 0]
    rfm["PCA2"] = comps[:, 1]
    return rfm, pca


# -------------------------------------------------------------
# CLUSTER PROFILE SUMMARY
# -------------------------------------------------------------
def cluster_profile(rfm):
    profile = (
        rfm.groupby("Cluster")
        .agg({
            "Recency": "mean",
            "Frequency": "mean",
            "Monetary": ["mean", "count"]
        })
        .round(1)
    )

    profile.columns = ["RecencyMean", "FrequencyMean", "MonetaryMean", "NumCustomers"]
    return profile.reset_index()


# In[ ]:




