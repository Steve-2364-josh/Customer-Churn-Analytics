# Customer Segmentation and Churn Analytics in European Banking

## Abstract

Customer churn remains a major challenge in the banking industry. This study analyzes customer churn using segmentation-based analytics and machine learning techniques to identify patterns across demographic, geographic, and financial characteristics.

## Introduction

Banks lose significant revenue when customers discontinue their services. Understanding customer behavior through segmentation can help organizations develop targeted retention strategies.

## Dataset Description

The dataset contains 10,000 customer records with the following attributes:

* Credit Score
* Geography
* Gender
* Age
* Tenure
* Balance
* Number of Products
* Credit Card Ownership
* Activity Status
* Estimated Salary
* Churn Status

## Data Preparation

The following preprocessing steps were performed:

* Removal of non-essential fields
* Validation of missing values
* Creation of Age Groups
* Creation of Credit Score Bands
* Creation of Tenure Groups
* Creation of Balance Segments

## Methodology

### Customer Segmentation

Segments were created based on:

* Geography
* Age
* Credit Score
* Tenure
* Balance

### Churn Analysis

Segment-wise churn rates were calculated using:

Churn Rate = (Churned Customers / Total Customers) × 100

### Predictive Modeling

A Logistic Regression model was trained using:

* Credit Score
* Age
* Tenure
* Balance
* Number of Products
* Activity Status
* Encoded Geography
* Encoded Gender

## Results

### Overall Churn

* Churn Rate: 20.37%

### Model Performance

* Accuracy: 81.4%

### Major Observations

* Germany exhibits the highest churn rate.
* Inactive members are more likely to churn.
* Customers with high balances contribute higher revenue risk.
* Older customers show greater churn tendencies.

## Conclusion

Segmentation-driven analytics successfully identified customer groups with elevated churn risk. The developed dashboard enables stakeholders to monitor churn trends and make informed retention decisions.
