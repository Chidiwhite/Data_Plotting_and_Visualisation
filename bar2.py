import matplotlib as mpl
import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd

plt.style.use('dark_background')

# Read data from the CSV file using pandas
data = pd.read_csv('file.csv')

# Extract the 'LanguagesWorkedWith' column from the data
responses = data['LanguagesWorkedWith']

# Create a Counter object to count the occurrences of each programming language
language_counter = Counter()

# Loop through each response in the 'LanguagesWorkedWith' column
for response in responses:
    # Check if the response is a string (to handle potential missing values)
    if isinstance(response, str):
        # Split the response by ';' and update the counter with the counts
        language_counter.update(response.split(';'))

# Get the top 15 most common programming languages and their counts
top_languages = language_counter.most_common(15)
language = [item[0] for item in top_languages]
count = [item[1] for item in top_languages]

#Right approach for plotting this data
# Create a horizontal bar chart to visualize the popularity of programming languages
plt.barh(language, count)

# Set the plot title, y-axis label, and x-axis label
plt.title('Popular Programming Languages')
plt.ylabel('Programming Languages')
plt.xlabel('Number of Users')

# Adjust the layout to fit the labels properly
plt.tight_layout()

# Display the plot on the screen
plt.show()
