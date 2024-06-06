import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv", index_col='Year')

    # Create scatter plot
    _, ax = plt.subplots()

    ax.scatter(df.index, df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope, intercept,_,_,_ = linregress(df.index, df['CSIRO Adjusted Sea Level'])
    
    x = np.arange(df.index.min(), 2051)
    y = slope * x + intercept

    plt.plot(x,y, color='red')
    


    # Create second line of best fit
    newDf = df[(df.index.get_loc(2000)):]

    slope1, intercept1,_,_,_ = linregress(newDf.index, newDf['CSIRO Adjusted Sea Level'])

    x1 = np.arange(2000,2051)
    y1 = slope1*x1 + intercept1

    plt.plot(x1,y1,color = 'yellow')

    # Add labels and title

    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()