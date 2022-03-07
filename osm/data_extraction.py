import pandas as pd

stations = pd.read_json('amenities-vancouver.json.gz', lines=True)

data = pd.read_csv('kc_house_data.csv')
print('minimum lat is: ' + str(data['lat'].min()))
print('maximum lat is: ' + str(data['lat'].max()))
print('minimum long is: ' + str(data['long'].min()))
print('maximum long is: ' + str(data['long'].max()))