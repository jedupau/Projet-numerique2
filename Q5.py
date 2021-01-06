alpha = 0.1
beta = 0.2
gamma = 0.1
delta = 0.1
import numpy as np
import matplotlib.pyplot as plt
def display_contour(f, x, y, levels):
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    fig, ax = plt.subplots()
    contour_set = plt.contour(
        X, Y, Z, colors="grey", linestyles="dashed", 
        levels=levels 
    )
    ax.clabel(contour_set)
    plt.grid(True)
    plt.xlabel("$x_1$") 
    plt.ylabel("$x_2$")
    plt.gca().set_aspect("equal")
def H(x,y):
    return(delta*x - gamma * np.log(x) + beta*y - alpha*np.log(y))

display_contour(H, np.linspace(0.1,2,20), np.linspace(0.1,2,20), 20)
plt.show()