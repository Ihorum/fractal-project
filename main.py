import matplotlib.pyplot as plt
import numpy as np
a = int(input())
x = np.linspace(-a,a,a*2)
y = x**2
plt.plot(x,y)
plt.show()