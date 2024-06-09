#scatter plot: A scatter plot is a diagram where each value in the data set is represented by a dot.
import numpy as np
import matplotlib.pyplot as plt

#x = [1,2,3,4,5]
x = np.random.randn(100, 1) # randn is used to generate random numbers from a normal distribution. The function takes the shape of the array as an argument. In this case, the shape is (100, 1), which means that the array will have 100 rows and 1 column.

# plot the scatter plot
plt.scatter(range(len(x)), x, color='blue')
plt.title('Scatter Plot of Given Data')
plt.show()