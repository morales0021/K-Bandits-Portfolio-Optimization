import yfinance as yf
import pandas as pd

class yahoo:

    def __init__(self, tickers):

        self.tickers = tickers
        self.ticker_srs = None
        self.df = None

    def pull_data(self, start_date, end_date):

        self.start_date = start_date
        self.end_date = end_date

        self.ticker_srs = [] 

        for ticker in self.tickers:
            # Get the data
            data = yf.download(ticker, start_date, end_date)
            self.ticker_srs.append(data)

        self.df = pd.DataFrame(self.ticker_srs[0]['Adj Close'])

        for i in range(1,len(self.ticker_srs)): 
            self.df = pd.concat([self.df,self.ticker_srs[i]['Adj Close']], axis = 1)

        self.df.columns = self.tickers

    
    def pct_change(self, interval = '2W'):

        df = self.df.resample(interval).last()
        returns = df.pct_change()
        df_bandits = pd.DataFrame(returns.values).dropna()
        return df_bandits