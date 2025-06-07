# generate_white_noise.py
import numpy as np
N = 1_000_00 # Number of samples
white_noise = (np.random.randn(N) + 1j*np.random.randn(N)).astype(np.complex64)
white_noise.tofile(r"C:\Users\Siddhant Jinturkar\OneDrive\Desktop\5G Research\white_noise_burst.cfile")
