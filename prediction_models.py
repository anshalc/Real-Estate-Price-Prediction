import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import make_pipeline
from sklearn import linear_model
import sys

house_data_file = sys.argv[1]
house_data = pd.read_csv(house_data_file)

X = house_data[['date','bedrooms', 'bathrooms', 'sqft_living',
       'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade',
       'sqft_above', 'sqft_basement', 'yr_built',
       'sqft_living15', 'sqft_lot15', 'food', 'place_of_worship', 'post_box',
       'car_services', 'parking', 'entertainment', 'finance', 'education',
       'animals', 'negative_amenities', 'storage', 'self_care', 'shopping',
       'transportation', 'emergency', 'healthcare', 'child_services', 'age']]
y = house_data['price']


X_train1, X_valid1, y_train1, y_valid1 = train_test_split(X, y)


model_with_amenities = make_pipeline(StandardScaler(), linear_model.LinearRegression())
model_with_amenities.fit(X_train1,y_train1)
# print(model_with_amenities.score(X_valid,y_valid), 
#       model_with_amenities.score(X_train,y_train))


X = house_data[['date','bedrooms', 'bathrooms', 'sqft_living',
       'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade',
       'sqft_above', 'sqft_basement', 'yr_built',
       'sqft_living15', 'sqft_lot15', 'age']]
y = house_data['price']


X_train2, X_valid2, y_train2, y_valid2 = train_test_split(X, y)

model_without_amenities = make_pipeline(StandardScaler(), linear_model.LinearRegression())
model_without_amenities.fit(X_train2,y_train2)
# print(model_without_amenities.score(X_valid,y_valid), 
#       model_without_amenities.score(X_train,y_train))

print()
print('Scores for model with amenities:')
print('Score with validation data: '  ,model_with_amenities.score(X_valid1,y_valid1))
print('Score with trainging data: '  ,model_with_amenities.score(X_train1,y_train1))
print()
print('Scores for model without amenities:')
print('Score with validation data: '  ,model_without_amenities.score(X_valid2,y_valid2))
print('Score with trainging data: '  ,model_without_amenities.score(X_train2,y_train2))
print()
