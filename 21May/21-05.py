import matplotlib.pyplot as plt
import pandas as pd

# Data for distance = 165 cm, now treating power values as negative dB
data = [
    (0, 0, -74.38),
    (0, 10, -65.00),
    (0, 20, -54.50),
    (0, 30, -45.50),
    (0, 40, -37.63),
    (10, 0, -68.38),
    (10, 10, -60.50),
    (10, 20, -50.00),
    (10, 30, -37.25),
    (10, 40, -26.00),
    (20, 0, -57.50),
    (20, 10, -47.00),
    (20, 20, -35.00),
    (20, 30, -25.63),
    (20, 40, -17.38),
    (30, 0, -56.38),
    (30, 10, -41.75),
    (30, 20, -31.63),
    (30, 30, -21.13),
    (30, 40, -15.50),
]

# Create DataFrame
df = pd.DataFrame(data, columns=["Tx Gain (dB)", "Rx Gain (dB)", "Power (dB)"])

# Pivot the table for plotting
pivot_df = df.pivot(index="Rx Gain (dB)", columns="Tx Gain (dB)", values="Power (dB)")

# Plotting
plt.figure(figsize=(10, 6))
for tx_gain in pivot_df.columns:
    plt.plot(pivot_df.index, pivot_df[tx_gain], marker='o', label=f"TX Gain = {tx_gain} dB")

plt.title("Received Power (Negative dB) at 165 cm vs RX Gain for Different TX Gains")
plt.xlabel("RX Gain (dB)")
plt.ylabel("Received Power (dB)")
plt.grid(True)
plt.legend(title="TX Gain")
plt.tight_layout()
plt.show()
