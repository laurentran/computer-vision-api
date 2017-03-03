import csv
import sys
import numpy as np

f = open(sys.argv[1], 'rb')
numFeatures = sys.argv[2]
reader = csv.reader(f)
ofile  = open('histograms.csv', "wb")
writer = csv.writer(ofile, delimiter=',')

imageIdx = 1
firstRun = True
bins = [0] * (int(numFeatures) + 1)
for row in reader:
    if firstRun == False:
        if int(row[1]) > imageIdx:   
            writer.writerow(bins)  
            bins = [0] * (int(numFeatures) + 1)
            imageIdx = imageIdx + 1
    # set 1st element to class label
    bins[0] = row[0]
    # get index of histogram bin
    binIdx = int(row[2]) + 1
    # increment value at bin
    bins[binIdx] = bins[binIdx] + 1
    firstRun = False
writer.writerow(bins)
        
 
f.close()
ofile.close()
