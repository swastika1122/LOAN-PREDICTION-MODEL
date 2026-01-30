# 🏦 Loan Approval Prediction using Machine Learning

## 📌 Problem Statement
Banks receive many loan applications daily.  
The objective of this project is to predict whether a loan will be **approved or rejected**
based on applicant details such as income, credit history, education, and loan amount
using Machine Learning techniques.

This is a **binary classification problem**:
- 1 → Loan Approved  
- 0 → Loan Rejected  

---

## 📊 Dataset
- Source: Kaggle – Loan Prediction Dataset
- Files used: `train.csv`
- Each row represents one loan applicant.

### Key Features:
- Gender
- Married
- Dependents
- Education
- ApplicantIncome
- CoapplicantIncome
- LoanAmount
- Credit_History
- Property_Area

Target Variable:
- `Loan_Status`

---

## 🛠️ Technologies Used
- Python
- Google Colab
- Pandas & NumPy
- Matplotlib & Seaborn
- Scikit-learn

---

## 🔍 Project Workflow

### 1️⃣ Data Loading & Understanding
- Loaded dataset using Pandas
- Checked shape, data types, and missing values

### 2️⃣ Exploratory Data Analysis (EDA)
- Univariate analysis on numerical and categorical features
- Bivariate analysis between Credit History and Loan Status
- Identified important patterns and class distribution

### 3️⃣ Data Preprocessing
- Handled missing values:
  - Categorical → Mode
  - Numerical → Median
- Removed unnecessary columns
- Converted categorical variables using Label Encoding

### 4️⃣ Feature Engineering
- Applied log transformation to reduce skewness in:
  - ApplicantIncome
  - LoanAmount

### 5️⃣ Model Building
- Split data into training and testing sets (80:20)
- Trained multiple models:
  - Logistic Regression
  - Random Forest Classifier

### 6️⃣ Model Evaluation
- Evaluated models using:
  - Accuracy Score
  - Confusion Matrix
  - Classification Report
- Compared performance of both models

---

## ✅ Results
- Random Forest performed better than Logistic Regression
- Credit_History was identified as the most important feature
- The model successfully predicts loan approval status

---

## 📈 Key Insights
- Applicants with good credit history have a higher chance of loan approval
- Feature engineering improves model performance
- Ensemble models perform better for this dataset

---

## ▶️ How to Run the Project
1. Open the notebook in Google Colab or Jupyter Notebook
2. Upload `train.csv`
3. Run cells sequentially
4. View results and visualizations

---

## 🎯 Learning Outcomes
- Hands-on experience with EDA
- Understanding of feature engineering
- Practical implementation of classification algorithms
- End-to-end ML project workflow

---

## 👩‍💻 Author
**Swastika Dandapat*
Machine Learning Enthusiast

---

⭐ If you like this project, feel free to star the repository!
