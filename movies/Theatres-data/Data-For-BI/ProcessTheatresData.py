
import pandas as pd
import PlotCharts

# Summary Variables
City_Count = 0
Max_Ticket_Price, Min_Ticket_Price = 0.0, 0.0
Max_Revenue_Per_Day, Min_Revenue_Per_Day = 0.0, 0.0
Max_Capacity_Per_Day, Min_Capacity_Per_Day = 0.0, 0.0
crore_val = 10000000
month_days = 30
year_days = 365


def plot_charts():
    # Cinema Chains Count Per City
    PlotCharts.plot_chart(theatres_df, "cinema_chain_group_by_cities")
    # Screen Type Count Per City
    PlotCharts.plot_chart(theatres_df, "screen_type_group_by_cities")
    # Total Screens Count Per City
    PlotCharts.plot_chart(theatres_df, "screens_count_group_by_cities")


def theatres_data_summary():
    global City_Count, Max_Ticket_Price, Min_Ticket_Price, Max_Revenue_Per_Day, Min_Revenue_Per_Day, Max_Capacity_Per_Day, Min_Capacity_Per_Day
    City_Count = int(theatres_df['City'].nunique())
    Theatres_Count = int(theatres_df['Screens (Count)'].sum())
    Max_Ticket_Price = float(theatres_df['Max Price'].max())
    Min_Ticket_Price = float(theatres_df[theatres_df['Min Price'].values > 0]['Min Price'].values.min())

    Max_Revenue_Per_Day = round(sum(theatres_df['Max Price'] * theatres_df['Max Shows Per Day']
                                    * theatres_df['Avg Capacity']
                                    * theatres_df['Screens (Count)']) / crore_val, 2)
    Min_Revenue_Per_Day = round(
        sum(theatres_df['Min Price'] * theatres_df['Min Shows Per Day'] * theatres_df['Avg Capacity']
            * theatres_df['Screens (Count)']) / crore_val, 2)
    Max_Capacity_Per_Day = round(sum(theatres_df['Max Shows Per Day'] * theatres_df['Avg Capacity']
                                     * theatres_df['Screens (Count)']) / crore_val, 2)
    Min_Capacity_Per_Day = round(sum(theatres_df['Min Shows Per Day'] * theatres_df['Avg Capacity']
                                     * theatres_df['Screens (Count)']) / crore_val, 2)
    print(f'City Count: {City_Count}, Theatres Count: {Theatres_Count}')
    print(f'Min-Max Ticket Prices: {Min_Ticket_Price} - {Max_Ticket_Price}')
    print(f'Min-Max people watching per day with 100% occupancy rate in crores: [{Min_Capacity_Per_Day} - '
          f'{Max_Capacity_Per_Day}] crores')
    print(f'Min-Max Revenue per day with 100% occupancy rate in crores: [ {Min_Revenue_Per_Day} '
          f'- {Max_Revenue_Per_Day}] crores')


def revenue_capacity_with_varied_occupancy_rates():
    global Max_Capacity_Per_Day, Min_Capacity_Per_Day, Max_Revenue_Per_Day, Min_Revenue_Per_Day
    print(f"{'DAYS':<5} | {'Occupancy':<10} | {'Min_Capacity':<13} | {'Max_Capacity':<15} | {'Min_Revenue':<12} | {'Max_Revenue':<12}")
    for occupancy in range(25, 125, 25):
        min_cap_per_day = (Min_Capacity_Per_Day * occupancy)/100
        max_cap_per_day = (Max_Capacity_Per_Day * occupancy)/100
        min_rev_per_day = (Min_Revenue_Per_Day * occupancy)/100
        max_rev_per_day = (Max_Revenue_Per_Day * occupancy)/100
        min_cap_per_month = (Min_Capacity_Per_Day * occupancy * month_days) / 100
        max_cap_per_month = (Max_Capacity_Per_Day * occupancy * month_days) / 100
        min_rev_per_month = (Min_Revenue_Per_Day * occupancy * month_days) / 100
        max_rev_per_month = (Max_Revenue_Per_Day * occupancy * month_days) / 100
        min_cap_per_year = (Min_Capacity_Per_Day * occupancy * year_days) / 100
        max_cap_per_year = (Max_Capacity_Per_Day * occupancy * year_days) / 100
        min_rev_per_year = (Min_Revenue_Per_Day * occupancy * year_days) / 100
        max_rev_per_year = (Max_Revenue_Per_Day * occupancy * year_days) / 100
        print(f"{1:<5} | {occupancy:<10} | {min_cap_per_day:<13,} | {max_cap_per_day:<15,} | {min_rev_per_day:<12,} | {max_rev_per_day:<12,}")
        print(f"{30:<5} | {occupancy:<10} | {min_cap_per_month:<13,} | {max_cap_per_month:<15,} | {min_rev_per_month:<12,} | {max_rev_per_month:<12,}")
        print(f"{365:<5} | {occupancy:<10} | {min_cap_per_year:<13,} | {max_cap_per_year:<15,} | {min_rev_per_year:<12,} | {max_rev_per_year:<12,}")


# Load Excel
theatres_df = pd.read_excel('Theatres_Data.xlsx', sheet_name='Theatres_Data')
PlotCharts.replacer(theatres_df)
# theatres_data_summary()
# revenue_capacity_with_varied_occupancy_rates()
# plot_charts()

