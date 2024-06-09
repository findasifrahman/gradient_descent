Gradient descent example using simple regression

example set = {1,2,3,4,5}
mean = total_sum_of_set/total_number_in_set = (1+2+3+4+5)/5 = 3  . np.mean(example_set)

standard_deviation = Rootover of Addition of How much each nimber in a set is deviated from the mean of the set in square formula devided by total number. if mean is 3 then = ((1-3)^2 + (2-3)^2 + (3-3)^2 + (4-3)^2 + (5-3)^2)/5-1 = (4+1+0+1+4)/5= 10/5 = 2 =  rootover(2) = 1.41

varience

Histogram: You can see roughly where the peaks of the distribution are. in a histogram. The higher the bins data is separated more. is a chart that plots the distribution of a numeric variable’s values as a series of bars

Normal Distribution (Gaussian): Bell curve in 2-d kartesian plot. the bell curve gives you a visual representation of how your data is distributed around the mean. in this case 3. For a small dataset like  the curve might not be very smooth, but with larger datasets, it helps to understand the distribution and variability of your data.
The normal distribution curve created using the mean (3) and standard deviation (1.41). This curve represents the theoretical distribution of data if it were to follow a normal distribution. 
Normal distro is used for linear regression. Not all set will behave like a bell curve. Best way to see if a dataset is normally distributed or not isto see the histogram chart
it is also for Exploratory Data Analysis and probabilistic thinking that next number should be around the mean or top of the bell
Normal distribution is to use: 
    If your histogram closely matches the normal distribution curve, it suggests that your data is approximately normally distributed.
    If there are significant deviations, it indicates skewness, outliers, or a different distribution type, guiding you in further analysis or data transformation.
How do you know if data is normally distributed?
A histogram presents a useful graphical representation of the given data. When a histogram of distribution is superimposed with its normal curve, then the distribution is known as the normal distribution.

scatter plot: A scatter plot is a diagram where each value in the data set is represented by a dot.

Linear Regression: y=mx+c is a simple linear equation. ax+(b^2)y = 3 is also linear as x and y is not square value (x^2 = not linear). Linear equation and Linear regression is not same. In a linear regression coefficiant (a,b) is linear but x,y may not be linear
Linera regression is the process of predicting y based on x. 
The term regression is used when you try to find the relationship between variables.

In Machine Learning, and in statistical modeling, that relationship is used to predict the outcome of future events

Linear regression uses the relationship between the data-points to draw a straight line through all them.

This line can be used to predict future values.
at least 2 parameters are required to draw the line for linear regression. One for x and one for y. 
If more than 2 parameters are given, then the line is called a multi-dimensional line.

Python has methods for finding a relationship between data-points and to draw a line of linear regression. We will show you how to use these methods instead of going through the 
mathematic formula.

In the example below, the x-axis represents age, and the y-axis represents speed. We have registered the age and speed of 13 cars as they were passing a tollbooth.
 Let us see if the data we collected could be used in a linear regression:

for a equation y=mx+c, m is slope and c is intercept
The r value ranges from -1 to 1. where 0 means no relationship, and 1 (and -1) means 100% related
p is the p-value. A p-value of less than 0.05 is considered statistically significant. It means that there is strong evidence against the null hypothesis, 