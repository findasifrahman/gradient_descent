'''
Linear Regression: y=mx+c is a simple linear equation. ax+(b^2)y = 3 is also linear as x and y is not square value (x^2 = not linear). Linear equation and Linear regression is 
not same. In a linear regression coefficiant (a,b) is linear but x,y may not be linear
Linera regression is the process of predicting y based on x. 
The term regression is used when you try to find the relationship between variables.

In Machine Learning, and in statistical modeling, that relationship is used to predict the outcome of future events

Linear regression uses the relationship between the data-points to draw a straight line through all them.

This line can be used to predict future values.

at least 2 parameters are required to draw the line for linear regression. One for x and one for y. 
If more than 2 parameters are given, then the line is called a multi-dimensional line.

'''

'''
Python has methods for finding a relationship between data-points and to draw a line of linear regression. We will show you how to use these methods instead of going through the 
mathematic formula.

In the example below, the x-axis represents age, and the y-axis represents speed. We have registered the age and speed of 13 cars as they were passing a tollbooth.
 Let us see if the data we collected could be used in a linear regression:

for a equation y=mx+c, m is slope and c is intercept
The r value ranges from -1 to 1. where 0 means no relationship, and 1 (and -1) means 100% related
p is the p-value. A p-value of less than 0.05 is considered statistically significant. It means that there is strong evidence against the null hypothesis, 
'''
import matplotlib.pyplot as plt
import scipy.stats as stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6] # age
y = [99,86,87,88,111,86,103,87,94,78,77,85,86] # speed of 13 cars


# we will use scipy library to draw the line of linear regression
slp, intercept, r, p, std_err = stats.linregress(x, y) 
# linregress is a function in scipy library that calculates the slope, intercept, r, p, and std_err values for the linear regression line. 
#The function takes the x and y values as arguments and returns the slope, intercept, r, p, and std_err values.
# for a equation y=mx+c, m is slope and c is intercept
# r is the correlation coefficient. It ranges from -1 to 1. If it is close to 1, it means that there is a strong positive correlation between the variables. 
#If it is close to -1, it means that there is a strong negative correlation between the variables. If it is close to 0, it means that there is no correlation between the variables.
# p is the p-value. A p-value of less than 0.05 is considered statistically significant. It means that there is strong evidence against the null hypothesis, 
#so you reject the null hypothesis. a p value less then 0.05 means the coefficient is significant and greater than 0.05 means the coefficient is not significant
# std_err is the standard error. It measures the accuracy of the coefficient. The lower the standard error, the better the coefficient.
print(slp, intercept, r, p, std_err)
# the result is slp= -1.7512877115526118, intercept=103.10596026490066, r=-0.758591524376155, p=0.0026468739224561064, std_err=0.453536157607742
# intercept 103.10596026490066 means that the line crosses the y-axis at 103.10596026490066 (y=mx+c and c is the intercept). so it means when x or age is 0 then speed is 103.10596026490066
# slope -1.7512877115526118 means that the slope of the line is -1.7512877115526118. It means that for every unit increase in x or age, the speed decreases by 1.7512877115526118 units.
# r=-0.758591524376155 means that there is a strong negative correlation between the variables. It means that the age and speed of the cars are negatively correlated. Its not perfect but strong
# p=0.0026468739224561064 means that the coefficient is significant and less then 0.05. It means that with age the speed of the cars is decreasing
# std_err=0.453536157607742 means that the accuracy of the coefficient is 0.453536157607742. The lower the standard error, the better the coefficient.

def myfunc(x):
  return slp * x + intercept

mymodel = list(map(myfunc, x))
print(mymodel)

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

# Predict the speed of a 10 years old car:
speed = myfunc(10)
print(speed)

# The example predicted a speed of 85.59308314937454 for a 10 years old car. as you can see we have used the linear regression to predict the speed of a 10 years old car.