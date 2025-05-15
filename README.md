# Telco Customer Churn – Data Analysis Project
📘 Overview

This project is a Jupyter Notebook-based exploratory data analysis (EDA) using the Telco Customer Churn dataset from Kaggle. The goal is to understand customer behavior and identify key factors associated with customer churn through visualization and statistical analysis.

The notebook performs:

- Loading and preparing the Telco dataset
- Cleaning missing or inconsistent data
- Visualizing customer patterns and correlations with churn
- Summarizing key statistics and findings

🛠️ Installation

System Requirements

- Hardware:
  - Minimum 4GB RAM (8GB+ recommended)
  - Any modern processor

- Software:
  - Python 3.7 or newer
  - Jupyter Notebook or JupyterLab environment

Required Python Libraries

You need to install the following libraries:
 - pandas
 - numpy
 - matplotlib
 - seaborn
 - plotly
 - scikit-learn
 - xgboost
   
Install them via pip:

pip install pandas numpy matplotlib seaborn plotly scikit-learn xgboost

If Jupyter Notebook is not installed:

pip install notebook

⚙️ Configuration Instructions

1- Download the dataset from Kaggle:
 - Link: https://www.kaggle.com/datasets/blastchar/telco-customer-churn
 - File name: WA_Fn-UseC_-Telco-Customer-Churn.csv

2- Place the dataset in the same folder as your notebook or update the file path in the code.

🚀 How to Run the Project

To run the notebook locally:

1- Open your terminal or Anaconda prompt.

2- Navigate to the folder where the notebook is located.

3- Launch Jupyter Notebook:

jupyter notebook

4- Open nb2.2.ipynb in your browser.

5- Run all cells in sequence to follow the analysis.

📂 Files Included

- nb2.2.ipynb: The main Jupyter Notebook containing the analysis
- WA_Fn-UseC_-Telco-Customer-Churn.csv: The dataset used
- README.txt: Project documentation (this file)

📊 Dataset Information

- Name: Telco Customer Churn
- Source: IBM Sample Data via Kaggle
- Link: https://www.kaggle.com/datasets/blastchar/telco-customer-churn
- File Type: CSV
- Size: Approximately 139 KB
- Target Variable: Churn (Yes/No)

🧠 Machine Learning Model Development and Optimization

- Applied multiple classifiers:

  - Logistic Regression
  - Support Vector Machine (SVM)
  - Random Forest
  - XGBoost

- Used train_test_split with stratification for fair model training
- Performed hyperparameter tuning with GridSearchCV and cross-validation
- Evaluated models using:

  - Accuracy
  - Recall
  - F1-score
  - ROC-AUC

- Selected the best-performing model based on recall (to catch churners)

🚀 Model Deployment

- Serialized the trained model using pickle for reuse
- Ready for integration into:

  - Web application (Flask/Streamlit)
  - Business Intelligence Dashboard

- Can accept new customer data and return churn predictions
- Example deployment steps (if Flask used):

  1- Load model with pickle

  2- Create an API endpoint (/predict)

  3- Accept JSON input and return prediction

📄 License

This project is an open source project made by DEPI students. The dataset is publicly available on Kaggle and subject to its terms of use.

🙌 Credits

- Dataset: IBM Telco Customer Churn (via Kaggle)
- Tools used: Python, pandas, numpy, matplotlib, seaborn
- Developed as part of a data analysis learning project for DEPI by:
  - Abdelrahman Elsayed
  - Abdelrahman Mohamed
  - Ahmed Mohamed
  - Amr Khaled
  - Kyrillos Nabil
  - Ramy Kamel
