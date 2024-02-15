import matplotlib.pyplot  as plt
import numpy as np
from math import *
def func(n):
    return ((sqrt(2*pi*n))*(pow(n/e,n)))

x=[p for p in range(0,10**1 +1)]
x=np.linspace(0,100)

y=[func(i) for i in x]
plt.plot(x,y,label="nothing")
plt.legend()
plt.grid()
plt.show()

# x = np.linspace(0, 1, 100)

# # Generate actual derivative and finite difference approximation values
# f_prime_values = [f_prime(val) for val in x]
# delta_plus_values = [delta_plus(f, val, h=0.01) for val in x]

# # Plot actual derivative and finite difference approximation
# plt.figure(figsize=(12, 6))
# plt.plot(x, f_prime_values, label="Actual Derivative")
# plt.plot(x, delta_plus_values, '--', label="Finite Difference Approximation")
# plt.xlabel('x') 
# plt.ylabel('f\'(x)')
# plt.title('Actual Derivative vs Forward Finite Difference Approximation of sin(x^2)')
# plt.legend()
# plt.grid()
plt.show()