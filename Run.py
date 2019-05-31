

#https://www.alphavantage.co/documentation/

import Execute
import pandas as pd
from datetime import datetime

if __name__ == "__main__":
    
    ticker = ""#input("Ticker:  ")
    lookUpDt = ""#input("Select date: (YYYY-MM-DD)  ")
    
    if not ticker:
        ticker = "MSFT"
    
    if not lookUpDt:
        lookUpDt = str(datetime.today().strftime('%Y-%m-%d'))
        
    ticker = str(ticker.upper())
    lookUpDt = str(lookUpDt)
    
    runList =   [
                "addr", 
                "addrSMA", 
                "addrEMA",
                "addrWMA"
                ]
    runDict =   {
                "addr": r"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + ticker + "&apikey=demo", 
                "addrSMA": r"https://www.alphavantage.co/query?function=SMA&symbol=" + ticker + "&interval=weekly&time_period=10&series_type=open&apikey=demo",
                "addrEMA": r"https://www.alphavantage.co/query?function=EMA&symbol=" + ticker + "&interval=weekly&time_period=10&series_type=open&apikey=demo",
                "addrWMA": r"https://www.alphavantage.co/query?function=WMA&symbol=" + ticker + "&interval=weekly&time_period=10&series_type=open&apikey=demo"
                }
    dimDict =   {
                "addr": "Time Series (Daily)", 
                "addrSMA": "Technical Analysis: SMA",
                "addrEMA": "Technical Analysis: EMA",
                "addrWMA": "Technical Analysis: WMA"
                }
    
    runListid = runList[0]
    filterValue = runDict[runListid]
    filterValuedim = dimDict[runListid]
    
    vl = Execute.main(filterValue, ticker, lookUpDt, filterValuedim)
    
    df = pd.DataFrame.from_dict(vl.PriceListx, orient='columns')
    print(df)
    