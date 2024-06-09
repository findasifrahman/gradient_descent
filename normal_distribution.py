'''
Normal Distribution (Gaussian): Bell curve in 2-d kartesian plot. the bell curve gives you a visual representation of how your data is distributed around the mean. in this case 3. 
For a small dataset like  the curve might not be very smooth, but with larger datasets, it helps to understand the distribution and variability of your data.
The normal distribution curve created using the mean (3) and standard deviation (1.41). This curve represents the theoretical distribution of data if it were to follow a normal 
distribution. 
Normal distro is used for linear regression. Not all set will behave like a bell curve. Best way to see if a dataset is normally distributed or not isto see the histogram chart
it is also for Exploratory Data Analysis and probabilistic thinking that next number should be around the mean or top of the bell
Normal distribution is to use: 
    If your histogram closely matches the normal distribution curve, it suggests that your data is approximately normally distributed.
    If there are significant deviations, it indicates skewness, outliers, or a different distribution type, guiding you in further analysis or data transformation.
How do you know if data is normally distributed?
A histogram presents a useful graphical representation of the given data. When a histogram of distribution is superimposed with its normal curve, then the distribution is known as the normal distribution.
'''
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