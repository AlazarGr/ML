import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-8,8, 0.01)
y = (np.sin(2*x) * np.sin(3*x)) / (x/2)
plt.plot(x,y, "r")
plt.yticks([-3, -2, -1,0, 1, 2, 3, 4],
[r'$-3$', r'$-2$',r'$-1$',r'$0$',r'$+1$',r'$+2$', r'$+3$', r'$+4$'])
plt.show()