class DataFactory:
    '''Class to get the data through a DB pipeline and make it available for analysis'''
    def __init__(self,data_file_name):
        self.data_file_name = data_file_name
        
        return
    def __del__(self):
        return
    def printData(self):
        with open(self.data_file_name,'r') as fbuf:
            try:
                record = fbuf.readline().strip()
                while record != '':
                    print record
                    record = fbuf.readline().strip()
            except Exception as e:
                print "This is an Exception :",e
