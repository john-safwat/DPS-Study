import numpy as np
import matplotlib.pyplot as plt


t = np.linspace(0, 0.33, 100)

x_t = 10 * np.cos(100 * np.pi * t + 150 * np.pi * t)


plt.figure("Figure")
plt.plot(t, x_t)
plt.title('Original Signal: $x(t) = 10 \cos(100\pi t + 150\pi t)$')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()