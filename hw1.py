'''
name: Weiqi Dong
date: 1/10/2025
'''
import pandas as pd

# Specify the path to the CSV file
file_path = 'data/Iris.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    # Print each row
    print('\t'.join([str(row[col]) for col in df.columns]))