import numpy as np
import matplotlib.pyplot as plt
import control as ctl
# import symbolic

s = ctl.TransferFunction.s
P1 = 1e3
P2 = 100e3
P3 = 500e3
A0 = 1e3
G = A0/((s/P1+1)*(s/P2+1)*(s/P3+1))
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
# ax.scatter(x_zeros, y_zeros, marker="o")

tvec = np.linspace(0,1000,1000)
tvec, yout= ctl.step_response(H, tvec)

plt.figure()
ctl.bode(H, dB=1, deg =1, margins=1)

fig2 = plt.figure()
ax2 = fig2.add_subplot(1,1,1)
ax2.plot(tvec,yout)
plt.show()