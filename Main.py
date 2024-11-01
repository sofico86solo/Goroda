from opencage.geocoder import OpenCageGeocode


def get_coord(city,key):
    try:
        geocoder = OpenCageGeocode(key)
        query = city
        results = geocoder.geocode(query)
        if results:
            return results[0]['geometry']['lat'], results[0]['geometry']['lng']
        else:
            return "Город не найден!"
    except Exception as e:
        return f"Возникла ошибка: {e}"

key = '420a69538d734305b55566a2e5894b65'
city="London"
coord=get_coord(city, key)
print(f"Координаты города {city} : {coord}")