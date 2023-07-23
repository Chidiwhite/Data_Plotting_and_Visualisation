import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# Use a dark background style for the plot
plt.style.use('dark_background')
# If you want to create a plot with an xkcd style, uncomment the next line
# plt.xkcd()

# Define the ages and their corresponding index for the x-axis
ages = [23, 24, 25, 26, 27, 28, 29, 30, 31, 32]
age_index = np.arange(len(ages))

# Set the width of the bars in the bar chart
width = 0.25

# Define the salary data for Python, Java, and C developers
py_salary = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
java_salary = [25000, 35000, 45000, 55000, 65000, 75000, 85000, 95000, 105000, 110000]
c_salary = [12300, 14300, 15300, 16300, 17300, 18300, 19500, 20500, 10500, 20500]

# Create the bar chart by plotting the data for each developer group
plt.bar(age_index - width, py_salary, width=width, label='python devs', color='y')
plt.bar(age_index, java_salary, width=width, label='java devs', color='b')
plt.bar(age_index + width, c_salary, width=width, label='C devs', color='c')

# Set the x-axis labels to be the ages and adjust their positions
plt.xticks(ticks=age_index, labels=ages)

# Set the x-axis and y-axis labels and the plot title
plt.xlabel('Age')
plt.ylabel('Salary Annually (USD)')
plt.title('Annual Salary of Developers by Age')

# Show the legend on the plot to indicate which bar represents which developer group
plt.legend()

# Uncomment the next line if you want to save the plot as an image file (e.g., plot.jpg)
# plt.savefig('plot.jpg')

# Display the plot on the screen
plt.show()
