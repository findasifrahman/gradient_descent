'''
train/test: In Machine Learning models are to predict the outcome of certain events,To measure if the model is good enough, we can use a method called Train/Test.

Train/Test is a method to measure the accuracy of model.

It is called Train/Test because you split the data set into two sets: a training set and a testing set.

80% for training, and 20% for testing.

train the model using the training set.

test the model using the testing set.

Train the model means create the model.

Test the model means test the accuracy of the model.

R2: R2, also known as R-squared. It measures the relationship between the x axis and the y axis, and the value ranges from 0 to 1, 
where 0 means no relationship, and 1 means totally related. The sklearn module has a method called r2_score() that will help us find this relationship
'''
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# lets create a dataset of 100 custtomer in a shop and their shopping habits
x = np.random.normal(3, 1, 100) # normal distribution with mean 3 and standard deviation 1. x is the amount of minutes the customer has spent in the shop
y = np.random.normal(150, 40, 100) / x # normal distribution with mean 150 and standard deviation 40 divided by x . Y is the amount of money spent by the customer

plt.scatter(x, y)
plt.show()

# lets split the data into 80% training and 20% testing
# The training set should be a random selection of 80% of the original data.The testing set should be the remaining 20%.
train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

# after looking at scatter plot, we can see that there is a relationship between x and y and we can use Polynomial regression to predict the outcome
mymodel = np.poly1d(np.polyfit(train_x, train_y, 4)) # polyfit is a function in numpy that takes x and y values and the degree of the polynomial and returns the coefficients of the polynomial that best fits the data
myline = np.linspace(0, 6, 100) # np.linspace is a function in numpy that returns evenly spaced numbers over a specified interval. In this case, it returns 100 evenly spaced numbers between 0 and 6

plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
#plt.show()

r2score = r2_score(train_y,mymodel(train_x))
print(r2score) # 0.7988645544629794 means that the model is 79.88% accurate

r2score_test = r2_score(test_y,mymodel(test_x))
print(r2score_test) # 0.8086921460343551 means that the model is 80.86% accurate and fits good in testing data

print(mymodel(5)) # 22.87962591812146 means that the model predicts that a customer who spends 5 minutes in the shop will spend 22.87962591812146 dollars