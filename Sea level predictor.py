import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def load_data():
    df = pd.read_csv('epa-sea-level.csv')
    return df

def plot_data(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = [df['Year'].min(), 2050]
    y = [slope * i + intercept for i in x]
    ax.plot(x, y, color='red')

    recent_df = df[df['Year'] >= 2000]
    slope, intercept, _, _, _ = linregress(recent_df['Year'], recent_df['CSIRO Adjusted Sea Level'])
    x = [recent_df['Year'].min(), 2050]
    y = [slope * i + intercept for i in x]
    ax.plot(x, y, color='green')

    return fig

df = load_data()
fig = plot_data(df)
