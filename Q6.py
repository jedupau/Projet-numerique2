import numpy as np
import matplotlib.pyplot as plt
def solve_euler_explicit(f, x0, dt, t0, tf):
    liste_t = []
    liste_x = []
    t = t0
    x = x0
    liste_t.append(t0)
    liste_x.append(x0)
    while t < tf:
        x += dt * f(t, x)
        t += dt
        liste_t.append(t)
        liste_x.append(x)
    t,x = np.array(liste_t), np.array(liste_x)
    return t, x

def f(t,x):
    return 1/t
plt.plot(np.linspace(0, 10, 101), solve_euler_explicit(f, 0, 0.1, 0.1, 10)[1])
plt.show()