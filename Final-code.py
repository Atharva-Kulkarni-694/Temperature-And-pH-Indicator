import serial
import matplotlib.pyplot as plt
import time

# Connect to Arduino (check your COM port)
ser = serial.Serial('COM3', 9600)  # Change COM port as needed
time.sleep(2)

temps = []
phs = []
timestamps = []

plt.ion()
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))
fig.suptitle("Live Sensor Data: Temperature and pH")

start_time = time.time()

def detect_anomaly(temp, ph):
    return not (0 <= temp <= 60 and 6.0 <= ph <= 8.5)

while True:
    try:
        raw = ser.readline().decode().strip()
        temp, ph = map(float, raw.split(","))
        now = time.time() - start_time

        temps.append(temp)
        phs.append(ph)
        timestamps.append(now)

        ax1.cla()
        ax2.cla()

        ax1.plot(timestamps, temps, color='blue')
        ax1.set_ylabel("Temperature (°C)")
        if detect_anomaly(temp, ph):
            ax1.scatter(timestamps[-1], temp, color='red', label='Anomaly')
        ax1.legend()

        ax2.plot(timestamps, phs, color='green')
        ax2.set_ylabel("pH Level")
        ax2.set_xlabel("Time (s)")
        if detect_anomaly(temp, ph):
            ax2.scatter(timestamps[-1], ph, color='red', label='Anomaly')
        ax2.legend()

        plt.pause(0.5)

    except Exception as e:
        print("Error:", e)



# Close the serial connection when done
ser.close() # plt.ioff()
plt.show()  # Keep the plot open    