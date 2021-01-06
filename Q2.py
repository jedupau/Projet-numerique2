from math import sin, cos
from numpy import linspace, meshgrid
from matplotlib.pyplot import quiver, show, streamplot
alpha = 0.1
beta = 0.2
gamma = 0.1
delta = 0.1
def f(x,y):
    return x*(alpha - beta*y), -y*(gamma - delta * x)
x, y = meshgrid(linspace(0, 2, 20), linspace(0, 2, 20))
dx, dy = f(x, y)
quiver(x, y, dx, dy)
streamplot(x,y,dx,dy)
show()