
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import odeint
import numpy as np
import scipy


A = 1.0; B = 3.0; k1 = 2.0; km1 = 2.0; k3 = 3.0
# k2 = 1.8
# change k3

P = lambda x,y,k2: k1*A - (km1 + k2*B)*x + k3*x**2*y
Q = lambda x,y,k2: k2*B*x - k3*x**2*y

fun = lambda p,t,k2: [ P(*p, k2), Q(*p, k2) ]

fig, ax = plt.subplots()

line, = ax.plot([], '-')


ax.set_xlim(0,3)
ax.set_ylim(0,3)
ax.set_xlabel('X')
ax.set_ylabel('Y')
fn=1


def animate(fn):
  tt = np.linspace(0,100, 1000)
  zz = odeint(fun, [1.0, 4.0], tt, args=(.8+1./100*fn,))
  line.set_data(zz[:,0], zz[:,1])
  return line

    
anim = FuncAnimation(fig, animate, frames=100, interval=50)

plt.show()