🛒 Customer Segmentation Dashboard

An interactive, multi-page Streamlit dashboard for RFM-based customer segmentation, clustering, and automated insights. Designed to analyze online retail data, identify valuable customer segments, and provide actionable business intelligence 

🔹 Key Features

RFM Analysis: Explore Recency, Frequency, and Monetary metrics for all customers.
K-Means Clustering: Segment customers interactively with adjustable number of clusters.
PCA Visualization: 2D projection of clusters for easy interpretation.
Automated Insights: Narrative summaries highlighting high-value and low-value segments.
Interactive & Modern UI: Plotly charts, sidebar navigation, KPI cards, multi-page layout.
Downloadable Reports: Export RFM segments and cluster profiles as CSV.

🛠 Tech Stack

Python 3.10+
Streamlit (multi-page, interactive dashboard)
Pandas & NumPy (data manipulation)
scikit-learn (StandardScaler, KMeans, PCA)
Plotly & Seaborn (interactive & static visualizations)

💻 Project Structure
customer-segmentation-dashboard/
│
├── app.py                    # main launcher
├── pages/                    # multi-page Streamlit app
│   ├── 1_📊_RFM_Overview.py
│   ├── 2_🎯_Clustering.py
│   └── 3_📈_Insights_and_Reports.py
├── modules/
│   └── rfm_processing.py     # data processing & clustering functions
├── data/
│   └── online_retail_II.csv
└── .streamlit/
    └── config.toml           # custom Streamlit theme

🚀 How to Run Locally

Clone the repo:

git clone https://github.com/<yourusername>/customer-segmentation-dashboard.git
cd customer-segmentation-dashboard

Install dependencies:

pip install -r requirements.txt

Run the app:

streamlit run app.py


