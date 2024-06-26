import numpy as np

np.random.seed(42) # The np.random.seed(42) function sets the seed for the NumPy random number generator. Setting a seed ensures reproducibility of random numbers. This means that every time you run the code with the same seed, you get the same sequence of random numbers. The number 42 is arbitrary and can be any integer

x = 2 * np.random.rand(100, 1)
y = 4 + 3 * x + np.random.randn(100, 1)
#print(np.random.randn(100, 1))

