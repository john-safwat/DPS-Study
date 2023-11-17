import matplotlib.pyplot as plt
import numpy as np

# define the time array and amplitude array for plotting the signal
time = np.array([-1, 0, 1, 2])  # X-Ais
amplitude = np.array([1, 1, 0.5, 1])  # Y-Ais

# define the figure to display plots in
figure = plt.figure("Display Changes in Each Operation")  # The Name of the Figure

# Set The position of SubPlot Using add_subplot Function
# The position is specified with the number of rows , Columns, and It's index in figure Grid View
# add_subplot(*Number of rows*, *Number of columns*, *Subplot index*) -> figure.add_subplot(3, 1, (1, 2))
# An Axes object encapsulates all the elements of an individual (sub-)plot in figure.
originalSignalSubPlot = figure.add_subplot(3, 2, 1)
# pass time and amplitude values to be plotted
originalSignalSubPlot.stem(time, amplitude)
# set plot tile above the plot
plt.title("Original Signal")


# Plot inverse
# reverse the time array using the inverse operator in numpy package
timeInverse = -time
# Set The position of SubPlot Using add_subplot Function
timeInversePlot = figure.add_subplot(3, 2, 2)
# pass time and amplitude values to be plotted
timeInversePlot.stem(timeInverse, amplitude)
# set plot tile above the plot
plt.title("Inverse Plot")


# delay by 2
# Delay the time array using the + operator in numpy package
timeDelay = time+2
# Set The position of SubPlot Using add_subplot Function
timeDelayPlot = figure.add_subplot(3, 2, 3)
# pass time and amplitude values to be plotted
timeDelayPlot.stem(timeDelay, amplitude)
# set plot tile above the plot
plt.title("Delay Plot")


# advance by 2
# Advance the time array using the - operator in numpy package
timeAdvance = time-2
# Set The position of SubPlot Using add_subplot Function
timeAdvancePlot = figure.add_subplot(3, 2, 4)
# pass time and amplitude values to be plotted
timeAdvancePlot.stem(timeAdvance, amplitude)
# set plot tile above the plot
plt.title("Advance Plot")


# compress signal
# compress signal using the / operator in numpy Package
timeCompress = time/2
# Set The position of SubPlot Using add_subplot Function
timeCompressPlot = figure.add_subplot(3, 2, 5)
# pass time and amplitude values to be plotted
timeCompressPlot.stem(timeCompress, amplitude)
# set plot tile above the plot
plt.title("Compressed Plot")


# Expanded
# Expand signal using the * operator in numpy Package
timeExpand = time*2
# Set The position of SubPlot Using add_subplot Function
timeExpandPlot = figure.add_subplot(3, 2, 6)
# pass time and amplitude values to be plotted
timeExpandPlot.stem(timeExpand, amplitude)
# set plot tile above the plot
plt.title("Expanded Plot")

# Function From PyLab Package to Display the Plots Figure
plt.show()
