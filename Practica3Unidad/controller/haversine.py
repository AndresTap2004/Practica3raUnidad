import math

def haversine(lon1, lat1, lon2, lat2):

    lon1_rad = math.radians(lon1)
    lat1_rad = math.radians(lat1)
    lon2_rad = math.radians(lon2)
    lat2_rad = math.radians(lat2)

    r = 6371

    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad

    a = (math.sin(dlat / 2) ** 2 +
         math.cos(lat1_rad) * math.cos(lat2_rad) *
         (math.sin(dlon / 2) ** 2))
    c = 2 * math.asin(math.sqrt(a))

    return c * r
