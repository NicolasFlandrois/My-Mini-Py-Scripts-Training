import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('seaborn')

data = pd.read_csv('timedata.csv')

data['Date'] = pd.to_datetime(data['Date'])
# Convert with Pandas, the string from the data set, into a Datetime Value
data.sort_values('Date', inplace=True)
# inplace=True will modify the data directly in the dataset

price_date = data['Date']
price_close = data['Close']

plt.plot_date(price_date, price_close, linestyle='solid')
# NB: This import of data just set up the date as a string ,
# and not as a datetime. If the data is scrambled out or order, then
# The graph would be False.

plt.gcf().autofmt_xdate()

plt.title('Bitcoin Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.tight_layout()

plt.savefig('matplot8-TimeSeries.png')
