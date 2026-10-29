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

Y = np.array([
    plank["youngs_modulus"]
    for plank in data.values()
], dtype=float)

plt.scatter(mass,Y)

# Add titles and labels
plt.title("Young's Modulus of L1 Planks (Top)")
plt.xlabel("mass (g)")
plt.ylabel("Young's Modulus (GPa)")
plt.ylim(0,50)

# Fit linear trend line
slope, intercept = np.polyfit(mass, Y, 1)

# Generate trend line
x_fit = np.linspace(min(mass), max(mass), 100)
y_fit = slope * x_fit + intercept

# Plot trend line
plt.plot(x_fit, y_fit, 'r--', label="Linear Fit")

# Display the plot
plt.savefig("L1_Top_ym_scatter.png",dpi=300)
