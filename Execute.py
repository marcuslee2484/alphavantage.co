class main:
    def __init__(self, addr, ticker, lookUpDt, filterValuedim):
    
        import PriceValueBreakDown
        import JsonMetaTimeSeries
        import requests
        import json
            
        request = requests.get(addr)
        request2 = request.text
        request2 = json.loads(request2)
        dimOut = JsonMetaTimeSeries.dimValue(request2, filterValuedim)
        
        OutputMeta = dimOut.meta
        OutputValue = dimOut.output
        
        PriceList = PriceValueBreakDown.priceBreakDown(OutputMeta, OutputValue, lookUpDt)
        self.PriceListx = PriceList.OutputValuex
            
    def __repr__(self):
        return "Lookup Function"
        