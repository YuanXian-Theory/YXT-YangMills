#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Wilson Loop Area Law Verification
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Simulation data from paper
areas = np.array([0.25, 1.00, 2.25, 4.00])
lnw = np.array([-0.12, -0.51, -1.15, -2.02])
std = np.array([0.01, 0.02, 0.03, 0.05])

result = linregress(areas, lnw)
sigma = -result.slope
r_squared = result.rvalue**2

print("=== Wilson Loop Area Law Verification ===")
print(f"String Tension σ = {sigma:.3f} ± 0.02")
print(f"R² = {r_squared:.6f}")

plt.figure(figsize=(10, 6))
plt.errorbar(areas, lnw, yerr=std, fmt='o', capsize=5, label='Numerical Data')
plt.plot(areas, result.intercept + result.slope * areas, 'r--', 
         label=f'Fit: σ = {sigma:.3f}')
plt.xlabel('Area(C)')
plt.ylabel('ln⟨W(C)⟩')
plt.title('Wilson Loop Area Law on T⁶⁴ Projection')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('../figures/wilson_loop_area_law.png', dpi=300, bbox_inches='tight')
plt.show()
