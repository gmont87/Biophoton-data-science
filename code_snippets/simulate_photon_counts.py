# simulate_photon_counts.py
# Author: Gino Montero
# Description: Simulate random photon emission counts per second 
# as a simple model for plant biophoton emission.
# This will later be replaced by real sensor data.

import numpy as np
import matplotlib.pyplot as plt

# ---- Step 1: Simulate data ----
# Assume a plant will emit 5 photon per second on average
# Simulate 300 seconds of data.

mean_photon_rate = 5
duration = 300  # seconds
photon_counts = np.random.poisson(mean_photon_rate, duration)

# ---- Step 2: Analyze basic statistics ----
mean_count = np.mean(photon_counts)
std_count = np.std(photon_counts)
max_count = np.max(photon_counts)

print(f"Average photons/sec: {mean_count:.2f}")
print(f"Standard deviation: {std_count:.2f}")
print(f"Max count: {max_count}")
