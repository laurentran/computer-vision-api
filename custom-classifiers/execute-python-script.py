import numpy as np
import pandas as pd

df = pd.read_csv('cluster-assignments.csv')

m = df.iloc[df.shape[0]-1,1]
hists = pd.DataFrame(np.zeros((m, 101)))

for index, row in df.iterrows():
    # get values from row
    cluster = row[2]
    #print cluster
    image = row[1]
    label = row[0] 
    # image = row['image']
    # label = row['class'] 
    
    # set 1st element to class label
    hists.iloc[image-1,0] = label
    hists.iloc[image-1,cluster+1] += 1

    #print cluster
    #print hists.iloc[[image-1]]

print hists