"""Exercise #4 - Refraction and Snell's Law (n1*sin(th1) = n2*sin(th2))
1. Define the media: air (n1 = 1.0) and glass (n2 = 1.5).
2. Calculate the angles: start with th1 = 45 deg. Use NumPy to convert it
   to radians, apply Snell's Law to find th2, and convert it back.
3. Trace the rays: generate simple x and y linear coordinate points using
   NumPy to draw the incoming ray, the refracted ray, and the boundary line
   between the two media.
"""
import numpy as np
import matplotlib.pyplot as plt

# 1. Media
n1, n2 = 1.0, 1.5

# 2. Angles (measured from the normal)
theta1_deg = 45
theta1 = np.deg2rad(theta1_deg)
theta2 = np.arcsin(n1 * np.sin(theta1) / n2)   # Snell's law
theta2_deg = np.rad2deg(theta2)
print(f"Angle of Incidence (theta1): {theta1_deg:.1f}°")
print(f"Angle of Refraction (theta2): {theta2_deg:.2f}°")

# 3. Rays (boundary on y = 0, air above, glass below, hit point at origin)
t = np.linspace(0, 1, 50)
x_in, y_in = -t * np.sin(theta1), t * np.cos(theta1)      # incoming ray
x_ref, y_ref = t * np.sin(theta2), -t * np.cos(theta2)    # refracted ray
x_bound = np.linspace(-1, 1, 2)
y_bound = np.zeros_like(x_bound)                          # boundary line
y_norm = np.linspace(-1, 1, 2)                            # normal (dashed)

fig, ax = plt.subplots(figsize=(6, 6))
ax.plot(x_bound, y_bound, "k", lw=2, label="boundary")
ax.plot(np.zeros_like(y_norm), y_norm, "k--", lw=1, label="normal")
ax.plot(x_in, y_in, color="hotpink", lw=2.5, label=rf"incident ($\theta_1$={theta1_deg}°)")
ax.plot(x_ref, y_ref, color="tab:blue", lw=2.5, label=rf"refracted ($\theta_2$={theta2_deg:.1f}°)")
ax.text(0.7, 0.5, f"medium 1: air (n={n1})")
ax.text(0.7, -0.5, f"medium 2: glass (n={n2})")
ax.set_aspect("equal")
ax.set_xlim(-1, 1.6)
ax.set_ylim(-1, 1)
ax.set_title("Refraction: Snell's Law")
ax.legend(loc="lower left")
fig.savefig("exercise4.png", dpi=300)

# 4. Several angles + scatter plot of sin(th1) vs sin(th2)
angles1_deg = np.array([0.0, 30.0, 60.0, 90.0])
angles2_deg = np.rad2deg(np.arcsin(n1 * np.sin(np.deg2rad(angles1_deg)) / n2))
print()
print("Incident Angles (deg):", angles1_deg)
print("Refracted Angles (deg):", angles2_deg)

sin1 = np.sin(np.deg2rad(angles1_deg))
sin2 = np.sin(np.deg2rad(angles2_deg))
xs = np.linspace(0, sin2.max(), 50)

fig2, ax2 = plt.subplots(figsize=(6, 6))
ax2.scatter(sin2, sin1, s=80, color="#D9A441", edgecolor="#8a6d1f",
            zorder=3, label="Snell's Law Points")
ax2.plot(xs, (n2 / n1) * xs, "--", color="slategrey", label="Theoretical Slope (n$_2$/n$_1$)")
ax2.set_xlabel(r"sin($\theta_2$) (Refracted Sine)")
ax2.set_ylabel(r"sin($\theta_1$) (Incident Sine)")
ax2.set_title("Scatter Plot of Snell's Law (Air to Glass)", fontweight="bold")
ax2.grid(True, alpha=0.3)
ax2.legend()
fig2.savefig("exercise4_scatter.png", dpi=300)
plt.show()
