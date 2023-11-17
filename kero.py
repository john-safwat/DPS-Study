import matplotlib.pyplot as plt
import numpy as np

sampleFrequency = 300
time = 0

iterations = np.array([time])

for i in range(1, 100, 1):
    time += (1/sampleFrequency)
    iterations = np.append(iterations, time)

amplitude = 10 * np.cos(250 * iterations * np.pi)

plt.figure("Signal")
plt.plot(iterations, amplitude)
plt.title("Signal Plotting")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show()
