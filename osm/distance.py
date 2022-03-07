import numpy as np
def distance(lat1, lon1, lat2, lon2): 
    lat1 = np.deg2rad(lat1)
    lon1 = np.deg2rad(lon1)
    lat2 = np.deg2rad(lat2)
    lon2 = np.deg2rad(lon2)
    
    # Used the haversine formula from here https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points
    return(1000 * 6371 * 2 * np.arcsin(np.sqrt(np.sin((lat2 - lat1)/2.0)**2 + np.cos(lat1) * np.cos(lat2) * np.sin((lon2-lon1)/2.0)**2)))
