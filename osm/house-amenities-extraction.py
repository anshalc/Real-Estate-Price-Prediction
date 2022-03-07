import pandas as pd

distance_value = 0.02

def amenities_check(lat, lon, amenities):
    # Creating range depending on our distance value
    lat_lower = lat - distance_value
    lat_higher = lat + distance_value
    lon_lower = lon - distance_value
    lon_higher = lon + distance_value
    
    # Filtering out any amenities not in our range then grouping by amenity type and counting how many there are of each type
    amenities = amenities[(lat_lower <= amenities['latitude']) & (amenities['latitude'] <= lat_higher) & (lon_lower <= amenities['longitude']) & (amenities['longitude'] <= lon_higher)]
    amenities = amenities.groupby(['amenities']).count()['latitude']

    # Initializing our return dictionary
    return_dictionary = {'food': 0, 'place_of_worship': 0, 'post_box': 0, 'car_services': 0, 'parking': 0, 'entertainment': 0, 'finance': 0, 'education': 0, 'animals': 0, 'rentals': 0, 'playgrounds': 0, 'negative_amenities': 0, 'storage': 0, 'self_care': 0, 'shopping': 0, 'transportation': 0, 'emergency': 0, 'healthcare': 0, 'child_services': 0}
    
    # Looping through Pandas series and adding value to return dictionary if applicable then returning the dictionary
    for amenity, value in amenities.items():
        return_dictionary[amenity] = value

    return return_dictionary


# Moving house and amenities data to dataframes
house_data = pd.read_csv('kc_house_data.csv')
amenities = pd.read_csv('rqd_data.csv')

# Filtering out the not needed category
amenities = amenities[amenities.amenities != 'not_needed']

# Applying amenities_check to each row and sorting results in a 'dictionary' column, and then exploding that column 
house_data['dictionary'] = house_data.apply(lambda row: amenities_check(row.lat, row.long, amenities), axis=1)
house_data2 = pd.json_normalize(house_data['dictionary'])

# Appending the exploded dictionary data frame with our original house data frame
house_data = pd.concat([house_data, house_data2], axis=1)
print(house_data)


