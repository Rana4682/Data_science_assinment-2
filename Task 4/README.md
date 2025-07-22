# Loan Default Risk Prediction with Business Cost Optimization

This project predicts the likelihood of a loan default using binary classification and applies cost-based optimization to improve decision-making from a business perspective.

##  Objective
- Predict loan default risk using classification models
- Minimize total business cost by optimizing decision threshold

## 📁 Dataset
- **Home Credit Default Risk Dataset**
- Includes customer demographic, credit, and loan application data

##  Step-by-Step Workflow

1. **Data Cleaning & Preprocessing**
   - Handle missing values
   - Encode categorical features
   - Feature engineering

2. **Model Training**
   - Logistic Regression
   - CatBoost Classifier

3. **Business Cost Optimization**
   - Define cost of False Positives (FP) and False Negatives (FN)
   - Tune classification threshold to minimize total cost

4. **Evaluation**
   - Confusion Matrix, ROC Curve, F1-score
   - Cost-based metrics (Expected Cost, Savings)
   - Feature Importance Analysis (SHAP / LIME)

##  Key Skills Gained
- Binary Classification Modeling
- Risk Scoring
- Business-focused Evaluation
- Cost Optimization Techniques

##  Getting Started

Install necessary packages:

```bash
pip install pandas scikit-learn catboost shap matplotlib
