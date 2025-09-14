

---

# Marketing Dashboard

## 📌 Project Overview

This project implements a **Marketing Intelligence Dashboard** using **Streamlit** and **Plotly** to analyze marketing campaigns and business metrics across multiple channels.

The dashboard provides insights into:

* Daily revenue, spend, and attributed revenue trends
* Channel performance comparison (Facebook, Google, TikTok)
* Campaign & tactic ROI drilldown
* Key performance indicators (KPIs) such as Orders, Revenue, ROAS, CAC, and Gross Margin
* Actionable insights for marketing analysts and business stakeholders

---

## 📂 Repository Structure

```
Marketing_Dashboard/
├── app.py                     # Main Streamlit app
├── data/                      # Folder containing CSV files
│   ├── Facebook.csv
│   ├── Google.csv
│   ├── TikTok.csv
│   └── business.csv
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── .gitignore                 # Ignore venv, caches, etc.
```

---

## ⚙️ Setup Instructions

### 1. Clone the repo

```bash
git clone <your-repo-link>
cd Marketing_Dashboard
```

### 2. Install dependencies

It’s recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows

pip install -r requirements.txt
```

Minimal requirements:

* streamlit
* pandas
* plotly
* numpy

### 3. Run the dashboard locally

```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501` to view the dashboard.

> **Note:** Make sure `requirements.txt` is up-to-date; this ensures the app runs smoothly locally or on Streamlit Cloud.

---

## 🚀 Workflow

### 1. Data Preparation

* Marketing CSV files: `Facebook.csv`, `Google.csv`, `TikTok.csv` — containing `date`, `clicks`, `impression`, `spend`, `attributed revenue`, `campaign`, `tactic`.
* Business metrics CSV: `business.csv` — containing `date`, `# of orders`, `# of new orders`, `new customers`, `total revenue`, `gross profit`, `COGS`.
* Ensures column names match app code for proper plotting and KPI calculations.

### 2. Interactive Dashboard Features

* **Custom Sidebar:** Gradient background with white labels and input fields
* **Date & Channel Filters:** Dynamic filtering of data by date range and marketing channel
* **KPIs Overview:** Orders, Revenue, Marketing Spend, Attributed Revenue, ROAS, CAC
* **Trend Analysis:** Interactive line charts for revenue, spend, and attributed revenue
* **Channel Comparison:** Bar charts comparing spend vs attributed revenue across channels
* **Campaign Drilldown:** Bubble charts for ROI per campaign/tactic with impressions sizing
* **Insights Panel:** Actionable insights generated based on data trends

---

## 🌐 Deployment

The dashboard is hosted on Streamlit:

[🔗 **Live Demo on Streamlit**](https://share.streamlit.io/your-username/your-repo/main/app.py)

Or deploy it yourself:

1. Push the repo to GitHub.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and click **New App**.
3. Select your GitHub repository and branch.
4. Choose `app.py` as the main file and deploy.

---

## ✍️ Author

Developed by **Sneha Sivakumar** — Powered by **Streamlit** and **Plotly**.

---

Would you like me to also prepare a **ready-to-use `requirements.txt`** for this dashboard so it runs directly on Streamlit Cloud without errors?
