from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

def train_model(X_train, y_train, **kwargs):
    """Train an XGBoost model."""
    model = XGBRegressor(**kwargs)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """Evaluate model performance."""
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    return {
        "mse": mse,
        "rmse": np.sqrt(mse),
        "r2_score": r2
    }
