import utils

import pandas as pd
import numpy as np

import os

import gen

# generate raw fake data & export to sub-directory
gen.generate_fake_data()

# clean fake data
# Set the directory containing the CSV files
rawfakedata_dir = "./data/raw/fake/"
results_dir = "./data/processed/fake"

# Create the subdirectory if it does not exist
if not os.path.exists(results_dir):
    os.makedirs(results_dir)

# Loop over each file in the directory
for filename in os.listdir(rawfakedata_dir):
    if filename.endswith(".csv"):
        # Construct the full file path
        file_path = os.path.join(rawfakedata_dir, filename)

        columns_to_keep = ["Last name", "First name", "ID number", "Course total (Real)"]
        
        # Read the CSV file, round to one decimal place, & assign letter grade
        df = pd.read_csv(file_path)

        # Select the subset of columns
        if all(col in df.columns for col in columns_to_keep):
            df_subset = df[columns_to_keep].copy()
            df_subset["Course total (Real)"] = np.round(df_subset["Course total (Real)"], 1)
            # df_subset["Course total (Real)"] = 100 * df_subset["Course total (Real)"]
            df_subset["letterGrade"] = df_subset["Course total (Real)"].map(utils.letter_grade_fall2024)
            
        # Construct the path for the new file
            results_file_path = os.path.join(results_dir, filename)
            
        # Write the subset DataFrame to a new CSV file
            df_subset.to_csv(results_file_path, index=False)