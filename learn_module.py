'''Global Declarations'''
SPLIT_RATIO = 0.2
from sklearn import svm
from run_module import *
import numpy as np


def getTranslation(element):
    if element in PROJECT_LIST:
        return PROJECT_LIST.index(element)
    elif element in FIELD_LIST:
        return FIELD_LIST.index(element)
    else:
        return int(element)


def getColumnSize(fname):
    with open(fname, 'r') as f:
        return len(f.readline().strip().split(','))


def getShape(f_name):
    return int(getNumOfLines(f_name))-1, int(getColumnSize(f_name)-1)


def meetsSplitCriteria(splt_count):
    if splt_count > 0:
        if random.choice([True, False]):
            #print splt_count
            return False
    return True


def createMatrix(f_name, data_arr, test_data_arr, num_of_records):
    with open(f_name, 'r') as f:
        record = f.readline()
        # to ignore the first line of data set
        rsize, csize = data_arr.shape
        #I've added a test matrix we need to change the record size to original
        splt_count = num_of_records * (SPLIT_RATIO)
        rsize = num_of_records
        i_data = 0
        i_test_data = 0
        #print 'the split count is', splt_count
        for i in range(rsize):
            print 'on the record number ',i
            record = f.readline().strip().split(',')
            if meetsSplitCriteria(splt_count):
                for j in range(csize):
                    data_arr[i_data][j] = int(getTranslation(str(record[j+1])))
                i_data += 1
            else:
                splt_count -= 1
                for j in range(csize):
                    test_data_arr[i_test_data][j] = int(getTranslation(str(record[j+1])))
                i_test_data += 1
    return


def printNumPyMatrix(data_arr):
    rs, cs = data_arr.shape
    for i in range(rs):
        for j in range(cs):
            print data_arr[i][j],
        print '\n'


def getPrediction(data_arr, test_data_arr):
    rs, cs = data_arr.shape
    sample_arr = data_arr[:,cs-1]
    test_sample_arr = test_data_arr[:,cs-1]
    #print ">>>",sample_arr,"<<<"
    print 'mapping matrices created'
    cfg = svm.SVC()
    cfg.fit(data_arr,sample_arr)
    print 'data has been fitted'

    print "score is",cfg.score(test_data_arr,test_sample_arr)
    #print "the prediction is ",cfg.predict(data_arr[0,:])


def numPyTest():
    row,col = getShape(FILE_NAME)
    #print 'row = %d and col = %d'%(row,col)
    data_arr = np.zeros((row*(1-SPLIT_RATIO),col))
    test_data_arr = np.zeros((row*(SPLIT_RATIO),col))
    #print data_arr
    createMatrix(FILE_NAME,data_arr,test_data_arr,row)
    #printNumPyMatrix(data_arr)
    #print data_arr
    #print data_arr[0]
    getPrediction(data_arr,test_data_arr)
    return


def main():
    numPyTest()


main()
