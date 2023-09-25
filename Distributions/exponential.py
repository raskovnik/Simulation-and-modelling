import numpy as np
import matplotlib.pyplot as plt

# Define the rate parameter (lambda) for the exponential distribution
rate_parameter = 0.5  # Adjust this value as needed

# Generate random numbers from an exponential distribution
num_samples = 1000  # Change this to the number of samples you want
random_numbers = np.random.exponential(scale=1/rate_parameter, size=num_samples)

# Create a histogram of the random numbers
plt.hist(random_numbers, bins=30, density=True, alpha=0.6, color='b', edgecolor='black', label='Histogram')

# Add labels and a title to the plot
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.title('Histogram and PDF of Exponential Distribution')

# Plot the probability density function (PDF) of the exponential distribution
x = np.linspace(0, 10, 100)
pdf = rate_parameter * np.exp(-rate_parameter * x)
plt.plot(x, pdf, color='r', label='Exponential PDF')

# Add a legend
plt.legend()

# Show the plot
plt.show()
