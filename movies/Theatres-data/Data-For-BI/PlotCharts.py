import matplotlib.pyplot as plt
import pandas as pd


def plot_chart(df: pd.DataFrame, ask: str):
    if ask == "cinema_chain_group_by_cities":
        cinema_chain_group_by_city = (
            df.groupby(["City"])
            .size()
            .reset_index(name="Cinema Chain Count")
        )
        plot_chart_with_updated_df(cinema_chain_group_by_city, "City",
                                   "Cinema Chain Count", title=ask)
    elif ask == "screen_type_group_by_cities":
        screen_type_group_by_city = (
            df.groupby(["City"])
            .size()
            .reset_index(name="Screen Type Count")
        )
        plot_chart_with_updated_df(screen_type_group_by_city, "City",
                                   "Screen Type Count", title=ask)
    elif ask == "screens_count_group_by_cities":
        screen_type_group_by_city = (
            df.groupby("City")["Screens (Count)"]
            .sum()
            .reset_index(name="Screens Count")
        )
        plot_chart_with_updated_df(screen_type_group_by_city, "City",
                                   "Screens Count", title=ask)


def plot_chart_with_updated_df(updated_df, x_label: str, y_label: str, title: str):
    # Bar plot: one bar per city
    plt.figure(figsize=(10, 4))
    plt.bar(updated_df[x_label], updated_df[y_label], color='skyblue', width=0.4)
    plt.xlabel(x_label, fontsize=10)
    plt.ylabel(y_label, fontsize=10)
    plt.title(title, fontsize=10)
    plt.xticks(rotation=90, fontsize=5)
    plt.yticks(fontsize=5)
    plt.tight_layout()
    plt.show()


def replacer(theatres_df: pd.DataFrame):
    cat = list(theatres_df.columns[theatres_df.dtypes == 'object'])
    for column in theatres_df.columns:
        if column in cat:
            mode = theatres_df[column].mode()[0]
            theatres_df[column] = theatres_df[column].fillna(mode)
        else:
            mean = theatres_df[column].mean()
            theatres_df[column] = theatres_df[column].fillna(mean)
    print('Missing values replaced')

def replacer(df: pd.DataFrame):
    cat = list(df.columns[df.dtypes == "object"])
    for col in df.columns:
        if col in cat:
            mode = df[col].mode()[0]
            df[col] = df[col].fillna(mode)
        else:
            mean = df[col].mean()
            df[col] = df[col].fillna(mean)
    print("Missing values replaced")