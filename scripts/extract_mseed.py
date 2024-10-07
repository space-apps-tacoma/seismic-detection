# Collect all mseed data sources of interest

# import libraries
import os
from obspy import read

# Directories
mars_train_dir = './data/mars/training/data/'

def extract_mseed():

    data = []
    for file in os.listdir(mars_train_dir):
        if file.endswith('.mseed'):
            st = read(f'{mars_train_dir}{file}')
            data.append(st)
    return(data)