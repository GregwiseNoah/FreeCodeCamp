import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col= "date")

# Clean data
df = df[(df.value >= (df.value.quantile(0.025))) & (df.value <= (df.value.quantile(0.975)))]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots()
    plt.plot(df)
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.figure(figsize=(16,7))

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    """df_bar = df.copy()
    df_bar.index = pd.to_datetime(df.index)

    df_bar = df_bar.groupby(pd.Grouper(freq="M"))"""

    '''df_bar = df.copy()

In [40]: df_bar.index = pd.to_datetime(df.index)

In [41]: df_bar["year"]  = df_bar.index.year

In [42]: df_bar["month"] = df_bar.index.month_name()

df_grouped = pd.DataFrame(df_bar.groupby(["year", "month"]).mean().roun
    ...: d().astype(int))

    '''

    fig, ax = plt.subplots()
    df_bar = df.copy()
    df_bar.index = pd.to_datetime(df_bar.index)
    df_bar["Years"] = df_bar.index.year
    df_bar["monthnum"] = df_bar.index.month
    #df_bar = df_bar.sort_values(by = "monthnum")
    df_bar["month"] = df_bar.index.month_name()

    df_grouped = pd.DataFrame(df_bar.groupby(["Years", "month"]).mean().round().astype(int))
    df_grouped = df_grouped.reset_index()

    df_grouped = df_grouped.rename(columns={"value":"Average Page Views"})    

    df_empty = pd.DataFrame({"Years":[2016, 2016,2016, 2016,2016,2016,2016], "month":["January","February", "March", "April", "May", "June", "July"], "Average Page Views":[0,0,0,0,0,0,0], "monthnum":[1,2,3,4,5,6,7]})

    df_grouped = pd.concat([df_empty, df_grouped])

    df_grouped = df_grouped.sort_values(by = ["Years","monthnum"])

    # Draw bar plot
    ax.set_title("Daily freeCodeCamp Forum Average Page Views per Month")
    sns.barplot(data = df_grouped, x = "Years", y = "Average Page Views", hue = "month")




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box.date = pd.to_datetime(df_box.date)
    df_box['Year'] = [d.year for d in df_box.date]
    df_box["monthnum"] = [d.month for d in df_box.date]
    df_box['Month'] = [d.strftime('%b') for d in df_box.date]
    df_box = df_box.rename(columns={"value" : "Page Views"})

    # Draw box plots (using Seaborn)


    fig, axs = plt.subplots(ncols = 2)
    sns.boxplot(data=df_box, x = "Year", y = "Page Views", ax = axs[0]).set(title = "Year-wise Box Plot (Trend)")

    df_box_month = df_box.sort_values(by = "monthnum")

    sns.boxplot(data=df_box_month, x = "Month", y = "Page Views", ax = axs[1]).set(title = "Month-wise Box Plot (Seasonality)")





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
