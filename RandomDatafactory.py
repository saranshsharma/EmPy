''' 
    Random Data Factory
for populating a file with data as  defined by the descriptor file
descriptor file name is given as an input and the format for descriptor file is as follows
___________________________
>number of records to inserted
>argument name[,details]
details format
string,len of string
>0,len
integer,int min,int max
>1,int l,int m
float,int min,int max, precision
>2,int l,int m, prec
elements from custom list
>3[,list_elements]

'''
class RandomDataFactory:
    def __init__(self,descriptor_file,output_data_file_name):
        is_valid,number_of_records,descriptor_list = scanDescriptorFile(descriptor_file)
        if is_valid:
            self.descriptor_list = descriptor_list
            self.data_file_name = output_data_file_name
            self.number_of_records = number_of_records
        else:
            print 'Invalid Description, Object not properly created'
            exit(0)
        return
    def scanDescriptorFile(self,descriptor_file):
        try:
            with open(descriptor_file, 'r') as f:
                arg = f.readline().strip()
                number_of_records = int(arg)
                arg = f.readline().strip()
                descriptor_list = []
                while arg != '':
                    addToDescriptionList(arg,descriptor_list)
                    arg = f.readline().strip()

        except Exception as e:
            print e
            print 'Invalid Description, Object not properly created'
            exit(0)
    def addToDescriptionList(self,arg,descriptor_list):
        arg_lst = arg.split(',')
        if arg_lst[0] == '0':
            
