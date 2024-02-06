import pandas as pd
import numpy as np
from matplotlib import pyplot as plt



daily_data_frame = pd.read_csv('daily.csv')


daily_data_frame_not_null = daily_data_frame

daily_data_frame_not_null['Volume'] = daily_data_frame['Volume'].replace(0, np.nan)

daily_data_frame_not_null['Volume'] = daily_data_frame['Volume'].interpolate(method='linear')

daily_data_frame_not_null.interpolate(method='linear', inplace=True)

daily_data_frame_not_null['20 days MA'] = daily_data_frame_not_null['Adj Close'].rolling(window=20).mean() 
daily_data_frame_not_null['50 days MA'] = daily_data_frame_not_null['Adj Close'].rolling(window=50).mean() 

daily_return = daily_data_frame_not_null['Adj Close'].pct_change()
daily_data_frame_not_null['Daily Return'] = daily_return 

indexes = np.arange(0, 275, 25)
plt.figure(figsize=(1, 7))
plt.plot(daily_data_frame_not_null['Date'], daily_data_frame_not_null['Adj Close'], label='Close Price')
plt.plot(daily_data_frame_not_null['Date'], daily_data_frame_not_null['20 days MA'], label='20 Days MA')
plt.plot(daily_data_frame_not_null['Date'], daily_data_frame_not_null['50 days MA'], label='50 Days MA')
date_labels = [daily_data_frame_not_null['Date'].iloc[i-1] for i in indexes]
plt.xticks(ticks=date_labels, labels=date_labels, rotation=45)
plt.title('Close Price and Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()
