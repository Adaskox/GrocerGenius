import os
import pandas as pd
import numpy as np

# Define the path to your CSV file
filtered_csv_path = r'C:\Users\Adaskox\GrocerGenius\FilteredIngr.csv'

# Check if the file exists and delete it
if os.path.exists(filtered_csv_path):
    os.remove(filtered_csv_path)

# Continue with your script
excel_path = r'C:\Users\Adaskox\Desktop\Trening i jedzenie\Jedzenie.xlsx'
excel_file = pd.ExcelFile(excel_path)
last_sheet = excel_file.sheet_names[-2]

df = pd.read_excel(excel_file, last_sheet, usecols=[1,13,15,16,17])
df.columns = ['meal', 'ingredient', 'amount', 'ingredient2', 'amount2']

# Keywords to convert to NaN
keywords = ['Produkt', 'Na 3 dni g', 'Bez liczenia prod.', 'Na mnie', 0, 0.0]
df.replace(keywords, np.nan, inplace=True)

# Select the specific rows you're interested in
indicies = np.array([range(4,63)]).flatten()
filtered_df = df.iloc[indicies]

# Drop rows where all values are NaN
clean_df = filtered_df.dropna(how='all')

# Save the cleaned DataFrame to CSV, file will be created here
clean_df.to_csv(filtered_csv_path, index=False, encoding='utf-8')
