
import streamlit as st
import pandas as pd
import plotly.express as px

# Page setup
st.set_page_config(
    page_title="Retail Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("📈 Retail Sales Analytics Dashboard")
st.markdown("---")

# Load data
@st.cache_data
def load_data():
    monthly = pd.read_csv("monthly_revenue.csv")
    yearly = pd.read_csv("yearly_revenue.csv")
    return monthly, yearly

monthly, yearly = load_data()

# Convert dates
monthly['Month'] = pd.to_datetime(monthly['Month'])
yearly['Year'] = pd.to_datetime(yearly['Year'])

# 1. KEY METRICS
st.subheader("📊 Key Performance Indicators")
col1, col2, col3, col4 = st.columns(4)

with col1:
    total_rev = monthly['Revenue'].sum()
    st.metric("Total Revenue", f"${total_rev:,.0f}")

with col2:
    avg_monthly = monthly['Revenue'].mean()
    st.metric("Average Monthly", f"${avg_monthly:,.0f}")

with col3:
    best_month = monthly.loc[monthly['Revenue'].idxmax()]
    st.metric("Best Month", f"${best_month['Revenue']:,.0f}")

with col4:
    st.metric("Data Points", f"{len(monthly)} months")

st.markdown("---")

# 2. CHARTS
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("📅 Monthly Revenue Trend")
    fig1 = px.line(
        monthly, 
        x='Month', 
        y='Revenue',
        markers=True,
        line_shape='spline'
    )
    fig1.update_layout(height=400)
    st.plotly_chart(fig1, use_container_width=True)

with col_right:
    st.subheader("📆 Yearly Revenue")
    fig2 = px.bar(
        yearly,
        x='Year',
        y='Revenue',
        color='Revenue',
        color_continuous_scale='viridis'
    )
    fig2.update_layout(height=400)
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

# 3. DATA TABLES
st.subheader("📋 Raw Data")

tab1, tab2 = st.tabs(["Monthly Data", "Yearly Data"])

with tab1:
    st.dataframe(
        monthly.sort_values('Month', ascending=False),
        use_container_width=True
    )

with tab2:
    st.dataframe(
        yearly.sort_values('Year', ascending=False),
        use_container_width=True
    )

# Footer
st.markdown("---")
st.success("✅ Dashboard loaded successfully!")
st.caption("Created with Streamlit | Data: Online Retail Dataset")
