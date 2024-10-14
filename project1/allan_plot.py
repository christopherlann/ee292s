import numpy as np
import matplotlib.pyplot as plt
import allantools

def adc_to_accel(adc_value):
    max_adc = 32768  # Signed 16-bit ADC values range from -32768 to 32768
    max_g = 2  # ±2g
    g_to_ms2 = 9.81  # 1g = 9.81 m/s²
    return (adc_value / max_adc) * max_g * g_to_ms2

def adc_to_gyro(adc_value):
    max_adc = 32768  # Signed 16-bit ADC values range from -32768 to 32768
    max_dps = 1000
    # Convert ADC value to acceleration in g's
    dps = (adc_value / max_adc) * max_dps    
    return dps

data = np.loadtxt('data2.csv', delimiter=',', skiprows=1)

accel_x = data[:, 1]  # AccelX
accel_y = data[:, 2]  # AccelY
accel_z = data[:, 3]  # AccelZ
gyro_x = data[:, 4]   # GyroX
gyro_y = data[:, 5]   # GyroY
gyro_z = data[:, 6]   # GyroZ

sampling_rate = 2.2  # Hz

datasets = [accel_x, accel_y, accel_z, gyro_x, gyro_y, gyro_z]
labels = ['AccelX', 'AccelY', 'AccelZ', 'GyroX', 'GyroY', 'GyroZ']

# Iterate over datasets to compute and save Allan deviation plots
for i, data in enumerate(datasets):
    # Calculate Allan deviation using allantools
    (tau_out, adev, adeverr, n) = allantools.adev(data, rate=sampling_rate, data_type="freq", taus="decade")

    # Create a new figure for each dataset
    plt.figure(figsize=(10, 6))
    plt.loglog(tau_out, adev, label=f'Allan Deviation - {labels[i]}', color='b')
    plt.xlabel('Integration Time Tau (s)')

    if 'accel' in labels[i].lower():
        plt.ylabel('Allan Deviation (m/s^2)')
    else:
        plt.ylabel('Allan Deviation (dps)')

    plt.title(f'Allan Deviation vs. Integration Time ({labels[i]})')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.legend()

    # Save the plot as a PNG file
    plt.savefig(f'allan_deviation_{labels[i]}.png', format='png')

    # Close the plot to free up memory
    plt.close()

print("Plots saved successfully.")

