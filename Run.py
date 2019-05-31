

#https://www.alphavantage.co/documentation/

import Execute
import pandas as pd
from datetime import datetime
import traceback
import time

if __name__ == "__main__":
    
    ticker = ""#input("Ticker:  ")
    lookUpDt = ""#input("Select date: (YYYY-MM-DD)  ")
    
    if not ticker:
        ticker = "GOOGL"
    
    if not lookUpDt:
        lookUpDt = str(datetime.today().strftime('%Y-%m-%d'))
        
    ticker = str(ticker.upper())
    lookUpDt = str(lookUpDt)
    
    apikey = "demo"
    
    runList =   [
                "addrPrice", 
                "addrSMA", 
                "addrEMA",
                "addrWMA",
                "addrDEMA",
                "addrTEMA",
                "addrTRIMA"
                ]
    runDict =   {
                "addrPrice": r"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + ticker + "&apikey=" + apikey, 
                "addrSMA": r"https://www.alphavantage.co/query?function=SMA&symbol=" + ticker + "&interval=weekly&time_period=10&series_type=open&apikey=" + apikey,
                "addrEMA": r"https://www.alphavantage.co/query?function=EMA&symbol=" + ticker + "&interval=weekly&time_period=10&series_type=open&apikey=" + apikey,
                "addrWMA": r"https://www.alphavantage.co/query?function=WMA&symbol=" + ticker + "&interval=weekly&time_period=10&series_type=open&apikey=" + apikey,
                "addrDEMA": r"https://www.alphavantage.co/query?function=DEMA&symbol=" + ticker + "&interval=weekly&time_period=10&series_type=open&apikey=" + apikey,
                "addrTEMA": r"https://www.alphavantage.co/query?function=TEMA&symbol=" + ticker + "&interval=weekly&time_period=10&series_type=open&apikey=" + apikey,
                "addrTRIMA": r"https://www.alphavantage.co/query?function=TRIMA&symbol=" + ticker + "&interval=weekly&time_period=10&series_type=open&apikey=" + apikey
                }
    dimDict =   {
                "addrPrice": "Time Series (Daily)", 
                "addrSMA": "Technical Analysis: SMA",
                "addrEMA": "Technical Analysis: EMA",
                "addrWMA": "Technical Analysis: WMA",
                "addrDEMA": "Technical Analysis: DEMA",
                "addrTEMA": "Technical Analysis: TEMA",
                "addrTRIMA": "Technical Analysis: TRIMA"
                }
    
    xLoopCnt = 0
    
    while xLoopCnt < len(runList):
        try:
            runListid = runList[xLoopCnt]
            filterValue = runDict[runListid]
            filterValuedim = dimDict[runListid]
            
            vl = Execute.main(filterValue, ticker, lookUpDt, filterValuedim)
            
            df = pd.DataFrame.from_dict(vl.PriceListx, orient='index')
            df.index.name = 'Date'
            
            df.to_csv(r"C:\Users\OutPut_" + ticker + "_" + runListid + ".csv")
            
            xLoopCnt += 1
            time.sleep(15)
        
        except Exception:
            traceback.print_exc()
            xLoopCnt += 1
            time.sleep(15)
            continue
        
        
