import pandas as pd
import os
import pickle

split_files = ['split_0.pkl', 'split_1.pkl']

for split_file in split_files:
    if os.path.exists(split_file):
        with open(split_file, 'rb') as file:
            split_df = pickle.load(file)
        print(f"Loaded split from {split_file}")

        # Check for missing headers and assign default headers
        new_columns = []
        for i, col in enumerate(split_df.columns):
            if not col or pd.isna(col):
                new_columns.append(f"Column_{i}")
            else:
                new_columns.append(col)
        split_df.columns = new_columns

        # Convert to csv
        csv_filename = split_file.replace('.pkl', '.csv')
        split_df.to_csv(csv_filename, index=False)
        print(f"Saved DataFrame to {csv_filename}")

    else:
        print(f"File {split_file} not found")
    