import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import date


# Inject custom CSS for sidebar background color (ocean blue)
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%) !important;
    }
    /* Sidebar headings and labels */
    [data-testid="stSidebar"] .stMarkdown p,
    [data-testid="stSidebar"] .st-emotion-cache-1xw8zd0,
    [data-testid="stSidebar"] label {
        color: white !important;
    }
    /* Make the sidebar header (title "Filters") and collapse arrow white */
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] h4,
    [data-testid="stSidebar"] h5,
    [data-testid="stSidebar"] h6,
    [data-testid="stSidebar"] .stSidebarHeader,
    [data-testid="stSidebar"] .st-emotion-cache-18ni7ap {
        color: white !important;
        fill: white !important;
    }
    /* Collapsible arrow (SVG) */
    [data-testid="collapsedControl"] svg {
        color: white !important;
        fill: white !important;
    }
    /* Prevent white text inside input widgets */
    [data-testid="stSidebar"] .stSelectbox div[role="combobox"], 
    [data-testid="stSidebar"] input, 
    [data-testid="stSidebar"] .stDateInput input {
        color: black !important;
        background: white !important;
    }
    </style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="Marketing Intelligence Dashboard", layout="wide", initial_sidebar_state="expanded")

# ---- DATA LOADING ----
@st.cache_data
def load_data():
    fb = pd.read_csv("data/Facebook.csv", parse_dates=['date'])
    fb['channel'] = 'Facebook'
    gg = pd.read_csv("data/Google.csv", parse_dates=['date'])
    gg['channel'] = 'Google'
    tk = pd.read_csv("data/TikTok.csv", parse_dates=['date'])
    tk['channel'] = 'TikTok'
    mkt = pd.concat([fb, gg, tk], ignore_index=True)
    biz = pd.read_csv("data/business.csv", parse_dates=['date'])
    # Clean column names for consistency
    biz.columns = biz.columns.str.strip()
    biz = biz.rename(columns={
        '# of orders': 'orders',
        '# of new orders': 'new_orders',
        'new customers': 'new_customers',
        'total revenue': 'total_revenue',
        'gross profit': 'gross_profit',
        'COGS': 'cogs'
    })
    # Ensure all 'date' columns are datetime.date (not datetime64)
    biz['date'] = pd.to_datetime(biz['date']).dt.date
    mkt['date'] = pd.to_datetime(mkt['date']).dt.date
    return mkt, biz

mkt, biz = load_data()

# ---- DATA PREPARATION ----
mkt.fillna(0, inplace=True)
biz.fillna(0, inplace=True)

mkt['CTR'] = mkt['clicks'] / mkt['impression'].replace(0, 1)
mkt['CPC'] = mkt['spend'] / mkt['clicks'].replace(0, 1)
mkt['ROAS'] = mkt['attributed revenue'] / mkt['spend'].replace(0, 1)

mkt_daily = mkt.groupby(['date', 'channel']).agg({
    'impression': 'sum', 'clicks': 'sum', 'spend': 'sum', 'attributed revenue': 'sum'
}).reset_index()
mkt_daily['CTR'] = mkt_daily['clicks'] / mkt_daily['impression'].replace(0, 1)
mkt_daily['ROAS'] = mkt_daily['attributed revenue'] / mkt_daily['spend'].replace(0, 1)
mkt_daily['date'] = pd.to_datetime(mkt_daily['date']).dt.date

# Merge with business
summary = pd.merge(
    biz,
    mkt_daily.groupby('date').agg({
        'spend': 'sum',
        'attributed revenue': 'sum'
    }).reset_index(),
    on='date', how='left'
)
summary['spend'] = summary['spend'].fillna(0)
summary['attributed revenue'] = summary['attributed revenue'].fillna(0)
summary['CAC'] = summary['spend'] / summary['new_customers'].replace(0, 1)
summary['ROAS'] = summary['attributed revenue'] / summary['spend'].replace(0, 1)
summary['Gross Margin'] = summary['gross_profit'] / summary['total_revenue'].replace(0, 1)
summary['date'] = pd.to_datetime(summary['date']).dt.date

# ---- SIDEBAR: Set correct min/max dates for selector ----
min_date = summary['date'].min()
max_date = summary['date'].max()

st.sidebar.title("Filters")
date_range = st.sidebar.date_input(
    "Select Date Range",
    [min_date, max_date],
    min_value=min_date,
    max_value=max_date
)
channel_options = ["All", "Facebook", "Google", "TikTok"]
channel = st.sidebar.selectbox("Marketing Channel", channel_options)

# ---- DATE FILTERING ----
if date_range and len(date_range) == 2:
    start_date, end_date = date_range
    summary = summary[(summary['date'] >= start_date) & (summary['date'] <= end_date)]
    mkt_daily = mkt_daily[(mkt_daily['date'] >= start_date) & (mkt_daily['date'] <= end_date)]
    mkt = mkt[(mkt['date'] >= start_date) & (mkt['date'] <= end_date)]

