# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17aBcIl0eh4vd3jim2BqkTYkNVSgdykq5
"""

# Import the libraries and functions that we need along the code
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

#Define the array, in this case we define it as training hours
training_hours = np.array([ 2,  8,  5, 12,  7, 15,  3, 10,  9, 20, 14,  6, 18, 13, 11, 16,  4, 17, 19, 22, 25, 21, 26, 23, 27, 28, 29, 30, 27,  5, 22,  7, 10, 14,  8,  9, 24, 26, 15, 25,  8, 26, 26, 28,  2, 15, 10,  1, 20, 24, 14, 18, 24, 26, 17, 27,  1, 24, 11, 23, 21, 15, 18,  4, 20, 20, 23, 30,  9,  3, 20, 20, 25, 29, 14, 20, 23, 21, 10,  6, 18, 24, 22, 26,  5, 21, 28, 11, 24, 28, 16, 12,  9, 26, 26, 24, 15,  1, 22, 30, 30,  7,  1, 20,  1, 17,  8,  8])
#Define array, for the perfomance according to the hours
performance = np.array([ 55,  65,  60,  75,  70,  85,  58,  72,  68,  90,  80,  62,  88,  77,  73,  80,  57,  82,  85,  92,  95,  90,  98,  94, 100, 102, 104, 105,  98,  57,  95,  66,  69,  75,  66,  63,  96,  94,  83,  98,  61,  94,  99, 106,  53,  84,  67,  57,  86,  99,  82,  90,  93, 100,  81,  98,  55,  99,  69,  94,  93,  84,  84,  60,  94,  87,  90, 101,  70,  55,  85,  88,  95, 106,  79,  86,  95,  89,  68,  62,  87,  90,  96,  96,  55,  94,  98,  74,  97, 103,  80,  70,  69, 102,  94,  94,  81,  53,  96, 103, 102,  74,  55,  94,  53,  81,  60,  65])


x = training_hours.reshape(-1, 1)
y = performance

#Divide the data to training and test (80% training, 20% test)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#Create the model
model = LinearRegression()

#Train the model with the training data
model.fit(x_train, y_train)

#Start the predictions with the test data
y_pred = model.predict(x_test)

#Get and print the R2
r2 = model.score(x_test, y_test)
print("R2 Score:", r2)

#Get the and print coefficient
coefficient = model.coef_[0]
print("Coefficient:", coefficient)

#Get and print the intercept
intercept = model.intercept_
print("Intercept:", intercept)

#Create the graphic, it will show the the blue dots as the real data and the red line is a prediction
plt.scatter(x_test, y_test, color='blue') #Real data
plt.plot(x_test, y_pred, color='red', linestyle='-', linewidth=2, label='Predicted Performance') #Prediction line
plt.xlabel('Training Hours') #x-axis name
plt.ylabel('Final Perormance') #y-axis name
plt.title('TrainingXPerformance') #Graphic tittle
plt.legend() #Give a name to the line
plt.show() #Show graphic