import pandas as pd
import numpy as np

def azureml_main(dataframe1 = None, dataframe2 = None):
    print dataframe1
    m = dataframe1.iloc[dataframe1.shape[0]-1,1]
    k = 300  # size of k from k-means clustering
    
    # initialize dataframe of all 0s, with size (m x vocab size)
    hists = pd.DataFrame(np.zeros((m, k+1)))
    
    
    for i, row in dataframe1.iterrows():
        # get values from row
        cluster = int(row[2])
        image = int(row[1])
        label = int(row[0])

        # set 1st element to class label
        hists.iloc[image-1,0] = label
        # print i, label, image, cluster
        
        # increment value 
        hists.iloc[image-1,cluster+1] += 1
        
    return hists
