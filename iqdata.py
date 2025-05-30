import numpy as np
import matplotlib.pyplot as plt

# Path to your recorded file
filename = r"C:\Users\Siddhant Jinturkar\OneDrive\Desktop\iqdata_NA_30deg.cfile"

# Load the complex64 IQ data
iq_data = np.fromfile(filename, dtype=np.complex64)

# Plot I vs Q (constellation diagram)
plt.figure(figsize=(6, 6))
plt.scatter(iq_data.real, iq_data.imag, s=1, alpha=0.5)
plt.title("IQ Constellation Plot")
plt.xlabel("In-phase (I)")
plt.ylabel("Quadrature (Q)")
plt.grid(True)
plt.axis('equal')
plt.show()

