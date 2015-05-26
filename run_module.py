from sets import Set
from DataFactory import *
import sys
import random
import string
'''Global declarations'''
NUM_OF_RECORDS = 10000
FILE_NAME = 'records_file.csv'
PROJECT_LIST = ['ASD','ECI','VIPR','IIG','ISILON']
FIELD_LIST = ['CLOUD','DATABASE','TESTING','QA']


def run_this_module(data_file_name):
    dataObj = DataFactory('records_file.csv')
    dataObj.printData()


def getRandomID(size = 3):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(size))


def getRandomProjectName(size = 2):
   # return ''.join(random.choice(string.ascii_uppercase) for _ in range(size))
    return ''.join(random.choice(PROJECT_LIST))


def getRandomField(size=2):
    return ''.join(random.choice(FIELD_LIST))


def getRandomRating(size = 1):
    return ''.join(random.choice(string.digits) for _ in range(size))


def isInIdSet(id_lst,rid):
    if rid in id_lst:
        return True
    else:
        id_lst.add(rid)
        return False

def isInIdFile(rid):
    is_in_id_file = False
    with open('id_lst','r') as f:
        rec_id = f.readline().strip()
        while rec_id != '':
            if rid==rec_id:
                is_in_id_file = True
                break
            rec_id = f.readline().strip()
    if is_in_id_file:
        with open('id_lst','a') as f:
            f.write(str(rid)+'\n')
        return True
    else:
        return False


def getNumOfLines(file_name):
    with open(file_name,'r') as f:
        rec = f.readline()
        counter = 0
        while rec != '':
            counter += 1
            rec = f.readline()
        return counter


def populate_data_set(data_file_name,num_of_records):
    open(data_file_name,'w').close()
    print num_of_records
    counter = 0
    with open(data_file_name,'w') as fbuf:
        fbuf.write("UniqueID,currentProjectName,currentProjectField,currentRating,previousProjectName,previousProjectField,previousProjectRating,previousProjectSatisfaction,firstProjectName,firstProjectField,firstProjectRating,firstProjectSatisfaction,satisfaction\n")
        open('id_lst','w').close()
        while num_of_records > 0:
            rec_id = getRandomID()
            if isInIdFile(rec_id):
                continue
            else:
                to_be_recorded = rec_id+','+str(getRandomProjectName())+','+str(getRandomField())+','+str(getRandomRating())+','+str(getRandomProjectName())+','+str(getRandomField())+','+str(getRandomRating())+','+str(getRandomRating())+','+str(getRandomProjectName())+','+str(getRandomField())+','+str(getRandomRating())+','+str(getRandomRating())+','+str(getRandomRating())+'\n'
                #print to_be_recorded
                #print to_be_recorded
                #print num_of_records
                fbuf.write(to_be_recorded)
                if num_of_records%1000 == 0:
                    print num_of_records," records left to be populated"
                num_of_records -= 1
'''***************************************Main Section*************************************'''
def main():
    populate_data_set(FILE_NAME,NUM_OF_RECORDS)
    print "DATA SET Populated"
    print "initiating matrix construction"
    num_of_lines = getNumOfLines(FILE_NAME)
    print num_of_lines
    if num_of_lines < NUM_OF_RECORDS:
        sys.exit(0)
main()
