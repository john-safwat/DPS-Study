import matplotlib.pyplot as plt
import numpy as np

sampleFrequency = 300
timeSample = 0

# define the array of time samples
time = np.array([timeSample])

# loop to calculate the list of iteration (Time samples)
for i in range(1 , 100):
    timeSample += (1 / sampleFrequency)
    time = np.append(time, timeSample)


print(time)

# calculate the amplitude
amplitude = 10 * np.cos(250 * np.pi * time)

# define the figure to plot the graph in
figure = plt.figure("Sample Frequency")
plt.plot(time, amplitude)

# title
plt.title(" 10 * np.cos(250 * pi * time)")
plt.xlabel("Time")
plt.ylabel("Time")

plt.show()
