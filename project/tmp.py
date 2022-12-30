from geopy.distance import geodesic
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent='myapp')

all_cities = ["Narbonne", "Marseille", "Paris"]

def find_closer(all_cities, city):
    all_cities.remove(city)
    city = geolocator.geocode(city)
    res = {}
    cities = {}
    for i in range(0, len(all_cities)):
        cities[all_cities[i]] = geolocator.geocode(all_cities[i])
        res[all_cities[i]] = cities[all_cities[i]].latitude, cities[all_cities[i]].longitude
    for i in range(0, len(all_cities)):
        res[all_cities[i]] = geodesic((res[all_cities[i]]), (city.latitude, city.longitude)).km
    print(min(res))

closer(all_cities, "Narbonne")