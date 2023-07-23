import matplotlib as mpl
import matplotlib.pyplot as plt

# Use the 'dark_background' style for the plot
plt.style.use('dark_background')
# If you want to create a plot with an xkcd style, uncomment the next line
# plt.xkcd()

# Define the ages and their corresponding salaries for Python, Java, C, and Perl developers
ages = [23, 24, 25, 26, 27, 28, 29, 30, 31, 32]
py_salary = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
java_salary = [25000, 35000, 45000, 55000, 65000, 75000, 85000, 95000, 105000, 110000]
c_salary = [12300, 14300, 15300, 16300, 17300, 18300, 19500, 20500, 10500, 20500]
perl_salary = [14700, 16800, 17900, 19200, 12200, 20100, 15430, 18470, 23990, 34800]

# Create bar and line plots to visualize the salaries of different language developers by age
plt.bar(ages, py_salary, label='python devs', color='y')
plt.plot(ages, java_salary, label='java devs', color='b', marker='o')
plt.plot(ages, c_salary, label='C devs', color='c', marker='p')
plt.plot(ages, perl_salary, label='perl devs', color='r', marker='*')

# Set the labels for the x-axis and y-axis and the plot title
plt.xlabel('Age')
plt.ylabel('Salary Annually (USD)')
plt.title('Annual Salary of Developers by Age')

# Display the legend on the plot to indicate which line represents which language developer
plt.legend()

# Uncomment the next line if you want to save the plot as an image file (e.g., plot.jpg)
# plt.savefig('plot.jpg')

# Display the plot on the screen
plt.show()
