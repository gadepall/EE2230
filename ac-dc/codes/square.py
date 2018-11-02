import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
A = 30  # wave amplitude

T =0.02  # wave period  

t = np.linspace(-2.5*T,2.5*T,int(1e4))
plt.plot(t,A/2 *(signal.square(2*np.pi*t/T,0.5)))

plt.ylim(-20,20)
plt.grid()
plt.xlabel('$t(msec)$')
plt.ylabel('$X(t)$')
plt.savefig('square.eps')
plt.show()
