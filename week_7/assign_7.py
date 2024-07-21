import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df=pd.read_csv(r"C:\Users\DELL\Downloads\Boston.csv")
df

df.columns

x=df[['Unnamed: 0', 'crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis',
       'rad', 'tax', 'ptratio', 'black', 'lstat']]
y=df[['medv']]

x
y

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=26)
model=LinearRegression()
model.fit(x_train,y_train)

y_pred=model.predict(x_test)
y_pred

np.sqrt(mean_squared_error(y_test,y_pred))

plt.scatter(y_test,y_pred)
plt.xlabel('ACTUAL MEDV')
plt.ylabel('PREDICTED MEDV')
plt.title('ACTUAL MEDV VS PREDICTYED MEDV ')
plt.show()
