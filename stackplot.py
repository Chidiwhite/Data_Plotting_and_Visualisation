import matplotlib.pyplot as plt
import matplotlib as mpl

# Use the 'fivethirtyeight' style for the plot
plt.style.use('fivethirtyeight')

# Define the time intervals (minutes) and the corresponding data for each player
minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
player2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
player3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]

# Define the labels and colors for the players
labels = ['player1', 'player2', 'player3']
colors = ['blue', 'green', 'yellow']

# Create a stacked area plot to visualize the performance of each player over time
plt.stackplot(minutes, player1, player2, player3, labels=labels, colors=colors)

# Display the legend on the plot to indicate which area represents each player
plt.legend()

# Show the plot on the screen
plt.show()
