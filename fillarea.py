import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

# Read data from 'data.csv' file into a DataFrame
data = pd.read_csv('data.csv')

# Extract data for different variables from the DataFrame
age = data['Age']
all_devs = data['All_Devs']
py_salaries = data['Python']
java_salaries = data['JavaScript']

# Plot lines for all developers, Python developers, and JavaScript developers against age
plt.plot(age, all_devs, label='All devs')
plt.plot(age, py_salaries, label='Python')
plt.plot(age, java_salaries, label='JavaScript')

# Define a salary value as the meridian
meridian = 65000

# Fill the area between Python and JavaScript salaries with different colors based on comparison with the meridian
plt.fill_between(age, py_salaries, java_salaries, where=py_salaries > java_salaries, color='pink', label='above_avg')
plt.fill_between(age, py_salaries, java_salaries, where=py_salaries < java_salaries, color='black', label='below_avg')

# Set the title, x-axis label, and y-axis label for the plot
plt.title('Salaries')
plt.xlabel('Age')
plt.ylabel('Salary')

# Add a legend to the plot to differentiate the lines and filled areas
plt.legend()

# Display the plot
plt.show()
