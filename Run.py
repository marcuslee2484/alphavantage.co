

#https://www.alphavantage.co/documentation/

import Execute
       
if __name__ == "__main__":
    
    ticker = input("Ticker:  ")
    lookUpDt = input("Select date: (YYYY-MM-DD)  ")
    
    if not ticker:
        ticker = "MSFT"
    
    if not lookUpDt:
        lookUpDt = '2019-01-18'
        
    ticker = str(ticker.upper())
    lookUpDt = str(lookUpDt)
    
    addr = r"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + ticker + "&apikey=demo"
    
    Execute.main(addr, ticker, lookUpDt)
