import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



# Load the Excel file
file_path = r"C:\Users\Siddhant Jinturkar\OneDrive\Desktop\5G Research\2705.xlsx"  # Update if needed
df = pd.read_excel(file_path)

# Convert timestamp to numeric if needed
df['timestamp'] = pd.to_numeric(df['timestamp'], errors='coerce')
df = df.dropna(subset=['timestamp'])

# Define distance groups and how many samples per group
distances_cm = [75, 20, 30, 40, 50, 60]
samples_distribution = [59, 59, 59, 59, 60, 60]  # Must sum to total rows
distance_labels = []

for dist, count in zip(distances_cm, samples_distribution):
    distance_labels.extend([dist] * count)

distance_labels = distance_labels[:len(df)]  # Ensure matching length
df['distance_cm'] = distance_labels

# Group by distance and compute average power
avg_power_by_distance = df.groupby('distance_cm')['avg_power_dB'].mean().reset_index()

# Plot
plt.figure(figsize=(8, 6))
plt.plot(avg_power_by_distance['distance_cm'], avg_power_by_distance['avg_power_dB'], marker='o')
plt.xlabel('Distance (cm)')
plt.ylabel('Average Power (dB)')
plt.title('Average Received Power vs Distance')
plt.grid(True)
plt.tight_layout()
plt.show()

from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

# Prepare data
x = avg_power_by_distance['distance_cm'].values
y = avg_power_by_distance['avg_power_dB'].values

# Path loss model
def path_loss_model(d, P0, n):
    return P0 - 10 * n * np.log10(d / 20)  # reference distance d0 = 20 cm

try:
    # Add initial guesses: P0 near max power, n between 2–4
    params, _ = curve_fit(path_loss_model, x, y, p0=[max(y), 2.0])
    P0_fit, n_fit = params
    print(f"Estimated P0 = {P0_fit:.2f} dB, Path loss exponent n = {n_fit:.2f}")

    # Plot data and fitted model
    d_fit = np.linspace(min(x), max(x), 100)
    y_fit = path_loss_model(d_fit, *params)

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, 'o', label='Measured Data')
    plt.plot(d_fit, y_fit, '-', label='Fitted Path Loss Model')
    plt.xlabel('Distance (cm)')
    plt.ylabel('Average Power (dB)')
    plt.title('Path Loss Model Fit')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

except Exception as e:
    print("Curve fitting failed:", e)

