import random
import string
def run_this_module(data_file_name):    
    from DataFactory import *
    dataObj = DataFactory('records_file.csv')
    dataObj.printData()
def getRandomID(size = 3):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(size))
def getRandomProjectName(size = 2):
   # return ''.join(random.choice(string.ascii_uppercase) for _ in range(size))
    return ''.join(random.choice())
def getRandomField(size=2):
    return ''.join(random.choice(['CLOUD','DATABASE','TESTING','QA']))
def getRandomRating(size = 1):
    return ''.join(random.choice(string.digits) for _ in range(size))
def isInIdList(id_lst,rid):
    if rid in id_lst:
        return True
    else:
        id_lst.append(rid)
        return False
def getNumOfLines(file_name):
    with open(file_name) as f:
        return sum(1 for _ in f)

def populate_data_set(data_file_name,num_of_records):
    open(data_file_name,'w').close()
    with open(data_file_name,'w') as fbuf:
        fbuf.write("UniqueID,currentProjectName,currentProjectField,currentRating,previousProjectName,previousProjectField,previousProjectRating,previousProjectSatisfaction,firstProjectName,firstProjectField,firstProjectRating,firstProjectSatisfaction,satisfaction\n")
        id_list = []
        for _ in range(0,num_of_records):9
            rec_id = getRandomID()
            if isInIdList(id_list,rec_id):
                continue
            else:
                to_be_recorded = rec_id+','+str(getRandomProjectName())+','+str(getRandomField())+','+str(getRandomRating())+','+str(getRandomProjectName())+','+str(getRandomField())+','+str(getRandomRating())+','+str(getRandomRating())+','+str(getRandomProjectName())+','+str(getRandomField())+','+str(getRandomRating())+','+str(getRandomRating())+','+str(getRandomRating())+'\n'
                print to_be_recorded
                fbuf.write(to_be_recorded)
'''***************************************Main Section*************************************'''
FILE_NAME = 'records_file.csv'
PROJECT_LIST = ['ASD','ECI','VIPR','IIG','ISILON']
populate_data_set(FILE_NAME,100)
print "DATA SET Populated"
print "initiating matrix construction"
print getNumOfLines(FILE_NAME)
