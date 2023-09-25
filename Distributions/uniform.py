import numpy as np
import matplotlib.pyplot as plt

# Define the lower and upper bounds of the uniform distribution
a = 2
b = 8

# Generate random numbers from a uniform distribution
num_samples = 1000  # Change this to the number of samples you want
random_numbers = np.random.uniform(a, b, num_samples)

# Create a histogram-like PDF plot
plt.hist(random_numbers, bins=30, density=True, alpha=0.6, color='b', edgecolor='black', label='PDF')

# Add labels and a title to the plot
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.title(f'PDF of Uniform Distribution [{a}, {b}]')

# Plot the theoretical PDF of the uniform distribution
x = np.linspace(a, b, 100)
pdf = np.full_like(x, 1 / (b - a))
plt.plot(x, pdf, 'r-', label='PDF')

# Add a legend
plt.legend()

# Show the plot
plt.show()
