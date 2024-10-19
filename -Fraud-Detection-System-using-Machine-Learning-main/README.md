# Fraud Detection System

This repository contains a fraud detection system built using a Random Forest Classifier. The model is trained on transactional data to predict whether a given transaction is fraudulent. It also includes functionality to detect specific types of fraud, such as Account Takeover, Phishing, Money Laundering, and more.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Model Details](#model-details)
- [Evaluation](#evaluation)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project aims to detect fraud in financial transactions. The system uses machine learning techniques to classify transactions as **fraud** or **not fraud** based on various features, including transaction amount, balances, transaction patterns, and additional features engineered from the dataset.

The model is trained on a combination of **numerical** and **categorical** data using a pipeline that handles preprocessing, imputation, and scaling. It is then saved and can be loaded for real-time fraud detection.

## Features

- **Fraud Prediction**: Predicts whether a transaction is fraudulent based on input features.
- **Fraud Type Detection**: Identifies the specific type of fraud if detected (e.g., Account Takeover, New Account Fraud).
- **Feature Engineering**: Adds domain-specific features such as the number of transactions per account, average transaction amount, and changes in transaction patterns.
- **User Interaction**: Allows users to input transaction data interactively and get real-time predictions.
- **Model Persistence**: The trained model can be saved to and loaded from a file for future predictions.

## Installation

To run this project locally, follow these steps:

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/fraud-detection-system.git
    ```
2. Navigate to the project directory:
    ```bash
    cd fraud-detection-system
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running the Script

1. Load the model and run fraud detection with user input:
    ```bash
    python main.py
    ```

2. You'll be prompted to enter transaction details interactively. The system will predict whether the transaction is fraudulent and, if applicable, detect the type of fraud.

### Predicting Transactions Programmatically

You can also use the model in your own scripts by loading the saved model:
```python
import pickle

# Load the model
with open('fraud_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Example transaction
transaction = {
    'amount': 5000,
    'oldbalanceOrg': 3000,
    'newbalanceOrig': 500,
    'oldbalanceDest': 100,
    'newbalanceDest': 5500,
    'hour': 21,
    'type': 'TRANSFER',
    'transactions_per_account': 10,
    'transactions_per_hour': 5,
    'avg_transaction_amount': 700,
    'is_new_account':  0,
    'transactions_per_destination': 10,
    'change_in_transaction_pattern': 50
}

# Predict
prediction = model.predict(pd.DataFrame([transaction]))
print("Fraud" if prediction[0] else "Not Fraud")
```

## Dataset

The model is trained on a public dataset containing transactional data. The dataset includes the following fields:

- **step**: Time step of the transaction (in hours).
- **type**: Type of transaction (e.g., `TRANSFER`, `CASH_OUT`).
- **amount**: Amount of money involved in the transaction.
- **oldbalanceOrg**: Initial balance of the origin account before the transaction.
- **newbalanceOrig**: New balance of the origin account after the transaction.
- **oldbalanceDest**: Initial balance of the destination account before the transaction.
- **newbalanceDest**: New balance of the destination account after the transaction.
- **isFraud**: Binary label indicating whether the transaction is fraudulent.

## Model Details

- **Model**: Random Forest Classifier
- **Preprocessing**:
  - Numerical features are standardized using `StandardScaler`.
  - Categorical features are one-hot encoded using `OneHotEncoder`.
  - Additional domain-specific features are engineered to enhance the model’s ability to detect fraud.
  
- **Feature Engineering**:
  - Transactions per account
  - Transactions per hour
  - Average transaction amount per account
  - Transactions to unfamiliar or new accounts
  - Change in transaction patterns

## Evaluation

The model is evaluated using:
- **Confusion Matrix**
- **Classification Report** (Accuracy, Precision, Recall, F1 Score)

### Example:

```
Confusion Matrix:
[[85239   124]
 [   56   110]]

Classification Report:
              precision    recall  f1-score   support

           0       1.00      1.00      1.00     85363
           1       0.47      0.66      0.55       166

    accuracy                           1.00     85529
   macro avg       0.73      0.83      0.78     85529
weighted avg       1.00      1.00      1.00     85529
```

## Contributing

Contributions are welcome! Please submit a pull request or raise an issue to suggest improvements or report bugs.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---
