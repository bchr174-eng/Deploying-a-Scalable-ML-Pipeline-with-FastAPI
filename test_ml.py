import pytest
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
# Assuming these functions are in ml.py
from ml import train_model, compute_model_metrics, process_data 

# TODO: implement the first test. Change the function name and input as needed
def test_model_algorithm():
    """
    Test if the training function returns a Random Forest Model.
    """
    X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    y = np.array([0, 1, 1, 0])
    model = train_model(X, y)
    
    # Check if the model is RandomForest (as intended)
    assert isinstance(model, RandomForestClassifier)

# TODO: implement the second test. Change the function name and input as needed
def test_data_processing():
    """
    Test if processing splits data into expected shapes.
    """
    data = pd.DataFrame({
        'age': [25, 30, 45, 50],
        'workclass': ['Private', 'Private', 'Self', 'Private'],
        'salary': ['<=50K', '>50K', '>50K', '<=50K']
    })
    # Mock label binning
    train, test = train_test_split(data, test_size=0.5)
    X_train, y_train, _, _ = process_data(train, target='salary')

    assert len(X_train) == 2
    assert isinstance(X_train, np.ndarray)

# TODO: implement the third test. Change the function name and input as needed
def test_metrics_range():
    """
    Test if metrics return expected types and valid ranges.
    """
    y_true = np.array([0, 1, 1, 0])
    y_pred = np.array([0, 1, 0, 0])
    precision, recall, fbeta = compute_model_metrics(y_true, y_pred)
    
    assert isinstance(precision, float)
    assert 0 <= precision <= 1
    assert 0 <= recall <= 1
    assert 0 <= fbeta <= 1