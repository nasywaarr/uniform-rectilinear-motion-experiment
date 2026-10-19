"""Exercise #2
Measurements of the duration of pendulum oscillations, affected by errors.
- Simulate 50 measurements, mean 2.0 s, std 0.2 s.
- Assign random uncertainties between 0.05 s and 0.15 s.
- Plot the data points with error bars using errorbar().
"""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
n = 50
periods = np.random.normal(loc=2.0, scale=0.2, size=n)
errors = np.random.uniform(0.05, 0.15, size=n)
x = np.arange(1, n + 1)  # measurement number

plt.figure(figsize=(10, 5))
plt.errorbar(x, periods, yerr=errors, fmt="o", ms=4, capsize=3, label="measurements")
plt.axhline(2.0, color="hotpink", ls="--", lw=1.5, label="mean = 2.0 s")
plt.xlabel("Measurement number")
plt.ylabel("Oscillation duration (s)")
plt.title("Pendulum oscillation measurements with error bars")
plt.grid(True, alpha=0.3)
plt.legend()
plt.savefig("exercise2.png", dpi=300)
plt.show()
