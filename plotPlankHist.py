import matplotlib.pyplot as plt 
import json
import numpy as np

# Load JSON file
with open("L1_Top_Results.json", "r") as file:
    data = json.load(file)

# Extract Young's modulus values
Y = np.array([
    plank["youngs_modulus"]
    for plank in data.values()
], dtype=float)

plt.hist(Y, bins=5)

# Add titles and labels
plt.title("Young's Modulus of L1 Planks (Top)")
plt.xlabel("Young's Modulus (GPa)")
plt.ylabel('Number of Planks')

# Display the plot
plt.savefig("L1_Top_YM_hist.png",dpi=300)