# Collect all data sources for training and testing into their own 
# respective pandas DataFrames

# import libraries
import pandas as pd
import os

# Lunar data paths
lunar_cat_directory = './data/lunar/training/catalogs/'
lunar_cat_file = lunar_cat_directory + 'apollo12_catalog_GradeA_final.csv'
lunar_train_dir = './data/lunar/training/data/S12_GradeA/'

# Mars data paths
mars_cat_directory = './data/mars/training/catalogs/'
mars_cat_file = mars_cat_directory + 'Mars_InSight_training_catalog_final.csv'

def extract_data(source, data_set, source_type):
    """
    This function extracts the given data and returns a pandas DataFrame
    """
    if (source_type == 'lunar' and data_set == 'train') and source_type == 'csv':
        # Lunar training data
        print('Extracting lunar training data...')
        lunar_train = []
        for file in os.listdir(lunar_train_dir):
            if file.endswith('.csv'):
                lunar_train.append(pd.read_csv(lunar_train_dir + file))
        
        print('Concatenating lunar training data...')
        lunar_train_df = pd.concat(lunar_train)
        
        print('\nLunar Training Data Details')
        print('Shape:')
        print(lunar_train_df.shape)
        print('\nHead:')
        print(lunar_train_df.head())
        print('\nTail:')
        print(lunar_train_df.tail())
        return lunar_train_df
    
    elif (source_type == 'lunar' and data_set == 'catalog') and source_type == 'csv':
        # Lunar catalog data
        print('Extracting lunar catalog data...')
        lunar_cat = pd.read_csv(lunar_cat_file)
        
        print('\nLunar Catalog Data Details')
        print('Shape:')
        print(lunar_cat.shape)
        print('\nHead:')
        print(lunar_cat.head())
        print('\nTail:')
        print(lunar_cat.tail())
        return lunar_cat
    else:
        print("""Valid entris are ['lunar','train','csv'], ['lunar','catalog','csv']""")

# Mars catalog data
mars_cat = pd.read_csv(mars_cat_file)
mars_cat['filename'] = mars_cat['filename'].str.replace('.csv','')
