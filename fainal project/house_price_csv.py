# ============================
# House Price Prediction (CSV Version)
# ============================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


def main():
    df = pd.read_csv("data.csv")
    
    print(df.head())

    print(df.isnull().sum())

    df = df.fillna(df.mean(numeric_only=True))


    df = pd.get_dummies(df, drop_first=True)

    X = df.drop("price", axis=1)
    y = df["price"]


    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )


    model = LinearRegression()
    model.fit(X_train, y_train)


    y_pred = model.predict(X_test)


    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    print("نتائج التقييم:")
    print(f"MSE: {mse:.2f}")
    print(f"RMSE: {rmse:.2f}")
    print(f"R2: {r2:.2f}")


    plt.figure(figsize=(6, 4))
    sns.scatterplot(x=y_test, y=y_pred, alpha=0.5)
    plt.xlabel("Actual Prices")
    plt.ylabel("Predicted Prices")
    plt.title("Actual vs Predicted House Prices")
    plt.show()


if __name__ == "__main__": 
    main()
# ============================