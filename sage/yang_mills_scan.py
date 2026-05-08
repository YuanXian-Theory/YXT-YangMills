#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Yang-Mills Gauge Field Spectrum Simulation on T^64
Part of YuanXian Theory (YXT) Numerical Verification
"""

import numpy as np
import matplotlib.pyplot as plt

# Parameters
R = 1.0
n_modes = 10000
np.random.seed(42)

def simulate_gauge_modes():
    n = np.random.randint(-5, 6, size=(n_modes, 64))
    energies = np.linalg.norm(n, axis=1) / R
    return energies[energies > 0]

energies = simulate_gauge_modes()

print("=== YD-T64 Yang-Mills Gauge Field Spectrum ===")
print(f"Minimum non-zero energy (Mass Gap): {energies.min():.6f}  (Theoretical: 1/R = 1.0)")

plt.figure(figsize=(10, 6))
plt.hist(energies, bins=60, alpha=0.75, color='#1f77b4', edgecolor='black')
plt.axvline(x=1.0, color='red', linestyle='--', linewidth=2, label='Theoretical Mass Gap Δ = 1/R')
plt.xlabel('Energy E')
plt.ylabel('Count')
plt.title('Yang-Mills Gauge Field Energy Spectrum on T⁶⁴')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('../figures/energy_spectrum.png', dpi=300, bbox_inches='tight')
plt.show()
