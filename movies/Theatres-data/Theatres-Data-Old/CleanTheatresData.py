import pandas as pd
import TheatresUtilData

# 1. Load Excel
all_sheets = pd.read_excel('Theatres_Data.xlsx', sheet_name=None)

# 2. Clean
cleaned_sheets = {}
for name, df in all_sheets.items():
    # your cleaning logic
    cleaned_sheets[name] = TheatresUtilData.clean_theatres_data_for_city(name, df)

# 3. Save back
with pd.ExcelWriter('../cleaned_up_data/Theatres_Data.xlsx', engine='openpyxl') as writer:
    for name, df in cleaned_sheets.items():
        df.to_excel(writer, sheet_name=name, index=False)

# 1. Validate Created Excel
all_sheets = pd.read_excel('cleaned_up_data\\Theatres_Data.xlsx', sheet_name=None)
theatres_data_cleaned_cities, theatres_data_not_cleaned_cities = [], []
for name, df in all_sheets.items():
    if df.isna().sum().sum() == 0:
        theatres_data_cleaned_cities.append(name)
    else:
        theatres_data_not_cleaned_cities.append(name)
print(f'Theatres data cleaned for cities : {theatres_data_cleaned_cities}')
print(f'Theatres data not cleaned for cities : {theatres_data_not_cleaned_cities}')
