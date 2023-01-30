import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot

    plt.scatter(x = df.Year, y = df["CSIRO Adjusted Sea Level"], color = "red")

    # Create first line of best fit
    slope, intercept, r, p, se = linregress(df.Year, df["CSIRO Adjusted Sea Level"])
    extended = np.arange(1880,2050, 1)

    #df_extended = pd.DataFrame({"Year":extended, "CSIRO Adjusted Sea Level": intercept + slope*extended})

    """plt.plot(df.Year, intercept + slope*df.Year, color = "black", label = "Regfit")
    plt.plot(extended, intercept + slope*extended, color = "red", label = "2050", linewidth = 5 )
"""
    extended_data = intercept + slope * extended

    #plt.plot(df_extended.Year, df_extended["CSIRO Adjusted Sea Level"], color = "blue")
    
    plt.plot(extended, extended_data)

    # Create second line of best fit
    df_cut = df[df.Year >= 2000]
    slope_cut, intercept_cut, rr, pp, see = linregress(df_cut.Year, df_cut["CSIRO Adjusted Sea Level"])

    extended_cut = np.arange(2000,2050, 1)

    df_extended_cut = pd.DataFrame({"Year":extended_cut, "predicted": intercept_cut + slope_cut*extended_cut})
    
    plt.plot(df_extended_cut.Year, df_extended_cut.predicted)

    #plt.plot(extended, intercept_cut + slope_cut*extended, color = "pink", label = "2050_cut", linewidth = 5 )

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()