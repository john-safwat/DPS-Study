import matplotlib.pyplot as plt
import numpy as np

sampleFrequency = 20
time = 0

timeIterations = np.array([time])

for i in range(1, 80, 1):
    time += (1/sampleFrequency)
    timeIterations = np.append(timeIterations, time)


amplitude = 2 * np.cos(3 * np.pi * timeIterations)


figure = plt.figure("Sample Frequency for 80 Sample")

plt.plot(timeIterations, amplitude)
plt.title("X(t) = 2Cos(3 Pi t)")
plt.xlabel("Time")
plt.ylabel("Amplitude")

plt.show()
