# CMPT353-Group-Project

### Installations required 
- The python package `hvplot` is required to run `HouseDataAnalysis.ipynb`(it can be installed using the command `pip3 install hvplot`)

### Imported Libraries
- `import pandas as pd`
- `from sklearn.model_selection import train_test_split`
- `from sklearn.preprocessing import StandardScaler`
- `from sklearn.preprocessing import MinMaxScaler`
- `from sklearn.pipeline import make_pipeline`
- `from sklearn import linear_model`
- `import sys`
- `import overpy`
- `import numpy as np`
- `import requests`
- `import scipy.stats as stats`
- `import seaborn as sns`
- `import matplotlib.pyplot as plt`
- `import hvplot.pandas`

These are already imported in the necessary files just make sure your computer is able to run them.

### Steps to extract data (Not necessary to run analysis; files already created)
1. Run `OsmDataExtraction.ipynb`(this will create `amenity_data.csv`)
2. Run `CleaningOsmData.ipynb`(this will take `amenity_data.csv` and create `rqd_data.csv` from it)
3. Run `AmenitiesToHouse.ipynb`(this will take `kc_house_data.csv` and `rqd_data.csv` then join them together to output `house_data.csv`, this may take up to a minute to run)
4. Run `HouseDataAnalysis.ipynb`(this will take `house_data.csv` and create `final_house_data.csv` from it) 

### Steps to run analysis
1. Open Terminal and go to the project
2. run the following command: `python3 prediction_models.py final_house_data.csv`
3. The code will print the scores of the models in the terminal.
