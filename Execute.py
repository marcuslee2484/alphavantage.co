class main:
    def __init__(self, addr, ticker, lookUpDt):
    
        import PriceValueBreakDown
        import JsonMetaTimeSeries
        import requests
        import json
            
        request = requests.get(addr)
        request2 = request.text
        request2 = json.loads(request2)
        dimOut = JsonMetaTimeSeries.dimValue(request2)
        
        OutputMeta = dimOut.meta
        OutputValue = dimOut.timeSeries
        
        PriceValueBreakDown.priceBreakDown(OutputMeta, OutputValue, lookUpDt)
            
    def __repr__(self):
        return "Lookup Function"
        