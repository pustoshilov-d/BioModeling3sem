
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.colors import Normalize
from scipy.integrate import odeint
import numpy as np
import scipy
from numpy.linalg import eig
from scipy.optimize import minimize
import warnings
warnings.filterwarnings("default")

def model(r=1, K=2, a=2):
    #вид1
    dx = lambda x,y: -r*x*(1+x/K) + a*x*y
    #вид2
    dy = lambda x,y: -r*y*(1+y/K) + a*x*y
    return lambda p,t: [ dx(*p), dy(*p) ]


initialPoints = [0,0.5,1,3,10]

fig, ax = plt.subplots(figsize=(7,7))
lines = []
for i in range(len(initialPoints)**2):
  lines.append(ax.plot([],[])[0])
text = ax.text(0.7, 0.9, '0', fontsize=15, transform = ax.transAxes)


ax.set_xlim(0, 15)
ax.set_ylim(0, 15)
ax.set_xlabel('X')
ax.set_ylabel('Y')

tt = np.linspace(0,10000, 300000)

def animate(step):
    global r
    r=1; K=1; a=1
    # r = 0 + step/10
    # K = 0 + step/10
    a = 0 + step/10

    
    for x in range(len(initialPoints)):
      for y in range(len(initialPoints)):
        fun = model(r=r, K=K, a=a)
        zz = odeint(fun, [initialPoints[x],initialPoints[y]], tt)
        lines[x*len(initialPoints)+y].set_data(zz[:, 0], zz[:, 1])
        text.set_text('r=%.2f K=%.2f a=%.2f' % (r, K, a))

    return lines, text

anim = FuncAnimation(fig, animate, frames=50, interval=500, blit = False)


f = r"animationA.gif" 
writergif = PillowWriter(fps=30) 
anim.save(f, writer=writergif)


plt.show()
