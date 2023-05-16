import os
import pandas as pd

# Get a list of all the csv files
csv_files = [f for f in os.listdir() if f.endswith('.csv')]

# Define chunksize
chunksize = 10 ** 6  # adjust this value depending on your available memory

# Loop through csv files and write each chunk to the new CSV file
for csv_file in csv_files:
    for chunk in pd.read_csv(csv_file, chunksize=chunksize):
        # If the file does not exist, write with a header, else skip the header
        if not os.path.isfile('combined.csv'):
            chunk.to_csv('combined.csv', index=False)
        else:  # else it exists so append without writing the header
            chunk.to_csv('combined.csv', mode='a', header=False, index=False)