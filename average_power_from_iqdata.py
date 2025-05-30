import numpy as np

# --- Load I/Q data from .cfile (assumed: complex64 = float32 + float32 interleaved) ---
filename = r"C:\Users\Siddhant Jinturkar\OneDrive\Desktop\iqdata_150_30deg.cfile"
iq_data = np.fromfile(filename, dtype=np.complex64)

# --- Compute instantaneous power (|I + jQ|^2) ---
instantaneous_power = np.abs(iq_data) ** 2  # Power per sample

# --- Average power in linear scale ---
average_power_linear = np.mean(instantaneous_power)

# --- Convert to dB (10 * log10(P)) ---
average_power_dB = 10 * np.log10(average_power_linear)

# --- Print results ---
print(f"Average Power (Linear): {average_power_linear:.6e}")
print(f"Average Power (dB): {average_power_dB:.2f} dB")
