import math
import time
import matplotlib.pyplot as plt
from ICM20948 import ICM20948
  
def adc_to_accel(adc_value):
    max_adc = 32768  # Signed 16-bit ADC values range from -32768 to 32768
    max_g = 2  # ±2g
    g_to_ms2 = 9.81  # 1g = 9.81 m/s²
    # Convert ADC value to acceleration in m/s^2
    accel = (adc_value / max_adc) * max_g * g_to_ms2
    
    return accel
    
if __name__ == '__main__':
    print("\nSense HAT Test Program ...\n")
    MotionVal=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    icm20948=ICM20948()
    
    x_data = []
    y_data = []
    z_data = []
    accel_angle = []
    times = []
    current_time = time.time()

    while True:
        icm20948.icm20948_Gyro_Accel_Read()
        icm20948.icm20948MagRead()
        icm20948.icm20948CalAvgValue()
        time.sleep(0.1)
        icm20948.imuAHRSupdate(MotionVal[0] * 0.0175, MotionVal[1] * 0.0175,MotionVal[2] * 0.0175,
                    MotionVal[3],MotionVal[4],MotionVal[5], 
                    MotionVal[6], MotionVal[7], MotionVal[8])
        # Gyro data
        pitch = math.asin(-2 * q1 * q3 + 2 * q0* q2)* 57.3
        roll  = math.atan2(2 * q2 * q3 + 2 * q0 * q1, -2 * q1 * q1 - 2 * q2* q2 + 1)* 57.3
        yaw   = math.atan2(-2 * q1 * q2 - 2 * q0 * q3, 2 * q2 * q2 + 2 * q3 * q3 - 1) * 57.3
        # Accel data
        accelx = adc_to_accel(Accel[0])
        accely = adc_to_accel(Accel[1])
        accelz = adc_to_accel(Accel[2])

        times.append(time.time() - current_time)

        x_data.append(accelx)
        y_data.append(accely)
        z_data.append(accelz)

        # angle = math.atan2(icm20948.adc_to_acceleration_ms2(Accel[2]), math.sqrt(icm20948.adc_to_acceleration_ms2(Accel[0])**2 + icm20948.adc_to_acceleration_ms2(Accel[1])**2)) * (180 / math.pi)
        angle = math.atan2(accely, math.sqrt(accelx**2 + accelz**2)) * (180 / math.pi)
        accel_angle.append(angle)

        # Create the figure and axes using plt.subplots()
        fig, ax = plt.subplots(figsize=(10, 6))  # Set the figure size

        ax.plot(times, x_data, label='X vs Time', color='r')             # Plot X vs Time
        ax.plot(times, y_data, label='Y vs Time', color='g')             # Plot Y vs Time
        ax.plot(times, z_data, label='Z vs Time', color='b')             # Plot Z vs Time

        # Plot of angular deviation from level using only acceleration data
        ax.plot(times, accel_angle, label='Angular Deviation', color='y')

        # Add grid
        ax.grid(True)

        # Add title and labels
        ax.set_title('X, Y, Z vs Time')
        ax.set_xlabel('Time')
        ax.set_ylabel('Values')

        # Add a legend
        ax.legend()

        # Show the plot
        plt.savefig('real_time.png')
