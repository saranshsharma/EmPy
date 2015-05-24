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
        self.descriptor_list = []
        if scanDescriptorFile(descriptor_file):
            self.data_file_name = output_data_file_name
            self.number_of_records = number_of_records
        else:
            print 'Invalid Description, Object not properly created'
            exit(0)
        return
    def scanDescriptorFile(descriptor_file):
        try:
            with open(descriptor_file, 'r') as f:
                arg = f.readline().strip()
                self.descriptor_list.append(arg)
                arg = f.readline().strip()
                while arg != '':
                    switchAndAddToDescriptionList(arg)
                    arg = f.readline().strip()
        except Exception as e:
            print e
            print 'Invalid Description, Object not properly created'
            return False
        return True
    def switchAndAddtoDescriptionList(arg):
        arg_lst = arg.split(',');
            if arg_lst[0] == '0':
                self.descriptor_list.append(str([arg_lst[0]),str(arg_lst[1]]))
            elif arg_lst[0] == '1':
                self.descriptor_lst.append(str
