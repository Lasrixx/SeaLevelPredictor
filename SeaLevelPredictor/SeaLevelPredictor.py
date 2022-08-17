import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    
    #Need dates ranging from the beginning of epa-sea-level.csv to 2050
    future_dates = pd.date_range(start=str(df['Year'].max()+1),end="2051",freq='Y').year.tolist()
    df2=pd.DataFrame(columns=['Year','CSIRO Adjusted Sea Level','Lower Error Bound','Upper Error Bound','NOAA Adjusted Sea Level'])
    df2['Year'] = future_dates

    total_df = pd.merge(df,df2,how="outer")

    # Create scatter plot
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    bestfit_overall = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    plt.plot(total_df['Year'], bestfit_overall.intercept + bestfit_overall.slope*total_df['Year'], 'r', label='fitted line')

    # Create second line of best fit
    recent_df = df.loc[df['Year']>=2000]
    bestfit_recent = linregress(recent_df['Year'],recent_df['CSIRO Adjusted Sea Level'])
    plt.plot(pd.merge(recent_df,df2,how="outer")['Year'], bestfit_recent.intercept + bestfit_recent.slope*pd.merge(recent_df,df2,how="outer")['Year'], 'r', label="fitted line")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()