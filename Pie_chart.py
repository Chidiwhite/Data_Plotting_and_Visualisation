import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# Use the 'fivethirtyeight' style for the plot
plt.style.use('fivethirtyeight')

# Define the data for the pie chart
slices = [57498, 53837, 46156, 35381, 34872]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java'] 
explode = [0.1, 0.1, 0.1, 0.1, 0.1]

# Create a pie chart with the specified data and settings
plt.pie(slices, shadow=True, startangle=90, labels=labels, autopct='%1.1f%%', explode=explode, wedgeprops={'edgecolor': 'blue'})

# Set the title of the pie chart
plt.title('Top Five Programming Languages')

# Display the pie chart
plt.show()
