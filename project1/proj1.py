import math
import time
import matplotlib.pyplot as plt
import ICM20948

# Initialize lists for storing data
times = []
x_data = []
y_data = []
z_data = []
timer = 0

# Setup the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
line1, = ax.plot([], [], label='X vs Time', color='r')
line2, = ax.plot([], [], label='Y vs Time', color='g')
line3, = ax.plot([], [], label='Z vs Time', color='b')

# Set up plot appearance
ax.set_xlim(0, 100)  # Adjust the x-axis range as needed
ax.set_ylim(-32768, 32768)  # Adjust based on accelerometer/gyroscope data range
ax.set_title('X, Y, Z vs Time')
ax.set_xlabel('Time')
ax.set_ylabel('Values')
ax.grid(True)
ax.legend()

# Update function for animation
def update(frame):
    global timer
    
    # Simulate the sensor readings and calculations
    icm20948.icm20948_Gyro_Accel_Read()
    icm20948.icm20948MagRead()
    icm20948.icm20948CalAvgValue()
    icm20948.imuAHRSupdate(MotionVal[0] * 0.0175, MotionVal[1] * 0.0175, MotionVal[2] * 0.0175,
                          MotionVal[3], MotionVal[4], MotionVal[5], 
                          MotionVal[6], MotionVal[7], MotionVal[8])

    pitch = math.asin(-2 * q1 * q3 + 2 * q0 * q2) * 57.3
    roll  = math.atan2(2 * q2 * q3 + 2 * q0 * q1, -2 * q1 * q1 - 2 * q2 * q2 + 1) * 57.3
    yaw   = math.atan2(-2 * q1 * q2 - 2 * q0 * q3, 2 * q2 * q2 + 2 * q3 * q3 - 1) * 57.3
    
    # Update time and sensor data
    times.append(timer)
    timer += 1
    x_data.append(Accel[0])
    y_data.append(Accel[1])
    z_data.append(Accel[2])

    # Update the plot data
    line1.set_data(times, x_data)
    line2.set_data(times, y_data)
    line3.set_data(times, z_data)

    # Adjust plot limits dynamically
    ax.set_xlim(max(0, timer - 100), timer + 10)  # Keep a rolling window of 100 data points

    return line1, line2, line3

# Animation object
ani = FuncAnimation(fig, update)

try:
    while True:
        time.sleep(0.1)  # Simulate the real-time nature of sensor data
except KeyboardInterrupt:
    print("Real-time data plotting interrupted.")

# Show the animated plot
plt.show()
