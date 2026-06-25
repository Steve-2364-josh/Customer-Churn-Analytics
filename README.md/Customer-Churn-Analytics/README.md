# 🏦 Customer Segmentation & Churn Analytics

## Executive Summary

Customer churn is one of the most significant challenges in the banking industry. Retaining existing customers is substantially more cost-effective than acquiring new ones, making churn analysis a critical business function.

This project provides a segmentation-driven analysis of customer churn using customer demographic, financial, and engagement data. Through exploratory data analysis, customer segmentation, and predictive modeling, the project identifies high-risk customer groups and uncovers patterns that can support targeted retention strategies.

An interactive Streamlit dashboard was developed to enable business users to explore churn behavior dynamically across different customer segments.

---

# Business Problem

Retail banks often monitor overall churn rates but lack detailed insights into:

* Which customer groups are most likely to leave
* How churn differs across geographic regions
* The relationship between customer engagement and churn
* Whether high-value customers are contributing disproportionately to revenue loss

Without segmentation-based analytics, retention efforts become reactive rather than strategic.

This project addresses these challenges by analyzing churn across multiple customer dimensions and presenting findings through an interactive dashboard.

---

# Project Objectives

## Primary Objectives

* Measure overall customer churn rate
* Analyze churn behavior across customer segments
* Compare churn patterns across European regions

## Secondary Objectives

* Identify high-value customer churn trends
* Evaluate customer engagement and tenure patterns
* Support data-driven customer retention strategies

---

# Dataset Overview

The dataset contains information for **10,000 banking customers**.

### Features

| Feature         | Description                       |
| --------------- | --------------------------------- |
| CreditScore     | Customer creditworthiness score   |
| Geography       | France, Germany, Spain            |
| Gender          | Male / Female                     |
| Age             | Customer age                      |
| Tenure          | Years with the bank               |
| Balance         | Account balance                   |
| NumOfProducts   | Number of bank products           |
| HasCrCard       | Credit card ownership             |
| IsActiveMember  | Customer activity status          |
| EstimatedSalary | Estimated annual salary           |
| Exited          | Churn indicator (Target Variable) |

### Engineered Features

To enhance segmentation analysis, the following derived features were created:

* AgeGroup
* CreditScoreBand
* TenureGroup
* BalanceSegment

---

# Technology Stack

### Programming & Analytics

* Python
* Pandas
* NumPy

### Data Visualization

* Plotly
* Matplotlib

### Machine Learning

* Scikit-Learn

### Dashboard Development

* Streamlit

### Version Control

* Git
* GitHub

---

# Project Workflow

## 1. Data Cleaning

Performed:

* Missing value validation
* Duplicate record verification
* Data consistency checks
* Removal of non-analytical attributes

## 2. Feature Engineering

Created segmentation variables:

* Age Groups
* Credit Score Bands
* Tenure Categories
* Balance Segments

## 3. Exploratory Data Analysis

Conducted detailed churn analysis across:

* Geography
* Age Groups
* Gender
* Tenure
* Credit Score Bands
* Customer Activity Status
* Balance Segments

## 4. Machine Learning

Implemented Logistic Regression for churn prediction.

Workflow:

1. Feature Selection
2. One-Hot Encoding
3. Train-Test Split (80:20)
4. Model Training
5. Performance Evaluation

---

# Key Performance Indicators

| KPI                | Value  |
| ------------------ | ------ |
| Total Customers    | 10,000 |
| Churned Customers  | 2,037  |
| Overall Churn Rate | 20.37% |

---

# Machine Learning Results

## Logistic Regression Performance

### Accuracy

81.4%

### Confusion Matrix

```text
[[1540   67]
 [ 305   88]]
```

### Classification Metrics

| Metric    | Churn Class |
| --------- | ----------- |
| Precision | 0.57        |
| Recall    | 0.22        |
| F1-Score  | 0.32        |

The model achieved strong overall accuracy but demonstrated lower recall for churned customers, indicating opportunities for future improvement using advanced machine learning techniques.

---

# Interactive Dashboard

A Streamlit dashboard was developed to provide business-friendly exploration of customer churn patterns.

## Dashboard Features

### Interactive Filters

* Geography
* Gender

### KPI Cards

* Total Customers
* Churned Customers
* Retained Customers
* Churn Rate

### Visual Analytics

* Customer Distribution
* Geography-wise Churn Rate
* Age-wise Churn Rate
* Tenure-wise Churn Rate
* Credit Score Band Churn
* Gender-wise Churn Rate
* Active vs Inactive Member Churn
* Balance Segment Churn
* High-Value Customer Churn Analysis

---

# Dashboard Screenshots

## Dashboard Overview

![Dashboard Home](screenshots/dashboard_home.png)

## Customer Dataset View

![Dataset](screenshots/dataset.png)

## Geography-wise Churn Analysis

![Geography Churn](screenshots/geography_churn.png)

## Age-wise Churn Analysis

![Age Churn](screenshots/age_churn.png)

## Tenure-wise Churn Analysis

![Tenure Churn](screenshots/tenure_churn.png)

---

# Key Business Insights

* Overall customer churn rate is 20.37%.
* Customer churn varies significantly across geographic regions.
* Inactive customers exhibit substantially higher churn rates.
* Certain age groups are more prone to churn than others.
* High-value customers contribute significantly to potential revenue loss.
* Customer engagement emerges as a major retention indicator.

---

# Project Structure

```text
Customer-Churn-Analytics
│
├── dashboard
│   └── app.py
│
├── data
│   └── processed
│
├── notebooks
│   ├── 01_data_cleaning.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_churn_analysis.ipynb
│   └── 04_logistic_regression.ipynb
│
├── screenshots
│
├── README.md
└── requirements.txt
```

---

# Installation & Usage

### Clone Repository

```bash
git clone <repository-url>
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Launch Dashboard

```bash
streamlit run dashboard/app.py
```

---

# Author

**Steve Joshua T**

Customer Segmentation & Churn Analytics Project

Developed as part of a Data Analytics Internship focused on customer behavior analysis, churn segmentation, and business intelligence reporting.
