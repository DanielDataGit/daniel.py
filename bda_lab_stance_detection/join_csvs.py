import pandas as pd
import glob
import os

# Set the folder where your CSV files are located
csv_folder = 'C:\\Users\\dtafm\\OneDrive\\Desktop\\data.science\\danielpy\\bda_lab_stance_uhc\\pythonProject1\\70k_bt'

# Use glob to get all CSV files in the folder
all_files = glob.glob(os.path.join(csv_folder, "*.csv"))

# Efficiently load and concatenate all CSVs
df = pd.concat((pd.read_csv(f) for f in all_files), ignore_index=True)

# Optionally save to a single CSV
df.to_csv("merged.csv", index=False)
