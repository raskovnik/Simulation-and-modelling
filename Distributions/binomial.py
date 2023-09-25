import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Define parameters for the binomial distribution
n = 10  # Number of trials
p = 0.3  # Probability of success

# Generate random numbers from a binomial distribution
num_samples = 1000  # Change this to the number of samples you want
random_numbers = np.random.binomial(n, p, num_samples)

# Create a histogram-like PMF plot
unique_values, counts = np.unique(random_numbers, return_counts=True)
plt.bar(unique_values, counts / len(random_numbers), color='b', alpha=0.6, label='PMF')

# Add labels and a title to the plot
plt.xlabel('Number of Successes (k)')
plt.ylabel('Probability')
plt.title(f'PMF of Binomial Distribution (n={n}, p={p})')

# Plot the theoretical PMF of the binomial distribution
x = np.arange(0, n + 1)
pmf = binom.pmf(x, n, p)
plt.plot(x, pmf, 'ro-', label='PMF')

# Add a legend
plt.legend()

# Show the plot
plt.show()
