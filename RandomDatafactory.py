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
        is_valid,descriptor_list = scanDescriptorFile(descriptor_file)
        if is_valid:
            self.descriptor_list = descriptor_list
            self.data_file_name = output_data_file_name
        else:
            print 'Invalid Description, Object not properly created'
            exit(0)
        return
    def scanDescriptorFile(descriptor_file):
        with open(descriptor_file, 'r') as f:
            arg = f.readline().strip()
            while arg != '':

