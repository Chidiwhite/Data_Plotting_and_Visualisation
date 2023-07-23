import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

# Read data from 'data1.csv' file into a DataFrame
data = pd.read_csv('data1.csv')

# Extract the 'Age' column data from the DataFrame
age = data['Age']

# Define bin intervals for the histogram
bins = [10, 20, 30, 40, 50, 60]

# Create a histogram plot with the 'Age' data using the specified bins
plt.hist(age, bins=bins, edgecolor='black', color='pink')

# Set the value of the median age
median = 29

# Add a vertical line at the median age on the histogram plot
plt.axvline(median, color='red', label='median_age')

# Add a legend to the plot to show the label of the median age line
plt.legend()

# Set the title, x-axis label, and y-axis label for the plot
plt.title('My Histogram')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# Display the histogram plot
plt.show()
