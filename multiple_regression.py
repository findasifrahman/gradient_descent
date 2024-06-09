'''
Multiple regression is like linear regression, but with more than one independent value, meaning that we try to predict a value based on two or more variables.

In multiple regression, the values are calculated with the following formula:
y = c + m1x1 + m2x2 + ... + mnxn
The y is the dependent variable, c is the constant, m is the coefficient, and x is the independent variable.
The p value in multiple regression , the p value used is a type 3 P-value. This essentially means that the p value shows the significance of the variable in the model assuming that all other variables exist in the model.

Thus, adding or subtracting variables to your model could change your p-value slightly.

'''

import pandas as pd
from sklearn import linear_model

df = pd.read_csv('data/data.csv')

print(df.head())

'''
The dataser contains 4 column.Car Model,Volume,Weight,CO2 Emission. We will use Volume and Weight to predict CO2 Emission
so we will use Volume and Weight as independent variable and CO2 Emission as dependent variable
'''
X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)
predictedCO2 = regr.predict([[2300, 1300]]) # predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3

print(predictedCO2) # [107.2087328] means that the CO2 emission of a car with 1300cm3 volume and 2300kg weight is 107.2087328 grams
'''
Coefficient
The coefficient is a factor that describes the relationship with an unknown variable.

Example: if x is a variable, then 2x is x two times. x is the unknown variable, and the number 2 is the coefficient.
In this case, we can ask for the coefficient value of weight against CO2, and for volume against CO2.
 The answer(s) we get tells us what would happen if we increase, or decrease, one of the independent values
'''
print(regr.coef_) # [0.00755095 0.00780526] means that for every 1kg of weight, the CO2 emission increases by 0.00755095g. And for every 1cm3 of volume, the CO2 emission increases by 0.00780526g.