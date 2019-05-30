# alphavantage.co
Alphavantage.co API - Prints values from JSON file.

Run.py will ask for a ticker and date. A default value will show if nothing was entered: MSFT, 2019-01-18.
Demo API Key is used - You can sign up for a free key.

Run.py calls Execute.py. Uses the input data to pull a JSON output using requests.

JsonMetaTimeSeries.py provides meta data info.

PriceValueBreakDown.py provides values based on the date. Additional objects can be added here.

Sample:
1. Information : Daily Prices (open, high, low, close) and Volumes
2. Symbol : MSFT
3. Last Refreshed : 2019-05-30 16:00:01
4. Output Size : Compact
5. Time Zone : US/Eastern
2019-01-15 ------------------- 
1. open :  102.5100
2. high :  105.0500
3. low :  101.8800
4. close :  105.0100
5. volume :  31587616
