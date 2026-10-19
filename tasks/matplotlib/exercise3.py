"""Exercise #3
Three datasets from a physics experiment over time.
Generate them with NumPy and make a 3D plot with Matplotlib
showing three histograms in perspective.
"""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
datasets = [
    np.random.normal(30, 5, 1000),   # t = 0
    np.random.normal(50, 8, 1000),   # t = 1
    np.random.normal(70, 6, 1000),   # t = 2
]
colors = ["tab:blue", "tab:orange", "tab:green"]

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(projection="3d")

for t, (data, c) in enumerate(zip(datasets, colors)):
    counts, edges = np.histogram(data, bins=20, range=(10, 90))
    centers = (edges[:-1] + edges[1:]) / 2
    ax.bar(centers, counts, zs=t, zdir="y", width=3.5, color=c, alpha=0.8)

ax.set_xlabel("Measured value")
ax.set_ylabel("Time")
ax.set_zlabel("Frequency")
ax.set_yticks([0, 1, 2])
ax.set_title("Three histograms in perspective")
plt.savefig("exercise3.png", dpi=300)
plt.show()
