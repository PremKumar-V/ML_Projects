import os
import opendatasets as od

dataDir = os.listdir(path = './dataset')

def downloadDataset(url, datasetName):
    if datasetName in dataDir:
        print("Dataset Already There ...")
    else:
        od.download(url, data_dir = './dataset/')
