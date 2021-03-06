#import Libraries
import pandas as pd  
import numpy as np    
import matplotlib.pyplot as plt

#import Dataset
data = pd.read_csv("D:/Study Point/Data Science/Intership/Students/students.csv")  
print("Successfully imported data into console" )  

data.head(6)  

#Graphs
data.plot(x='Hours', y='Scores', style='o')    
plt.title('Hours vs Percentage')    
plt.xlabel('The Hours Studied')    
plt.ylabel('The Percentage Score')    
plt.show()


#divide the data into attributes and labels 
X = data.iloc[:, :-1].values    
y = data.iloc[:, 1].values  

#split data into train and test dataset
from sklearn.model_selection import train_test_split    
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2, random_state=0)   

#train data
from sklearn.linear_model import LinearRegression    
regressor = LinearRegression()    
regressor.fit(X_train, y_train)   
  
line = regressor.coef_*X+regressor.intercept_  
plt.scatter(X, y)  
plt.plot(X, line);  
plt.show()

#predict
print(X_test)   
y_pred = regressor.predict(X_test)  

#Actual Vs Predict
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})    
df

hours = [[9.25]]  
own_pred = regressor.predict(hours)  
print("Number of hours = {}".format(hours))  
print("Prediction Score = {}".format(own_pred[0]))  
