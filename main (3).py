import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Import data
df = pd.read_csv("epa-sea-level.csv")

# Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')

# Linear regression for all data
slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
x_all = np.arange(df['Year'].min(), 2051)
y_all = slope * x_all + intercept
plt.plot(x_all, y_all, color='red', label='Best Fit Line (All Data)')

# Linear regression for data from year 2000
df_recent = df[df['Year'] >= 2000]
slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
x_recent = np.arange(2000, 2051)
y_recent = slope_recent * x_recent + intercept_recent
plt.plot(x_recent, y_recent, color='green', label='Best Fit Line (Since 2000)')

# Set labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.legend()

# Save and show plot
plt.savefig('sea_level_plot.png')
plt.show()
