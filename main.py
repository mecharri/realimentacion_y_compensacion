import numpy as np
import matplotlib.pyplot as plt
import control as ctl
import symbolic

s = ctl.TransferFunction.s
P1 = 50
P2 = 100
P3 = 10
G = 100000/((s+P1)*(s+P2)*(s+P3))
k = 0.1
H = G/(1+k*G)
print(H)
x_polos = ctl.pole(H).real
y_polos = ctl.pole(H).imag

x_zeros = ctl.zero(H).real
y_zeros = ctl.zero(H).imag

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(x_polos,y_polos,marker="x")
ax.scatter(x_zeros, y_zeros, marker="o")
plt.show()