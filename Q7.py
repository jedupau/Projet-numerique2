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

alpha = 0.1
beta = 0.2
gamma = 0.1
delta = 0.1
def f(t, X):
    return np.array([X[0]*(alpha - beta*X[1]), -X[1]*(gamma - delta * X[0])])
sol = solve_euler_explicit(f, np.array([0.1 ,0.1]), 0.01, 0, 100)
plt.plot(sol[0], sol[1])
plt.show()