import math
import time
import matplotlib.pyplot as plt
from ICM20948 import ICM20948  # Correct import

def adc_to_accel(adc_value):
    max_adc = 32768  # Signed 16-bit ADC values range from -32768 to 32768
    max_g = 2  # ±2g
    g_to_ms2 = 9.81  # 1g = 9.81 m/s²
    return (adc_value / max_adc) * max_g * g_to_ms2

if __name__ == '__main__':
    print("\nSense HAT Test Program ...\n")
    MotionVal = [0.0]*9
    icm20948 = ICM20948()

    x_data, y_data, z_data, accel_angle, times = [], [], [], [], []
    current_time = time.time()

    fig, ax = plt.subplots(figsize=(10, 6))  # Create figure outside the loop

    try:
        while True:
            icm20948.icm20948_Gyro_Accel_Read()
            icm20948.icm20948MagRead()
            icm20948.icm20948CalAvgValue()
            time.sleep(0.1)

            # Gyro data calculations
            pitch = math.asin(-2 * q1 * q3 + 2 * q0 * q2) * 57.3
            roll = math.atan2(2 * q2 * q3 + 2 * q0 * q1, -2 * q1 * q1 - 2 * q2 * q2 + 1) * 57.3
            yaw = math.atan2(-2 * q1 * q2 - 2 * q0 * q3, 2 * q2 * q2 + 2 * q3 * q3 - 1) * 57.3

            # Accel data
            accelx = adc_to_accel(Accel[0])
            accely = adc_to_accel(Accel[1])
            accelz = adc_to_accel(Accel[2])

            times.append(time.time() - current_time)
            x_data.append(accelx)
            y_data.append(accely)
            z_data.append(accelz)

            angle = math.atan2(accely, math.sqrt(accelx**2 + accelz**2)) * (180 / math.pi)
            accel_angle.append(angle)

            # Limit data points for efficient plotting
            max_points = 1000
            times, x_data, y_data, z_data, accel_angle = (
                times[-max_points:], x_data[-max_points:], y_data[-max_points:], z_data[-max_points:], accel_angle[-max_points:]
            )

            # Clear and plot the new data
            ax.clear()
            ax.plot(times, x_data, label='X vs Time', color='r')
            ax.plot(times, y_data, label='Y vs Time', color='g')
            ax.plot(times, z_data, label='Z vs Time', color='b')
            ax.plot(times, accel_angle, label='Angular Deviation', color='y')
            ax.grid(True)
            ax.set_title('X, Y, Z vs Time')
            ax.set_xlabel('Time')
            ax.set_ylabel('Values')
            ax.legend()

            # Update the plot
            plt.pause(0.1)

    except Exception as e:
        print(f"Error: {e}")

    # Save the final plot
    plt.savefig('real_time.png')
