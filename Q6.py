import numpy as np
import matplotlib.pyplot as plt
def solve_euler_explicit(f, x0, dt, t0, tf):
    t = [t0]
    x = [x0]
    while t[-1] < tf:
        t.append(t[-1] + dt)
        x.append(x[-1] + dt * f(t, x[-1]))
    t,x = np.array(t), np.array(x)
    return t, x

def f(t,x):
    return x
sol = solve_euler_explicit(f, np.array([1]), 0.01, 0, 10)
plt.plot(sol[0], sol[1])
plt.show()