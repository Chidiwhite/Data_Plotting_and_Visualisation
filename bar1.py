import matplotlib.pyplot as plt
import csv
from collections import Counter

plt.style.use('dark_background')

# Read the data from the CSV file and count occurrences of each programming language
with open('file.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    # Create a Counter object to count the occurrences of each programming language
    language_counter = Counter()
    
    # Loop through each row in the CSV file
    for row in csv_reader:
        languages = row['LanguagesWorkedWith']
        # If the 'LanguagesWorkedWith' field is empty, skip to the next row
        if languages is None:
            pass
        else:
            # Split the languages by ';' and update the counter with the counts
            language_counter.update(languages.split(';'))
            
# Get the top 15 most common programming languages and their counts
top_languages = language_counter.most_common(15)
language = [item[0] for item in top_languages]
count = [item[1] for item in top_languages]

#wrong approach for plotting this data
# Create a bar chart to visualize the popularity of programming languages
plt.bar(language, count)

# Set the plot title, x-axis label, and y-axis label
plt.title('Popular Programming Languages')
plt.xlabel('Programming Languages')
plt.ylabel('Number of Users')

# Adjust the layout to fit the labels properly
plt.tight_layout()

# Display the plot on the screen
plt.show()
