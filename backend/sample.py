import numpy as np
import pandas as pd  
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

DATA_CSV_FILE = pd.read_csv('population.csv')
DATA_CSV_FILE.isnull().sum()

print(DATA_CSV_FILE)
X = pd.DataFrame(np.c_[
    DATA_CSV_FILE['Year'],
    DATA_CSV_FILE['Rooms'],
    DATA_CSV_FILE['FullTime'],
    DATA_CSV_FILE['PartTime']],
    columns = ['Year',
    'Rooms',
    'FullTime',
    'PartTime'])
Y = DATA_CSV_FILE['Population']


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2)
print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)

lin_model = LinearRegression()
lin_model.fit(X_train, Y_train)

predict_population = lin_model.predict([[2022, 70, 30, 20]])
predict_population = int(predict_population)
print(predict_population)