if channel != "All":
    mkt_daily = mkt_daily[mkt_daily['channel'] == channel]
    mkt = mkt[mkt['channel'] == channel]

# ---- HEADER ----
st.title("🌟 Marketing Intelligence Dashboard")
st.markdown("#### Insight-driven dashboard to connect marketing activity with business outcomes.")

# ---- KPIs ----
col1, col2, col3, col4, col5, col6 = st.columns(6)
col1.metric("Orders", int(summary['orders'].sum()))
col2.metric("Revenue", f"${summary['total_revenue'].sum():,.0f}")
col3.metric("Marketing Spend", f"${summary['spend'].sum():,.0f}")
col4.metric("Attributed Revenue", f"${summary['attributed revenue'].sum():,.0f}")
col5.metric("ROAS", f"{summary['ROAS'].mean():.2f}x")
col6.metric("CAC", f"${summary['CAC'].mean():.2f}")

st.markdown("---")

# ---- TRENDS ----
st.subheader("📈 Daily Trends")
trends_fig = go.Figure()
trends_fig.add_trace(go.Scatter(x=summary['date'], y=summary['total_revenue'], name='Total Revenue', line=dict(color='green')))
trends_fig.add_trace(go.Scatter(x=summary['date'], y=summary['spend'], name='Marketing Spend', line=dict(color='blue')))
trends_fig.add_trace(go.Scatter(x=summary['date'], y=summary['attributed revenue'], name='Attributed Revenue', line=dict(color='orange')))
trends_fig.update_layout(legend=dict(orientation="h"), margin=dict(l=20,r=20,t=30,b=20), height=350)
st.plotly_chart(trends_fig, use_container_width=True)

# ---- CHANNEL COMPARISON ----
st.subheader("📊 Channel Comparison")
ch_cmp = mkt_daily.groupby('channel').agg({
    'spend': 'sum',
    'attributed revenue': 'sum',
    'ROAS': 'mean',
    'CTR': 'mean'
}).reset_index()
fig_cmp = px.bar(ch_cmp, x='channel', y=['spend', 'attributed revenue'], barmode='group', title="Spend vs Attributed Revenue by Channel", color_discrete_sequence=px.colors.qualitative.Set1)
st.plotly_chart(fig_cmp, use_container_width=True)
st.dataframe(ch_cmp.set_index('channel'))

# ---- CAMPAIGN/Tactic Drilldown ----
st.subheader("🔎 Campaign & Tactic Explorer")
if channel != "All":
    campaigns = mkt['campaign'].unique()
    selected_campaign = st.selectbox("Select Campaign", ["All"] + list(campaigns))
    if selected_campaign != "All":
        drill = mkt[mkt['campaign'] == selected_campaign]
    else:
        drill = mkt
else:
    drill = mkt

if not drill.empty:
    fig_drill = px.scatter(
        drill, x='spend', y='attributed revenue', color='tactic',
        size='impression', hover_data=['campaign', 'date'],
        title="Campaign/Tactic ROI (Bubble = Impressions)"
    )
    st.plotly_chart(fig_drill, use_container_width=True)
    st.dataframe(drill[['date','channel','campaign','tactic','impression','clicks','spend','attributed revenue','CTR','ROAS']].sort_values(by='date', ascending=False).head(50))

# ---- INSIGHT PANEL ----
st.markdown("## 🧠 Insights")
insight = ""

# Only compare across channels if more than one channel is shown
if channel == "All" and not ch_cmp.empty and len(ch_cmp) > 1:
    best_channel = ch_cmp.sort_values('ROAS', ascending=False).iloc[0]
    insight += f"- **{best_channel['channel']}** is currently the most efficient channel (highest ROAS: {best_channel['ROAS']:.2f}x).\n"
elif channel != "All" and not ch_cmp.empty and len(ch_cmp) == 1:
    this_ch = ch_cmp.iloc[0]
    insight += f"- The average ROAS for **{channel}** is {this_ch['ROAS']:.2f}x.\n"

if not summary.empty and summary['CAC'].mean() < 20:
    insight += f"- Customer Acquisition Cost (CAC) is healthy at **${summary['CAC'].mean():.2f}**.\n"
if not summary.empty and len(summary) >= 7 and trends_fig.data[0].y[-1] > trends_fig.data[0].y[-7]:
    insight += "- Revenue is trending upwards in the last week! 📈\n"
if not insight:
    insight = "Explore the dashboard for actionable insights!"

st.info(insight)

st.markdown("---")
st.markdown("© Sneha Sivakumar — Powered by Streamlit + Plotly")
