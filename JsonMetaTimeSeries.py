######
'''
This will grab the meta data information and grab JSON output by given the field
'''
######

class dimValue:
    def __init__(self, request2, filterValuedim):
        self.meta = request2["Meta Data"]
        
        try:
            self.output = request2[filterValuedim]
        except:
            pass

    def __repr__(self):
        return "DIM Function"