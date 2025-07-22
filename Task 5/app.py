
import pandas as pd
import streamlit as st
import plotly.express as px

# Load Data
df = pd.read_csv("superstore_clean.csv")

# Sidebar Filters
st.sidebar.title("Filters")
region = st.sidebar.multiselect("Select Region", options=df['Region'].unique(), default=df['Region'].unique())
category = st.sidebar.multiselect("Select Category", options=df['Category'].unique(), default=df['Category'].unique())
sub_category = st.sidebar.multiselect("Select Sub-Category", options=df['Sub-Category'].unique(), default=df['Sub-Category'].unique())

# Apply Filters
df_filtered = df[
    (df['Region'].isin(region)) &
    (df['Category'].isin(category)) &
    (df['Sub-Category'].isin(sub_category))
]

# Title
st.title("📊 Global Superstore Sales Dashboard")

# KPIs
total_sales = df_filtered['Sales'].sum()
total_profit = df_filtered['Profit'].sum()
top_customers = df_filtered.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).head(5)

col1, col2 = st.columns(2)
col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")

# Charts
st.subheader("Sales by Category")
fig1 = px.bar(df_filtered.groupby('Category')['Sales'].sum().reset_index(), x='Category', y='Sales')
st.plotly_chart(fig1)

st.subheader("Profit by Region")
fig2 = px.pie(df_filtered, names='Region', values='Profit', title='Profit Distribution by Region')
st.plotly_chart(fig2)

st.subheader("Top 5 Customers by Sales")
fig3 = px.bar(top_customers.reset_index(), x='Customer Name', y='Sales', color='Sales')
st.plotly_chart(fig3)
