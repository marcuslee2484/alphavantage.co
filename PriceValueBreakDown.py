######
'''
This will print a list, but also passes down the JSON
'''
######

class priceBreakDown:
    def __init__(self, OutputMeta, OutputValue, lookUpDt):
        for x in OutputMeta:
            print(str(x) + " : " + str(OutputMeta[x]))
    
        for dt in OutputValue:
            if str(dt) == lookUpDt:
                print(str(dt) + " ------------------- ")
                for dimname in OutputValue[dt]:
                    print(str(dimname) + " : ", end =" ")
                    print(OutputValue[dt][dimname])
                    
        self.OutputValuex = OutputValue

    def __repr__(self):
        return "Main Loop Function"