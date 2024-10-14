import csv

def calculate_average_sampling_rate(file_path):
    # Read the timestamps from the CSV file
    timestamps = []
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip the header row
        for row in reader:
            timestamps.append(float(row[0]))

    # Calculate the time intervals between consecutive samples
    time_intervals = [
        timestamps[i+1] - timestamps[i] for i in range(len(timestamps) - 1)
    ]

    # Calculate the average sampling rate (samples per second)
    if len(time_intervals) == 0:
        print("Insufficient data to calculate the sampling rate.")
        return None

    average_interval = sum(time_intervals) / len(time_intervals)
    average_sampling_rate = 1 / average_interval

    print(f"Average Sampling Rate: {average_sampling_rate:.2f} Hz")
    return average_sampling_rate

# Path to the CSV file
file_path = 'data2.csv'

# Calculate the average sampling rate
calculate_average_sampling_rate(file_path)


# import csv
# import matplotlib.pyplot as plt

# def plot_sampling_rate(file_path):
#     # Read the timestamps from the CSV file
#     timestamps = []
#     with open(file_path, 'r') as csv_file:
#         reader = csv.reader(csv_file)
#         next(reader)  # Skip the header row
#         for row in reader:
#             timestamps.append(float(row[0]))

#     # Calculate the time intervals and sampling rates between consecutive samples
#     time_intervals = [
#         timestamps[i+1] - timestamps[i] for i in range(len(timestamps) - 1)
#     ]
#     sampling_rates = [1 / interval for interval in time_intervals]

#     # Plot the sampling rates
#     plt.figure(figsize=(10, 6))
#     plt.plot(range(1, len(sampling_rates) + 1), sampling_rates, marker='o', linestyle='-')
#     plt.title('Sampling Rate Between Consecutive Samples')
#     plt.xlabel('Sample Index')
#     plt.ylabel('Sampling Rate (Hz)')
#     plt.grid()
#     plt.show()

# # Path to the CSV file
# file_path = 'data2.csv'

# # Plot the sampling rate
# plot_sampling_rate(file_path)

# import csv
# import matplotlib.pyplot as plt

# def save_sampling_rate_plot(file_path, output_image_path):
#     # Read the timestamps from the CSV file
#     timestamps = []
#     with open(file_path, 'r') as csv_file:
#         reader = csv.reader(csv_file)
#         next(reader)  # Skip the header row
#         for row in reader:
#             timestamps.append(float(row[0]))

#     # Calculate the time intervals and sampling rates between consecutive samples
#     time_intervals = [
#         timestamps[i+1] - timestamps[i] for i in range(len(timestamps) - 1)
#     ]
#     sampling_rates = [1 / interval for interval in time_intervals]

#     # Plot the sampling rates
#     plt.figure(figsize=(10, 6))
#     plt.plot(range(1, len(sampling_rates) + 1), sampling_rates, marker='o', linestyle='-')
#     plt.title('Sampling Rate Between Consecutive Samples')
#     plt.xlabel('Sample Index')
#     plt.ylabel('Sampling Rate (Hz)')
#     plt.grid()

#     # Save the plot as a .png file
#     plt.savefig(output_image_path, format='png')
#     plt.close()

# # Path to the CSV file
# file_path = 'data2.csv'

# # Path to save the output image
# output_image_path = 'sampling_rate_plot.png'

# # Save the sampling rate plot
# save_sampling_rate_plot(file_path, output_image_path)
