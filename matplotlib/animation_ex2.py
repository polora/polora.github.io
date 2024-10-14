import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib.animation import FuncAnimation  
   
# initialisation de la figure
fig = plt.figure()  
   
# initialisation des axes
axis = plt.axes(xlim =(0, 4),  
                ylim =(-2, 2))  
  
# initialisation de la variable objet ligne
line, = axis.plot([], [], lw = 3)  
   
# data which the line will contain (x, y) 
def init():  
    line.set_data([], []) 
    return line, 
   
def animate(i): 
    x = np.linspace(0, 4, 1000) 
   
    # plots a sine graph 
    y = np.sin(2 * np.pi * (x - 0.01 * i)) 
    line.set_data(x, y) 
      
    return line, 
   
anim = FuncAnimation(fig, animate, init_func = init, 
                     frames = 200, interval = 20, blit = True) 

plt.show()