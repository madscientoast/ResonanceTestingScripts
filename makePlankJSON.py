import json
import pandas as pd

plank_num = numbers = list(range(1, 21))
plank_num.pop(1) # Did not measure L1 02 yet

# Load spreadsheet #
data = pd.read_csv("L1_Top_Results.csv")

mass = data['mass'].tolist()
freq = data['mean freq'].tolist()
ym = data["Y"].tolist()

results = {
    f"L1_{num:02d}": {
        "num": num,
        "mass": m,
        "frequency": f,
        "youngs_modulus": y
    }
    for num, m, f, y in zip(plank_num, mass, freq, ym)
}

# Save JSON
with open("L1_Top_Results.json", "w") as f:
    json.dump(results, f, indent=4)