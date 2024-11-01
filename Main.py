from opencage.geocoder import OpenCageGeocode


def get_coord(city,key):
    geocoder = OpenCageGeocode(key)
    query = city
    results = geocoder.geocode(query)
    if results:
        return results[0]['geometry']['lat'], results[0]['geometry']['lng']
    else:
        return "Город не найден!"

key = '420a69538d734305b55566a2e5894b65'
city="Moscow"
coord=get_coord(city, key)
print(f"Координаты города {city} : {coord}")