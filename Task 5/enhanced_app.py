
import pandas as pd
import streamlit as st
import plotly.express as px

# Apply custom page config
st.set_page_config(page_title="Global Superstore Dashboard", layout="wide", page_icon="📈")

# Load data
df = pd.read_csv("superstore_clean.csv")

# Apply dark theme
st.markdown(
    """
    <style>
        .main {
            background-color: #111111;
            color: #FAFAFA;
        }
        .stApp {
            background-color: #111111;
        }
        .css-18e3th9 {
            background-color: #111111;
        }
        .css-1d391kg {
            color: #FAFAFA;
        }
        .css-1cpxqw2 {
            color: #FAFAFA;
        }
        .st-c6 {
            color: #FAFAFA;
        }
        .st-bz {
            color: #FAFAFA;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar filters
st.sidebar.title("🔍 Filters")
region = st.sidebar.multiselect("🌍 Select Region", options=df['Region'].unique(), default=df['Region'].unique())
category = st.sidebar.multiselect("📦 Select Category", options=df['Category'].unique(), default=df['Category'].unique())
sub_category = st.sidebar.multiselect("🧱 Select Sub-Category", options=df['Sub-Category'].unique(), default=df['Sub-Category'].unique())

# Filter data
df_filtered = df[
    (df['Region'].isin(region)) &
    (df['Category'].isin(category)) &
    (df['Sub-Category'].isin(sub_category))
]

# Title
st.title("📊 Global Superstore Sales Dashboard")
st.markdown("### 💼 Track sales, profit, and customer performance interactively")

# KPIs
total_sales = df_filtered['Sales'].sum()
total_profit = df_filtered['Profit'].sum()
top_customers = df_filtered.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).head(5)

col1, col2, col3 = st.columns([1, 1, 2])
col1.metric("💰 Total Sales", f"${total_sales:,.2f}")
col2.metric("📈 Total Profit", f"${total_profit:,.2f}")
col3.markdown("**🔝 Top 5 Customers by Sales**")
col3.dataframe(top_customers.reset_index().rename(columns={'Customer Name': 'Customer', 'Sales': 'Total Sales'}))

# Charts
st.markdown("---")
col4, col5 = st.columns(2)

with col4:
    st.subheader("🪟 Sales by Category")
    fig1 = px.bar(df_filtered.groupby('Category')['Sales'].sum().reset_index(), 
                  x='Category', y='Sales', color='Category', template='plotly_dark')
    st.plotly_chart(fig1, use_container_width=True)

with col5:
    st.subheader("📍 Profit Distribution by Region")
    fig2 = px.pie(df_filtered, names='Region', values='Profit', template='plotly_dark')
    st.plotly_chart(fig2, use_container_width=True)

# Bottom chart
st.markdown("### 🚀 Sales by Sub-Category")
fig3 = px.bar(df_filtered.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False).reset_index(),
              x='Sub-Category', y='Sales', color='Sales', template='plotly_dark')
st.plotly_chart(fig3, use_container_width=True)
