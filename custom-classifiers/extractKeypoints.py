#import cv2
import numpy as np
from skimage import data, feature
from sklearn import cluster
import matplotlib.pyplot as plt
import csv
import os

ofile  = open('daisy_keypoints.csv', "wb")
writer = csv.writer(ofile, delimiter=',')
imageIdx = 0

imageLocations = ['starbucks/']
classIdx = 1

for location in imageLocations:
    for image in os.listdir(location):
        if image != '.DS_Store':

            imageIdx = imageIdx + 1

            img = data.imread(location + image, as_grey=True)

            descs, descs_img = feature.daisy(img, step=30, radius=10, rings=2, histograms=6, orientations=8, visualize=True)

            fig, ax = plt.subplots()
            ax.axis('off')
            ax.imshow(descs_img)
            descs_num = descs.shape[0] * descs.shape[1]
            ax.set_title('%i DAISY descriptors extracted:' % descs_num)
            plt.show()

            print descs.shape

            x = descs.shape[0] 
            y = descs.shape[1]
            z = descs.shape[2]

            daisy = np.zeros((x*y, z+2))

            idx = 0
            for i in range(x):
                for j in range(y):
                    row = descs[i][j]
                    row = np.insert(row, 0, imageIdx)
                    row = np.insert(row, 0, classIdx)
                    daisy[idx] = row
                    # print row
                    writer.writerow(row)
                    idx = idx + 1
        
    classIdx = classIdx + 1

ofile.close()
