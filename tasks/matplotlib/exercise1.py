"""Exercise #1
Import data of an experiment that you have done by using NumPy.
Plot these data customizing the graph with several pyplot functions.
Tip: use help() to check the properties of pyplot's functions.

Experiment used here: Newton's 2nd law (F = m*a), data from the slides.
Replace data.csv with your own experiment if you like.
"""
import numpy as np
import matplotlib.pyplot as plt

# Write a small data file so the script runs standalone, then import it with NumPy
np.savetxt(
    "data.csv",
    np.column_stack([[1, 2, 3, 4, 5], [11, 19, 31, 40, 52]]),
    delimiter=",", header="acceleration,force", comments="",
)
acc, force = np.loadtxt("data.csv", delimiter=",", skiprows=1, unpack=True)

# Linear fit F = m*a + q
m, q = np.polyfit(acc, force, 1)

font = {"family": "serif", "color": "darkblue", "size": 16}

plt.figure(figsize=(8, 5))
plt.plot(acc, force, "o", ms=8, mec="#4CAF50", mfc="#4CAF50", label="measurements")
plt.plot(acc, m * acc + q, ls="--", c="hotpink", lw=2, label=f"fit: F = {m:.1f}a + {q:.1f}")
plt.xlabel(r"Acceleration (m/s$^2$)")
plt.ylabel("Force (N)")
plt.title("Force vs Acceleration", fontdict=font)
plt.grid(axis="both", color="grey", linestyle="--", linewidth=0.5)
plt.xlim(0, 6)
plt.ylim(0, 60)
plt.xticks(np.arange(0, 7, 1))
plt.annotate("last point", xy=(5, 52), xytext=(3.2, 55),
             arrowprops=dict(facecolor="black", shrink=0.05))
plt.legend()
plt.savefig("exercise1.png", dpi=300)
plt.show()
