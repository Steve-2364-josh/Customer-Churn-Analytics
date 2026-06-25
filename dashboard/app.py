import streamlit as st
import pandas as pd
import plotly.express as px

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Customer Churn Analytics",
    layout="wide"
)

# =========================
# TITLE
# =========================

st.title("🏦 Customer Segmentation & Churn Analytics")

# =========================
# LOAD DATA
# =========================

df = pd.read_csv("data/processed/segmented_bank_data.csv")

# =========================
# FILTERS
# =========================

st.sidebar.header("Filters")

selected_country = st.sidebar.multiselect(
    "Select Geography",
    options=df["Geography"].unique(),
    default=df["Geography"].unique()
)

selected_gender = st.sidebar.multiselect(
    "Select Gender",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

filtered_df = df[
    (df["Geography"].isin(selected_country)) &
    (df["Gender"].isin(selected_gender))
]

# =========================
# KPI CARDS
# =========================

total_customers = len(filtered_df)
churned_customers = filtered_df["Exited"].sum()
retained_customers = total_customers - churned_customers

if total_customers > 0:
    churn_rate = round(
        (churned_customers / total_customers) * 100,
        2
    )
else:
    churn_rate = 0

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Customers", int(total_customers))
col2.metric("Churned Customers", int(churned_customers))
col3.metric("Retained Customers", int(retained_customers))
col4.metric(
    "Churn Rate (%)",
    f"{churn_rate}%"
)

st.divider()

# =========================
# PIE CHART
# =========================

pie_data = pd.DataFrame({
    "Status": ["Retained", "Churned"],
    "Count": [retained_customers, churned_customers]
})

fig_pie = px.pie(
    pie_data,
    values="Count",
    names="Status",
    title="Customer Distribution"
)

st.plotly_chart(
    fig_pie,
    width="stretch"
)

st.divider()

# =========================
# DATASET
# =========================

st.subheader("📊 Filtered Dataset")

with st.expander("View Customer Data"):
    st.dataframe(
        filtered_df,
        width="stretch"
    )

st.write(f"Rows: {filtered_df.shape[0]}")

st.divider()

# =========================
# GEOGRAPHY CHART
# =========================

country_churn = (
    filtered_df
    .groupby("Geography")["Exited"]
    .mean() * 100
)

st.subheader("🌍 Geography-wise Churn Rate")

fig = px.bar(
    x=country_churn.index,
    y=country_churn.values,
    color=country_churn.values,
    title="Geography-wise Churn Rate",
    labels={
        "x": "Geography",
        "y": "Churn Rate (%)"
    }
)

fig.update_traces(
    texttemplate="%{y:.1f}%",
    textposition="outside"
)

fig.update_layout(title_font_size=22)

st.plotly_chart(
    fig,
    width="stretch"
)

st.divider()

# =========================
# AGE CHART
# =========================

age_churn = (
    filtered_df
    .groupby("AgeGroup", observed=True)["Exited"]
    .mean() * 100
)

st.subheader("👥 Age-wise Churn Rate")

fig_age = px.bar(
    x=age_churn.index,
    y=age_churn.values,
    color=age_churn.values,
    title="Age-wise Churn Rate",
    labels={
        "x": "Age Group",
        "y": "Churn Rate (%)"
    }
)

fig_age.update_traces(
    texttemplate="%{y:.1f}%",
    textposition="outside"
)

fig_age.update_layout(title_font_size=22)

st.plotly_chart(
    fig_age,
    width="stretch"
)

st.divider()

# =========================
# TENURE CHURN RATE
# =========================

tenure_churn = (
    filtered_df
    .groupby("TenureGroup")["Exited"]
    .mean() * 100
)

st.subheader("📅 Tenure-wise Churn Rate")

fig_tenure = px.bar(
    x=tenure_churn.index,
    y=tenure_churn.values,
    title="Tenure-wise Churn Rate",
    labels={
        "x": "Tenure Group",
        "y": "Churn Rate (%)"
    },
    color=tenure_churn.values
)

fig_tenure.update_traces(
    texttemplate="%{y:.1f}%",
    textposition="outside"
)

fig_tenure.update_layout(
    title_font_size=22
)

st.plotly_chart(
    fig_tenure,
    width="stretch"
)

st.divider()

# =========================
# CREDIT SCORE CHURN
# =========================

credit_churn = (
    filtered_df
    .groupby("CreditScoreBand")["Exited"]
    .mean() * 100
)

st.subheader("💳 Credit Score Band Churn")

fig_credit = px.bar(
    x=credit_churn.index,
    y=credit_churn.values,
    title="Credit Score Band Churn",
    labels={
        "x": "Credit Score Band",
        "y": "Churn Rate (%)"
    },
    color=credit_churn.values
)

fig_credit.update_traces(
    texttemplate="%{y:.1f}%",
    textposition="outside"
)

fig_credit.update_layout(
    title_font_size=22
)

st.plotly_chart(
    fig_credit,
    width="stretch"
)

st.divider()

# =========================
# GENDER CHURN RATE
# =========================

gender_churn = (
    filtered_df
    .groupby("Gender")["Exited"]
    .mean() * 100
)

st.subheader("👨👩 Gender-wise Churn Rate")

fig_gender = px.bar(
    x=gender_churn.index,
    y=gender_churn.values,
    title="Gender-wise Churn Rate",
    labels={
        "x": "Gender",
        "y": "Churn Rate (%)"
    },
    color=gender_churn.values
)

fig_gender.update_traces(
    texttemplate="%{y:.1f}%",
    textposition="outside"
)

fig_gender.update_layout(
    title_font_size=22
)

st.plotly_chart(
    fig_gender,
    width="stretch"
)

st.divider()

# =========================
# ENGAGEMENT CHURN
# =========================

engagement_churn = (
    filtered_df
    .groupby("IsActiveMember")["Exited"]
    .mean() * 100
)

engagement_churn.index = [
    "Inactive",
    "Active"
]

st.subheader("📉 Active vs Inactive Member Churn")

fig_engagement = px.bar(
    x=engagement_churn.index,
    y=engagement_churn.values,
    title="Active vs Inactive Member Churn",
    labels={
        "x": "Membership Status",
        "y": "Churn Rate (%)"
    },
    color=engagement_churn.values
)

fig_engagement.update_traces(
    texttemplate="%{y:.1f}%",
    textposition="outside"
)

fig_engagement.update_layout(
    title_font_size=22
)

st.plotly_chart(
    fig_engagement,
    width="stretch"
)

st.divider()

# =========================
# BALANCE CHART
# =========================

balance_churn = (
    filtered_df
    .groupby("BalanceSegment")["Exited"]
    .mean() * 100
)

st.subheader("💰 Balance Segment Churn")

fig_balance = px.bar(
    x=balance_churn.index,
    y=balance_churn.values,
    color=balance_churn.values,
    title="Balance Segment Churn",
    labels={
        "x": "Balance Segment",
        "y": "Churn Rate (%)"
    }
)

fig_balance.update_traces(
    texttemplate="%{y:.1f}%",
    textposition="outside"
)

fig_balance.update_layout(title_font_size=22)

st.plotly_chart(
    fig_balance,
    width="stretch"
)

st.divider()

# =========================
# HIGH VALUE CUSTOMER ANALYSIS
# =========================

high_value = filtered_df[
    filtered_df["Balance"] >= 100000
]

if len(high_value) > 0:
    hv_count = len(high_value)

    hv_churn = round(
        high_value["Exited"].mean() * 100,
        2
    )
else:
    hv_count = 0
    hv_churn = 0

st.subheader("💎 High Value Customer Analysis")

col1, col2 = st.columns(2)

col1.metric(
    "High Value Customers",
    int(hv_count)
)

col2.metric(
    "High Value Customer Churn Rate (%)",
    f"{hv_churn}%"
)

st.divider()

# =========================
# INSIGHT MESSAGE
# =========================

st.success(
    f"📌 High Value Customers have a churn rate of {hv_churn}%."
)

st.divider()

# =========================
# FOOTER
# =========================

st.caption(
    "Customer Segmentation & Churn Analytics Dashboard | Internship Project"
)
