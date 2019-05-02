# Import the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np

# Prepare the data
x = np.linspace(1, 10, 20)

for i in x:
    print(i)

# Plot the data
# xdata, ydata, linewidth=None, linestyle=None, color=None, marker=None, markersize=None,
# markeredgewidth=None, markeredgecolor=None, markerfacecolor=None, markerfacecoloralt='none', 
# fillstyle=None, antialiased=None, dash_capstyle=None, solid_capstyle=None, dash_joinstyle=None, 
# solid_joinstyle=None, pickradius=5, drawstyle=None, markevery=None, **kwargs)
plt.plot(x, x, label='linear', marker='s', color='lightgreen', linestyle='none', markersize=5.5)    
                                        
                                        # x por y (neste caso x está na posição de y) e o label
                                        # legal. quando é passado nome parametro, outros recursos podem ser
                                        # passados depois, estilo hash

# Add a legend
plt.legend()                        # legenda disponivel no mapa passado pelo parametro 'label'

# Show the plot
plt.show()

""" 
tags:

        ## plt.plot(paramns)
label
color
marker: o, *, s, +, ...             https://matplotlib.org/api/markers_api.html
linestyle: none, dashed, solid
linewidth; tam line. 0.1 ... x
markersize: tam marker. 0.1 ... x

lines                               https://matplotlib.org/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_linestyle
obs: linestyle='none', marker='x' === 'x' (posição 3)
'bo' circulo azul
'ro' circulo vermelho

color com light<color> são claras 
 """