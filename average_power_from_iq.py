import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# === Load IQ data ===
iq = np.fromfile(r"C:\Users\Siddhant Jinturkar\OneDrive\Desktop\rx_output_10cm.cfile", dtype=np.complex64)
power_db = 10 * np.log10(np.abs(iq)**2 + 1e-12)

# === Ignore first 30,000 samples due to error spike ===
start_index = 30_000
power_db_valid = power_db[start_index:]

# === Smooth power curve to reduce noise ===
smoothed = np.convolve(power_db_valid, np.ones(1000)/1000, mode='valid')

# === Automatically detect burst start using threshold ===
threshold = -50  # dB — power should rise above this during burst
peaks, _ = find_peaks(smoothed, height=threshold)

if len(peaks) == 0:
    print("❌ No burst detected.")
    exit()

burst_start = peaks[0]           # Index in smoothed array
burst_length = 20_000            # ~50 ms at 1 MS/s (adjust if needed)
burst_end = burst_start + burst_length

# === Clamp to array bounds ===
burst_start = max(burst_start, 0)
burst_end = min(burst_end, len(power_db_valid))

# === Convert burst indices back to original power_db indexing ===
burst_start_orig = burst_start + start_index
burst_end_orig = burst_end + start_index

# === Compute average burst power ===
burst_power = power_db[burst_start_orig:burst_end_orig]
avg_burst_power = np.mean(burst_power)

# === Plot power and burst region ===
plt.figure(figsize=(10, 5))
plt.plot(power_db, label="Power (dB)")
plt.axvspan(burst_start_orig, burst_end_orig, color='yellow', alpha=0.3, label="Detected Burst")
plt.axhline(avg_burst_power, color='red', linestyle='--', label=f'Avg Burst Power: {avg_burst_power:.2f} dB')
plt.title("Automatically Detected Burst and Average Power (Ignoring first 30k samples)")
plt.xlabel("Sample Index")
plt.ylabel("Power (dB)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

print(f"✅ Detected burst from sample {burst_start_orig} to {burst_end_orig}")
print(f"✅ Average power during burst: {avg_burst_power:.2f} dB")
