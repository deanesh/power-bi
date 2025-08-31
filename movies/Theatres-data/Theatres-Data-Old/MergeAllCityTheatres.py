import pandas as pd

# Load all sheets from the Excel file
sheets_dict = pd.read_excel('cleaned_up_data\\Theatres_Data.xlsx', sheet_name=None)

# Combine all sheets by stacking them, and tag with sheet name as 'City'
merged_list = []
for sheet_name, df in sheets_dict.items():
    df = df.copy()

    merged_list.append(df)

# Stack them into a single DataFrame
merged_df = pd.concat(merged_list, ignore_index=True)

# Save to Excel
merged_df.to_excel('cleaned_up_data\\Merged_Theatres_Data.xlsx', index=False)
