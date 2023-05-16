import pandas as pd

# Read the csv files
df1 = pd.read_csv('file1.csv')
df2 = pd.read_csv('file2.csv')
df3 = pd.read_csv('file3.csv')

# Merge df1 and df2 on 'ORDER_ID'
merged_df = pd.merge(df1, df2, on='ORDER_ID', how='inner')

# Then merge the result with df3 on 'CATALOG_CD'
merged_df = pd.merge(merged_df, df3, on='CATALOG_CD', how='inner')

# If you want to choose specific columns, create a list of column names
columns_to_keep = ['ORDER_ID', 'CATALOG_CD', 'column3', 'column4']  # replace with your column names

# Keep only the columns in columns_to_keep
merged_df = merged_df[columns_to_keep]

# Write the merged dataframe to a new csv file
merged_df.to_csv('merged.csv', index=False)