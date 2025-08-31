import pandas as pd, numpy as np


def string_mode(series):
    modes = series.mode()
    return modes.iloc[0] if not modes.empty else np.nan


def clean_theatres_data_for_city(name: str, theatres_df: pd.DataFrame):
    # print(f"Started Data Cleaning for Theatres in City: {name}")
    fwd_fill_cols_list = ["Cinema Chain", "Zone", "Owner"]
    theatres_df[fwd_fill_cols_list] = theatres_df[fwd_fill_cols_list].ffill()

    theatres_df['Avg Capacity'] = pd.to_numeric(theatres_df['Avg Capacity'], errors='coerce')
    group_means_for_capacity = theatres_df.groupby(['Screen Type', 'Screens (Count)'])['Avg Capacity'].transform('mean')
    theatres_df['Avg Capacity'] = theatres_df['Avg Capacity'].fillna(group_means_for_capacity)
    theatres_df['Avg Capacity'] = theatres_df.apply(
        lambda row:
        group_means_for_capacity[row.name] if pd.isna(row['Avg Capacity']) and row['Screens (Count)'] > 0
        else 0 if pd.isna(row['Avg Capacity'])
        else row['Avg Capacity'],
        axis=1
    )

    # Step 1: Ensure object column is clean
    theatres_df['Avg Ticket Price (₹)'] = theatres_df['Avg Ticket Price (₹)'].astype(str).replace('nan', np.nan)

    group_mode_ranges = theatres_df.groupby('Screen Type')['Avg Ticket Price (₹)'].transform(string_mode)
    # Step 4: Fill missing
    theatres_df['Avg Ticket Price (₹)'] = theatres_df['Avg Ticket Price (₹)'].fillna(group_mode_ranges)

    # df['Multiplex_Chain_Theatres_Data'] = sheet_name  # Add city name from sheet name
    split_price = theatres_df['Avg Ticket Price (₹)'].str.split('–', expand=True)
    if len(split_price) >= 2:
        theatres_df['Min Price'] = pd.to_numeric(split_price[0].str.strip(), errors='coerce')
        theatres_df['Max Price'] = pd.to_numeric(split_price[1].str.strip(), errors='coerce')
    else:
        print("Bhutu...")

    theatres_df.loc[theatres_df['Screens (Count)'] == theatres_df.empty, ['Min Price', 'Max Price']] = 0

    # print(f"Finished Data Cleaning for Theatres in City: {name}")
    return theatres_df




