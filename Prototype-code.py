import matplotlib.pyplot as plt
import numpy as np
import time

# Initialize lists to store data
timestamps = []
temps = []
phs = []

# Create figure and axes
plt.ion()
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))
fig.suptitle("Real-time Temperature & pH Monitoring (Simulated)", fontsize=14)

# Set axes labels
ax1.set_ylabel("Temperature (°C)")
ax2.set_ylabel("pH Level")
ax2.set_xlabel("Time (s)")

start_time = time.time()

def detect_anomaly(temp, ph):
    return not (0 <= temp <= 60 and 6.0 <= ph <= 8.5)

for i in range(100):
    current_time = time.time() - start_time
    timestamps.append(current_time)

    # Simulate sensor values
    temp = np.random.normal(30, 5)  # mean=30°C, std=5
    ph = np.random.normal(7.2, 0.3)  # mean=7.2, std=0.3
    temps.append(temp)
    phs.append(ph)

    # Clear previous plots
    ax1.cla()
    ax2.cla()

    # Plot Temperature
    ax1.plot(timestamps, temps, label="Temperature (°C)", color="blue")
    ax1.set_ylabel("Temperature (°C)")
    if detect_anomaly(temp, ph):
        ax1.scatter(timestamps[-1], temp, color='red', label="Anomaly")

    # Plot pH
    ax2.plot(timestamps, phs, label="pH Level", color="green")
    ax2.set_ylabel("pH Level")
    ax2.set_xlabel("Time (s)")
    if detect_anomaly(temp, ph):
        ax2.scatter(timestamps[-1], ph, color='red', label="Anomaly")

    # Refresh plots
    ax1.legend()
    ax2.legend()
    plt.pause(0.5)

plt.ioff()
plt.show()

'''
This code simulates real-time data collection and visualization for temperature and pH levels.
It uses matplotlib to plot the data and highlights anomalies in red.
The data is generated using a normal distribution to simulate sensor readings.
The anomaly detection function checks if the temperature and pH values are within expected ranges.
The code runs for 100 iterations, simulating a continuous monitoring system.
The plots are updated in real-time, and anomalies are marked with red dots.   
The code uses interactive mode in matplotlib to allow for real-time updates.
The simulation runs for approximately 50 seconds, updating the plots every 0.5 seconds.
Note: This is a simulated environment. In a real application, you would replace the random data generation
with actual sensor readings from a temperature and pH sensor.
'''
