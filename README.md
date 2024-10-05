# seismic-detection

NASA Space Apps 2024 entry from team Seismic Surge for the challenge of Seismic Detection Across the Solar System

## Loading Space Apps Data

Data for this challenge can be found at the NASA Space App Challenge Page [Seismic Detection Across the Solar System](https://www.spaceappschallenge.org/nasa-space-apps-2024/challenges/seismic-detection-across-the-solar-system/?tab=resources). 
Click on the Space Apps 2024 Seismic Detection Data Packet to download the data and demo notebook as a zipped folder.

Once you have downloaded the data packet and unzipped the folder, the data directory can be copied into the main directory for this 
cloned repository.

## Installing Dependencies

With your environment ready, you can install the dependencies by running the following command from your terminal:
`pip install -r requirements.txt`

## Extracting Data

The `extract.py` script will extract and returned the desired data as a single pandas DataFrame. The extract_data 
function within this script loops through the data sets of interest and concatenates them together. Each data set 
of interest can be obtained with the code below:

```python
import extract

lunar_train = extract.extract_data('lunar', 'train', 'csv')
lunar_catalog = extract.extract_data('lunar', 'catalog', 'csv')
mars_train = extract.extract_data('mars', 'train', 'csv')
mars_catalog = extract.extract_data('mars', 'catalog', 'csv')
mars_test = extract.extract_data('mars', 'test', 'csv')
```

## Interpreting Data

### Lunar Seismic Data

### Mars Seismic Data
