from checkFunctions import wide_transform

class wideCheck(object):
    
    def __init__(self, list):

        """List will be in the form [A,B,C] where A is an object, A:{name: A, time_client: '2h', booking_time: 1400, list_index = 0}"""
        self.list = list
    
    def x(self,string):
        """call a specific function"""
        newstring = string
        return newstring

zhiyuan = wideCheck([1,2,3])

print(zhiyuan.x('hello'))
    

    
        