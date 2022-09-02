
from Stratgey import MarketData

import matplotlib.pyplot as plt

import pandas as pd
import matplotlib.dates as mpdates

plt.style.use('dark_background')

# extracting Data for plotting
df = MarketData.g
df = df[['Date', 'Open', 'High','Low', 'Close']]

# convert into datetime object
df['Date'] = pd.to_datetime(df['Date'])

# apply map function
df['Date'] = df['Date'].map(mpdates.date2num)

# creating Subplots
fig, ax = plt.subplots()

# plotting the data
MarketData.g(ax, df.values, width=0.6,
                 colorup='green', colordown='red',
                 alpha=0.8)

# allow grid
ax.grid(True)

# Setting labels
ax.set_xlabel('Date')
ax.set_ylabel('Price')

# setting title
plt.title('Prices For the Period 01-07-2020 to 15-07-2020')

# Formatting Date
date_format = mpdates.DateFormatter('%d-%m-%Y')
ax.xaxis.set_major_formatter(date_format)
fig.autofmt_xdate()

fig.tight_layout()

# show the plot
plt.show()