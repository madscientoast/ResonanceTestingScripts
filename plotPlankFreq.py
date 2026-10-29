import matplotlib.pyplot as plt 
import json
import numpy as np

# Load JSON file
with open("L1_Top_Results.json", "r") as file:
    data = json.load(file)

# Extract Young's modulus values
mass = np.array([
    plank["mass"]
    for plank in data.values()
], dtype=float)

freq = np.array([
    plank["frequency"]
    for plank in data.values()
], dtype=float)

plt.scatter(mass,freq)

# Add titles and labels
plt.title("Mean Frequency of L1 Planks (Top)")
plt.xlabel("mass (g)")
plt.ylabel("Frequency (Hz)")
plt.ylim(0,400)

# Fit linear trend line
slope, intercept = np.polyfit(mass, freq, 1)

# Generate trend line
x_fit = np.linspace(min(mass), max(mass), 100)
y_fit = slope * x_fit + intercept

# Plot trend line
plt.plot(x_fit, y_fit, 'r--', label="Linear Fit")

# Display the plot
plt.savefig("L1_Top_freq_scatter.png",dpi=300)
