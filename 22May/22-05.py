import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file (make sure this file is in the same directory or provide full path)
file_path = r"C:\Users\Siddhant Jinturkar\OneDrive\Desktop\5G Research\2705.xlsx"

# Read Excel sheet
df = pd.read_excel(file_path)  # This reads the first sheet by default

# Convert necessary columns to numeric (safe conversion)
df['tx_gain'] = pd.to_numeric(df['tx_gain'], errors='coerce')
df['rx_gain'] = pd.to_numeric(df['rx_gain'], errors='coerce')
df['avg_power_dB'] = pd.to_numeric(df['avg_power_dB'], errors='coerce')

# Drop rows with missing values
df.dropna(subset=['tx_gain', 'rx_gain', 'avg_power_dB'], inplace=True)

# Plot: Received Power vs RX Gain for Different TX Gains
plt.figure(figsize=(10, 6))

for tx in sorted(df['tx_gain'].unique()):
    subset = df[df['tx_gain'] == tx]
    avg_power_by_rx = subset.groupby('rx_gain')['avg_power_dB'].mean()
    plt.plot(avg_power_by_rx.index, avg_power_by_rx.values, marker='o', label=f'TX Gain = {int(tx)} dB')

plt.title('Received Power (dB) vs RX Gain for Different TX Gains')
plt.xlabel('RX Gain (dB)')
plt.ylabel('Received Power (dB)')
plt.grid(True)
plt.legend(title='TX Gain')
plt.tight_layout()
plt.show()
