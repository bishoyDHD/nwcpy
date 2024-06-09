from matplotlib.colors import Colormap
import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('GE.csv')
df2 = pd.read_csv('BA.csv')

plt.scatter(df1['Adj Close'], df2['Adj Close'], c='blue')
plt.title('Close Prices')
plt.xlabel('GE')
plt.ylabel('BA')
#plt.legend()
#plt.show()
#print(df.tail(10))

'''
symbols=['AAPL.csv', 'AMZN.csv', 'BA.csv', 'GOOG.csv', 'GE.csv']

plt.figure()
for s in symbols:
    close_df = pd.read_csv(s)
    close_df['Adj Close'].plot(lw=2,label=s,marker='.')

plt.legend(loc='best')
plt.title('Stock Prices')
plt.ylabel('Adj Close')
plt.show()
'''
############################################
##### EXERCISES AND EXAMPLES ###############
############################################
# How to select and create a new DataFrame from column greater than a given value
df3=df1.query('Close > 30')
print(df3.head(10))
#Now plot the data for the above and also apply this to the list of companies
#You are free to choose which coluumns you want to cut on and plot