import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42) # The np.random.seed(42) function sets the seed for the NumPy random number generator. Setting a seed ensures reproducibility of random numbers. This means that every time you run the code with the same seed, you get the same sequence of random numbers. The number 42 is arbitrary and can be any integer

x = np.array([1,2,3,4,5,4])

# Plot the histogram of the data
plt.hist(x, bins=10, color='lightblue', edgecolor='black')
plt.title('Histogram of Given Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()