import pybaseball as pb
import pandas as pd
import pickle
import os

player = pb.playerid_lookup('cole', 'gerrit')

bbref_id = player.key_bbref.values[0]

splits = pb.get_splits(bbref_id, 2024, pitching_splits=True)

for i, split in enumerate(splits):
    if isinstance(split, pd.DataFrame):
        filename_pkl = f"split_{i}.pkl"
        filename_html = f"split_{i}.html"

        # Check if the DataFrame is already saved
        if os.path.exists(filename_pkl):
            # Load the DataFrame from the file
            with open(filename_pkl, 'rb') as file:
                split = pickle.load(file)
            print(f"Loaded split {i} from {filename_pkl}")
        else:
            # Save the DataFrame to a pickle file
            with open(filename_pkl, 'wb') as file:
                pickle.dump(split, file)
            print(f"Saved split {i} to {filename_pkl}")

        # Save the DataFrame to an HTML file
        split.to_html(filename_html)
        print(f"Saved split {i} to {filename_html}")
