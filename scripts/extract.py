# Collect all data sources for training and testing into their own 
# respective pandas DataFrames

# import libraries
import pandas as pd
import os

# Lunar data paths
lunar_cat_directory = './data/lunar/training/catalogs/'
lunar_cat_file = lunar_cat_directory + 'apollo12_catalog_GradeA_final.csv'
lunar_train_dir = './data/lunar/training/data/S12_GradeA/'
lunar_test_dir = './data/lunar/test/data/'

# Mars data paths
mars_cat_directory = './data/mars/training/catalogs/'
mars_cat_file = mars_cat_directory + 'Mars_InSight_training_catalog_final.csv'
mars_train_dir = './data/mars/training/data/'
mars_test_dir = './data/mars/test/data/'

def extract_data(source, data_set, file_type):
    """
    This function extracts the given data and returns a pandas DataFrame
    """
    # Return lunar training data from csvs
    if (source == 'lunar' and data_set == 'train') and file_type == 'csv':
        # Lunar training data
        print('Extracting lunar training data...')
        lunar_train = []
        for file in os.listdir(lunar_train_dir):
            if file.endswith('.csv'):
                df = pd.read_csv(lunar_train_dir + file)
                df['filename'] = file
                lunar_train.append(df)
        
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
    
    # Return lunar catalog data
    elif (source == 'lunar' and data_set == 'catalog') and file_type == 'csv':
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
    
    elif (source == 'lunar' and data_set == 'test') and file_type == 'csv':
        # Lunar test data
        print('Extracting lunar test data...')
        lunar_test = []
        for dir in os.listdir(lunar_test_dir):
            for file in os.listdir(os.path.join(lunar_test_dir, dir)):
                if file.endswith('.csv'):
                    df = pd.read_csv(os.path.join(lunar_test_dir, dir, file))
                    df['directory'] = dir
                    df['filename'] = file
                    lunar_test.append(df)
        
        print('Concatenating lunar test data...')
        lunar_test_df = pd.concat(lunar_test)
        
        print('\nLunar Test Data Details')
        print('Shape:')
        print(lunar_test_df.shape)
        print('\nHead:')
        print(lunar_test_df.head())
        print('\nTail:')
        print(lunar_test_df.tail())
    
    elif (source == 'mars' and data_set == 'catalog') and file_type == 'csv':
        # Mars catalog data
        print('Extracting mars catalog data...')
        mars_cat = pd.read_csv(mars_cat_file)
        
        print('\nMars Catalog Data Details')
        print('Shape:')
        print(mars_cat.shape)
        print('\nHead:')
        print(mars_cat.head())
        print('\nTail:')
        print(mars_cat.tail())
        return mars_cat
    
    # Return mars training data from csvs
    elif (source == 'mars' and data_set == 'train') and file_type == 'csv':
        # Mars training data
        print('Extracting mars training data...')
        mars_train = []
        for file in os.listdir(mars_train_dir):
            if file.endswith('.csv'):
                df = pd.read_csv(mars_train_dir + file)
                df['filename'] = file
                mars_train.append(df)
        
        print('Concatenating mars training data...')
        mars_train_df = pd.concat(mars_train)
        
        print('\nMars Training Data Details')
        print('Shape:')
        print(mars_train_df.shape)
        print('\nHead:')
        print(mars_train_df.head())
        print('\nTail:')
        print(mars_train_df.tail())
        return mars_train_df
    
    # Return mars test data from csvs
    elif (source == 'mars' and data_set == 'test') and file_type == 'csv':
        # Mars test data
        print('Extracting mars test data...')
        mars_test = []
        for file in os.listdir(mars_test_dir):
            if file.endswith('.csv'):
                df = pd.read_csv(mars_test_dir + file)
                df['filename'] = file
                mars_test.append(df)
        
        print('Concatenating mars test data...')
        mars_test_df = pd.concat(mars_test)
        
        print('\nMars Test Data Details')
        print('Shape:')
        print(mars_test_df.shape)
        print('\nHead:')
        print(mars_test_df.head())
        print('\nTail:')
        print(mars_test_df.tail())
        return mars_test_df

    # Print suggestion for valid entry
    else:
        print("""Valid entries are ('lunar','train','csv'), ('lunar','catalog','csv'),
              ('lunar','test','csv'), ('mars','catalog','csv'), ('mars','train','csv'), 
              ('mars','test','csv')""")
