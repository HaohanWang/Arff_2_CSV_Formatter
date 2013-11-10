__author__ = 'haohanwang'

import os
import csv
import sys

def getInputFiles():
    file_names = []
    for r, d, f in os.walk('inputData'):
        file_names = f
    if len(file_names)==0:
        sys.stderr.writelines('please put you .arff files into inputData')
        sys.exit()
    return file_names

def generageTmpFile(file_name):
    data = [line.strip() for line in open('inputData/'+file_name)]
    features = []
    value = []
    for line in data:
        if line.startswith('@'):
            if line.startswith('@ATTRIBUTE'):
                features.append(line.split()[1])
        else:
            value.append(line)
    f = open('temp/tmp.tab', 'w')
    f.writelines('\t'.join(features)+'\n')
    for line in value:
        f.writelines('\t'.join(line.split(','))+'\n')

def convertTabToCSV(file_name):
    txt_file = r"temp/tmp.tab"
    csv_file = r"outputData/"+file_name[:-4]+'csv'

    # use 'with' if the program isn't going to immediately terminate
    # so you don't leave files open
    # the 'b' is necessary on Windows
    # it prevents \x1a, Ctrl-z, from ending the stream prematurely
    # and also stops Python converting to / from different line terminators
    # On other platforms, it has no effect
    in_txt = csv.reader(open(txt_file, "rb"), delimiter='\t')
    out_csv = csv.writer(open(csv_file, 'wb'))
    out_csv.writerows(in_txt)

def removeTmpFile():
    os.remove('temp/tmp.tab')

def run():
    for file_name in getInputFiles():
        generageTmpFile(file_name)
        convertTabToCSV(file_name)
        removeTmpFile()
run()