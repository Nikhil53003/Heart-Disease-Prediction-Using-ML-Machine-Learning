# ❤️ Heart Disease Prediction Using Machine Learning
This project aims to predict the presence of heart disease in patients using machine learning techniques. It utilizes patient data and applies various classification algorithms to determine whether or not a patient is likely to have heart disease.

# 📌 Project Overview
Heart disease is a leading cause of death globally. Early diagnosis can help in effective treatment. This project uses a machine learning model trained on a dataset containing medical parameters to predict the likelihood of heart disease.

# 📁 Dataset
  The dataset used includes the following features:
  * Age
  * Sex
  * Chest pain type (cp)
  * Resting blood pressure (trestbps)
  * Serum cholesterol (chol)
  * Fasting blood sugar (fbs)
  * Resting electrocardiographic results (restecg)
  * Maximum heart rate achieved (thalach)
  * Exercise induced angina (exang)
  * ST depression induced by exercise (oldpeak)
  * The slope of the peak exercise ST segment (slope)
  * Number of major vessels colored by fluoroscopy (ca)
  * Thalassemia (thal)
  * Target (0 = No heart disease, 1 = Heart disease)

# 🔍 Exploratory Data Analysis (EDA)
  * Visualized distributions of numeric and categorical features
  * Checked for missing values and data imbalances
  * Explored correlations using heatmaps

# 🛠️ Preprocessing
  * Encoded categorical variables
  * Standardized numerical features
  * Split dataset into training and test sets

# 🤖 Models Used
  * Logistic Regression
  * K-Nearest Neighbors (KNN)
  * Decision Tree
  * Random Forest
  * Support Vector Machine (SVM)
  * Naive Bayes

# 📊 Evaluation Metrics
Each model was evaluated using:
  * Accuracy
  * Precision
  * Recall
  * F1 Score
  * Confusion Matrix

# ✅ Best Performing Model
Based on the results, [insert best model here] achieved the highest accuracy on the test data.

# 📦 Requirements
Install dependencies using:

bash
Copy
Edit
pip install -r requirements.txt
Typical libraries used:

pandas

numpy

matplotlib

seaborn

scikit-learn

# 🚀 How to Run
Clone this repository

Open the Jupyter Notebook: Heart Disease Prediction Using ML.ipynb

Run each cell sequentially

# 📈 Future Improvements
Hyperparameter tuning using GridSearchCV

Deployment via Flask or Streamlit

Using more advanced ML techniques or deep learning
