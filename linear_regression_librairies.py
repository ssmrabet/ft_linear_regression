import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

regressor = LinearRegression()
regressor.fit(X, y)

print(regressor.predict([[100000]]))

print(regressor.predict(X))
