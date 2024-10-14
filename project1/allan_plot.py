import numpy as np
import matplotlib.pyplot as plt
import allantools

data = np.loadtxt('data.csv', delimiter=',', skiprows=1)

accel_x = data[:, 0]  # AccelX
accel_y = data[:, 1]  # AccelY
accel_z = data[:, 2]  # AccelZ
gyro_x = data[:, 3]   # GyroX
gyro_y = data[:, 4]   # GyroY
gyro_z = data[:, 5]   # GyroZ

sampling_rate = 5  # Hz

datasets = [accel_x, accel_y, accel_z, gyro_x, gyro_y, gyro_z]
labels = ['AccelX', 'AccelY', 'AccelZ', 'GyroX', 'GyroY', 'GyroZ']

# Iterate over datasets to compute and save Allan deviation plots
for i, data in enumerate(datasets):
    # Calculate Allan deviation using allantools
    taus, adev, errors, additional_info = allantools.adev(data, rate=sampling_rate, data_type="freq")

    # Create a new figure for each dataset
    plt.figure(figsize=(10, 6))
    plt.loglog(taus, adev * 1e9, label=f'Allan Deviation - {labels[i]}', color='b')  # Convert to ppb
    plt.xlabel('Integration Time (s)')
    plt.ylabel('Allan Deviation (ppb)')
    plt.title(f'Allan Deviation vs. Integration Time ({labels[i]})')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.legend()

    # Save the plot as a PNG file
    plt.savefig(f'allan_deviation_{labels[i]}.png', format='png')

    # Close the plot to free up memory
    plt.close()

print("Plots saved successfully.")

