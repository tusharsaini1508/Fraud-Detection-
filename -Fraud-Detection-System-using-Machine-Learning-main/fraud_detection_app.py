#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

# Load the pre-trained model
with open('fraud_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define numerical and categorical features
categorical_features = ['type']
numerical_features = ['amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest', 'hour',
                      'transactions_per_account', 'transactions_per_hour', 'avg_transaction_amount', 'is_new_account',
                      'transactions_per_destination', 'change_in_transaction_pattern']

def predict_transaction(transaction):
    """
    Predict whether a transaction is fraudulent.
    """
    transaction_df = pd.DataFrame([transaction])
    transaction_df = transaction_df[numerical_features + categorical_features]
    prediction = model.predict(transaction_df)
    return prediction[0]

def detect_fraud_type(transaction):
    """
    Detect the type of fraud based on transaction details.
    """
    fraud_types = []

    if transaction['is_new_account'] == 1:
        fraud_types.append("New Account Fraud")

    if transaction['transactions_per_account'] > 50:
        fraud_types.append("Account Takeover Fraud")

    if transaction['transactions_per_hour'] > 10:
        fraud_types.append("Unauthorized Transaction Fraud")

    if transaction['avg_transaction_amount'] > 10000:
        fraud_types.append("Money Laundering")

    if transaction['change_in_transaction_pattern'] > 100:
        fraud_types.append("Change in Transaction Pattern Fraud")

    if not fraud_types:
        fraud_types.append("No Specific Fraud Detected")

    return fraud_types

def main():
    st.title("Fraud Detection System")
    
    # Collect user input for transaction details
    st.header("Enter Transaction Details")
    amount = st.number_input("Amount", value=0.0)
    oldbalanceOrg = st.number_input("Old Balance Origin", value=0.0)
    newbalanceOrig = st.number_input("New Balance Origin", value=0.0)
    oldbalanceDest = st.number_input("Old Balance Destination", value=0.0)
    newbalanceDest = st.number_input("New Balance Destination", value=0.0)
    hour = st.number_input("Hour (0-23)", min_value=0, max_value=23, value=0)
    transaction_type = st.selectbox("Transaction Type", ['CASH-IN', 'CASH-OUT', 'DEBIT', 'PAYMENT', 'TRANSFER'])
    transactions_per_account = st.number_input("Transactions per Account", value=1)
    transactions_per_hour = st.number_input("Transactions per Hour", value=1)
    avg_transaction_amount = st.number_input("Average Transaction Amount", value=0.0)
    is_new_account = st.selectbox("Is New Account", [0, 1])
    transactions_per_destination = st.number_input("Transactions per Destination", value=1)
    change_in_transaction_pattern = st.number_input("Change in Transaction Pattern", value=0.0)

    # Prepare the transaction for prediction
    transaction = {
        'amount': amount,
        'oldbalanceOrg': oldbalanceOrg,
        'newbalanceOrig': newbalanceOrig,
        'oldbalanceDest': oldbalanceDest,
        'newbalanceDest': newbalanceDest,
        'hour': hour,
        'type': transaction_type,
        'transactions_per_account': transactions_per_account,
        'transactions_per_hour': transactions_per_hour,
        'avg_transaction_amount': avg_transaction_amount,
        'is_new_account': is_new_account,
        'transactions_per_destination': transactions_per_destination,
        'change_in_transaction_pattern': change_in_transaction_pattern
    }

    # Predict fraud and detect fraud type
    if st.button("Predict Fraud"):
        prediction = predict_transaction(transaction)
        st.write("Prediction: ", "Fraud" if prediction else "Not Fraud")
        
        if prediction:
            fraud_types = detect_fraud_type(transaction)
            st.write("Detected Fraud Types: ", ", ".join(fraud_types))

if __name__ == "__main__":
    main()


# In[ ]:




