# Import the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np

# Create a Figure
fig = plt.figure()

# Set up Axes
ax = fig.add_subplot(321)

# Scatter the data
ax.scatter(np.linspace(5, 15, 15), np.linspace(0, 15, 15))

# Set up Axes
ax2 = fig.add_subplot(322)

# Scatter the data
ax2.scatter(np.linspace(5, 15, 15), np.linspace(0, 15, 15))

# Set up Axes
ax3 = fig.add_subplot(323)

# Scatter the data
ax3.scatter(np.linspace(5, 15, 15), np.linspace(0, 15, 15))

# Set up Axes
ax4 = fig.add_subplot(324)

# Scatter the data
ax4.scatter(np.linspace(5, 15, 15), np.linspace(0, 15, 15))

# Set up Axes
ax5 = fig.add_subplot(325)

# Scatter the data
ax5.scatter(np.linspace(5, 15, 15), np.linspace(0, 15, 15))

# Show the plot
plt.show()

""" 
add_supplot -> 3 numeros 
primeiro: lines
segundo: collumns
terceiro seria um dos possiveis locais a se posicionar, respeitando a linha de lines x collumns
se 32 então 3 x 2 = 6. Logo terceiro pode ser de 1 a 6
 """