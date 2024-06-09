import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import yfinance as yf

style.use('ggplot')

start=dt.datetime(2020,1,1)
end=dt.datetime.today()

old_start=dt.datetime(2016,1,1)
old_end=dt.datetime(2019,12,31)

#df=pdr.get_data_yahoo('AAPL', sart, end)
df1=yf.download('MSFT', start, end)
df2=yf.download('NVDA', start, end)
print(df1['Adj Close'].head())

plt.scatter(df1['Adj Close'],df2['Adj Close'],alpha=0.5)
plt.xlabel('MSFT')
plt.ylabel('NVDA')
plt.show()

###########################################################################
## Exercise 1: Get the stock prices for the last year of the S&P 500
## Exercise 2: Plot the correlations between individial stocks and S&P 500
###########################################################################
###
# Next Time: Fitting Financial Data (SciPy)
###