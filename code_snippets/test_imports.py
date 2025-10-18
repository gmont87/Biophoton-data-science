import numpy as np
import matplotlib.pyplot as plt

print("NumPy and Matplotlib are working!")

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title("Test Plot")
plt.show()


