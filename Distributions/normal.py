import numpy as np
import matplotlib.pyplot as plt

# Define the mean and standard deviation for the normal distribution
mean = 0
std_dev = 1

# Generate random numbers from a normal distribution
num_samples = 1000  # Change this to the number of samples you want
random_numbers = np.random.normal(mean, std_dev, num_samples)

# Create a histogram of the random numbers
plt.hist(random_numbers, bins=30, density=True, alpha=0.6, color='b', edgecolor='black')

# Add labels and a title to the plot
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.title('Histogram of Random Numbers from Normal Distribution')

# Plot the probability density function (PDF) of the normal distribution
x = np.linspace(mean - 4 * std_dev, mean + 4 * std_dev, 100)
pdf = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev)**2)
plt.plot(x, pdf, color='r', label='Normal PDF')

# Add a legend
plt.legend()

# Show the plot
plt.show()
