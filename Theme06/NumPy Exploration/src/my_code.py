# -*- coding: utf-8 -*-
"""
#KT 3
Tutustu omatoimisesti NymPy-kirjastoon. Käytä tutustumiseen vaikkapa w3schools-sivustoa. 
Tee yksi esimerkkiohjelma, jossa käytät ko kirjastoa sekä selitä se python-kommenteissa. Esimerkkisovellus on vapaavalintainen.

#TASK 3
Independently explore the NymPy library. You can use resources like the W3Schools website for reference.
Create an example program that uses the NymPy library, and explain it with Python comments.
The example application is up to your choice.

"""
# Importing the NumPy library
import numpy as np

# Explanation: NumPy is used for numerical and statistical operations.
# We'll use it to generate random data and perform statistical calculations.

if __name__ == '__main__':
    # Generate a dataset of 1000 random values from a normal distribution (mean=50, std_dev=10)
    data = np.random.normal(loc=50, scale=10, size=1000)
    print("Generated data (first 10 values):", data[:10])

    # Explanation: `np.random.normal(loc, scale, size)` generates random values from a normal distribution.
    # `loc` is the mean, `scale` is the standard deviation, and `size` is the number of values generated.

    # Calculate the mean of the dataset
    mean_value = np.mean(data)
    print(f"Mean of the dataset: {mean_value:.2f}")

    # Explanation: `np.mean()` calculates the average value of the array.

    # Calculate the median of the dataset
    median_value = np.median(data)
    print(f"Median of the dataset: {median_value:.2f}")

    # Explanation: `np.median()` finds the middle value in the sorted dataset.

    # Calculate the standard deviation of the dataset
    std_deviation = np.std(data)
    print(f"Standard deviation of the dataset: {std_deviation:.2f}")

    # Explanation: `np.std()` calculates the standard deviation of the dataset, showing how spread out the data is.

    # Find the 25th and 75th percentiles (also known as quartiles)
    percentile_25 = np.percentile(data, 25)
    percentile_75 = np.percentile(data, 75)
    print(f"25th percentile (Q1): {percentile_25:.2f}")
    print(f"75th percentile (Q3): {percentile_75:.2f}")

    # Explanation: `np.percentile()` finds the value below which a certain percentage of the data falls.

    # Simulate a z-score (standard score) calculation for each data point
    z_scores = (data - mean_value) / std_deviation
    print(f"Z-scores (first 10 values): {z_scores[:10]}")

    # Explanation: Z-score represents how many standard deviations a data point is from the mean.
    # Z = (X - μ) / σ where X is the data point, μ is the mean, and σ is the standard deviation.

    # Generate a histogram of the dataset (just showing the counts for this example)
    histogram, bin_edges = np.histogram(data, bins=10)
    print("Histogram counts:", histogram)
    print("Bin edges:", bin_edges)

    # Explanation: `np.histogram()` computes the frequency of the data within specified bins.
    # `bin_edges` are the boundaries of each bin, and `histogram` is the count of values in each bin.

    # Create a cumulative sum of the dataset
    cumulative_sum = np.cumsum(np.sort(data))
    print(f"Cumulative sum (first 10 values): {cumulative_sum[:10]}")

    # Explanation: `np.cumsum()` returns the cumulative sum of the sorted data. Each value in the result
    # array is the sum of all previous values in the sorted array.




