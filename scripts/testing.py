import extract

lunar_train = extract.extract_data('lunar', 'train', 'csv')
lunar_catalog = extract.extract_data('lunar', 'catalog', 'csv')
mars_train = extract.extract_data('mars', 'train', 'csv')
mars_catalog = extract.extract_data('mars', 'catalog', 'csv')
mars_test = extract.extract_data('mars', 'test', 'csv')