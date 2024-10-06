# seismic-detection

NASA Space Apps 2024 entry from team Seismic Surge for the challenge of Seismic Detection Across the Solar System

## Loading Space Apps Data

Data for this challenge can be found at the NASA Space App Challenge Page [Seismic Detection Across the Solar System](https://www.spaceappschallenge.org/nasa-space-apps-2024/challenges/seismic-detection-across-the-solar-system/?tab=resources). 
Click on the Space Apps 2024 Seismic Detection Data Packet to download the data and demo notebook as a zipped folder. Due to the size of the 
data directory, it is missing from this repository as it is included in the gitignore. The data can be set up in a local or Google Colab 
environment with the steps below.

### Local Environment
Once you have downloaded the data packet and unzipped the folder, the data directory can be copied into the main directory for this 
cloned repository to be used locally.

### Colab Environment

To access the data through a shared Google Colab notebook, the project repository can be uploaded to a shared Google drive and then 
mounted to the notebook using the code below. This is utilized in the `nasa2024_colab_notebook.ipynb`.

```python
from google.colab import drive
drive.mount('/content/drive')
```

```python
%cd /content/drive/My Drive/space_apps_2024_seismic_detection
```

## Installing Dependencies

With your environment ready, you can install the dependencies by running the following command from your terminal:
`pip install -r requirements.txt`

## Extracting Data

The `extract.py` script can be used to extract and returned the desired data as a single pandas DataFrame. The extract_data 
function within this script loops through the data sets of interest and concatenates them together while performing data cleaning and 
transformations as needed. Each data set of interest can be obtained with the code below:

```python
import extract

lunar_train = extract.extract_data('lunar', 'train', 'csv')
lunar_catalog = extract.extract_data('lunar', 'catalog', 'csv')
lunar_test = extract.extract_data('lunar', 'test', 'csv')
mars_train = extract.extract_data('mars', 'train', 'csv')
mars_catalog = extract.extract_data('mars', 'catalog', 'csv')
mars_test = extract.extract_data('mars', 'test', 'csv')
```

## Interpreting Data

### Lunar Seismic Data

### Mars Seismic Data
 
The `mars_demo_notebook.ipynb` takes the lunar `demo_notebook.ipynb` and adapts the code to be capable of handling data in the mars files, 
such as accounting for differences between file structures and frequencies measured.
* Bandpass - a function in obspy that helps with filtering data. In this case it filters out data between the min and max frequencies given.
* Highpass - similar to bandpass but handles frequencies above 10 hz, which is bandpass cap. this is the one mars data uses to filter, but the 
notebook will recognize that bandpass can't handle it and automatically shift to highpass. frequencies above the specified frequency are 
allowed through.
* Lowpass - frequencies below the given frequency are  allowed to come through.

## Model Development

There are many different options for model development, such as pre-built neural networks for earthquake detection, event detection, or 
even designing a model from scratch.

### Pre-Built Models

#### EQTransformer

There is a python package, [EQTransformer](https://github.com/smousavi05/EQTransformer), for signal detection and phase picking using AI 
(Tensorflow). This model is an intriguing option as it is tuned for earthquake detection. As noted in their paper, [Earthquake transformer—an attentive deep-learning model for simultaneous earthquake detection and phase picking](https://www.nature.com/articles/s41467-020-17591-w),
phase picking refers to measuring the arrival time of the seismic P and S wave phases. These phases are useful for estimating the location 
of the seismic activity. This could allow for more accuracy when it comes to the start and stop times of such seismic events, or for 
using either P or S wave to determine the general time of an event. Both the P and S waves can be seen in the image below from their paper.

![P and S waves in EQTransformer](images/p_and_s_waves.JPG)

When working to install the package, we kept running into a ModuleNotFoundError: No mudle named 'distutils.msvcompiler'. Further documentation 
for EQTransformer can be found at [EQTransformer Docs](https://eqtransformer.readthedocs.io/en/latest/index.html).

#### 

#### Custom Models