class dimValue:
    def __init__(self, request2):
        self.meta = request2["Meta Data"]
        self.timeSeries = request2["Time Series (Daily)"]
        
    def __repr__(self):
        return "DIM Function"