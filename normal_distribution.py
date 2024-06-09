import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

np.random.seed(42) # The np.random.seed(42) function sets the seed for the NumPy random number generator. Setting a seed ensures reproducibility of random numbers. This means that every time you run the code with the same seed, you get the same sequence of random numbers. The number 42 is arbitrary and can be any integer

x= np.array([1,2,3,4,5.4]) # numpy array is faster than list
print(x)
mean = np.mean(x)
std = np.std(x)
print(mean)
print(std)

# craete a range of values for x axis
x_range = np.linspace(x.min() - 1, x.max() + 1, 100)
print(x_range)

# calculate the y(pdf) values for the normal distribution
pdf = stats.norm.pdf(x_range, mean, std)
print(pdf)

# Plot the original data points and the PDF
print(np.zeros_like(x))
plt.scatter(x, np.zeros_like(x), color='red', label='Data points')
plt.plot(x_range, pdf, 'k', linewidth=2, label='Normal distribution')
plt.title('Normal Distribution of Given Data')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.legend()
plt.show()