```markdown
# Marketing_Dashboard

🌟 **Marketing Intelligence Dashboard** built with **Streamlit** and **Plotly** for analyzing marketing campaigns and business metrics across multiple channels.

[🔗 **Live Demo on Streamlit**](https://marketingdashboard-cxxk6zk4u2zqdxjzpm6asw.streamlit.app/)
---

## **Overview**

This dashboard connects marketing activity with business outcomes, providing insights into:

- Daily revenue, spend, and attributed revenue trends
- Channel performance comparison (Facebook, Google, TikTok)
- Campaign & tactic ROI drilldown
- Key performance indicators (KPIs) such as Orders, Revenue, ROAS, CAC, and Gross Margin
- Actionable insights based on data trends

It is designed for marketing analysts, managers, and business stakeholders to monitor campaign effectiveness in an interactive way.

---

## **Repository Structure**

```

Marketing\_Dashboard/
├── app.py                 # Main Streamlit app
├── requirements.txt       # Python dependencies
├── data/                  # Folder containing CSV files
│   ├── Facebook.csv
│   ├── Google.csv
│   ├── TikTok.csv
│   └── business.csv

````

---

## **Installation & Setup**

### **1. Clone the repository**
```bash
git clone <your-repo-link>
cd Marketing_Dashboard
````

### **2. Install dependencies**

It's recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows

pip install -r requirements.txt
```

### **3. Run the dashboard locally**

```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501` to view the dashboard.

---

## **Requirements**

Make sure the `requirements.txt` includes all the dependencies used in the app:

```
streamlit
pandas
plotly
numpy
```

*(Add any other libraries you may use in future updates.)*

---

## **Data Requirements**

Place your marketing and business CSV files inside the `data` folder:

* `Facebook.csv`, `Google.csv`, `TikTok.csv` — Marketing campaign data with columns like `date`, `clicks`, `impression`, `spend`, `attributed revenue`, `campaign`, `tactic`.
* `business.csv` — Business metrics with columns like `date`, `# of orders`, `# of new orders`, `new customers`, `total revenue`, `gross profit`, `COGS`.

> Make sure the CSV column names match those used in the app code.

---

## **Deployment**

You can deploy the dashboard easily on **Streamlit Community Cloud**:

1. Push the repo to GitHub.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and click **New App**.
3. Select your GitHub repository and branch.
4. Choose `app.py` as the main file and deploy.

> Make sure `requirements.txt` is up-to-date; Streamlit Cloud installs all dependencies from it.

---

## **Features**

* **Custom Sidebar:** Gradient background with white labels and input fields
* **Date & Channel Filters:** Dynamic filtering of data by date range and marketing channel
* **KPIs Overview:** Orders, Revenue, Marketing Spend, Attributed Revenue, ROAS, CAC
* **Trend Analysis:** Interactive line charts for revenue, spend, and attributed revenue
* **Channel Comparison:** Bar charts comparing spend vs attributed revenue across channels
* **Campaign Drilldown:** Bubble charts for ROI per campaign/tactic with impressions sizing
* **Insights Panel:** Actionable insights generated based on data trends

---

## **Credits**

Developed by **Sneha Sivakumar** — Powered by **Streamlit** and **Plotly**.

---
