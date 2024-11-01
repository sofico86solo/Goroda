from opencage.geocoder import OpenCageGeocode


def get_coord(city,key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city,language='ru')
        if results:
            lat= round(results[0]['geometry']['lat'],2)
            lng= round(results[0]['geometry']['lng'],2)
            return f"широта: {lat}, долгота: {lng}"
        else:
            return "Город не найден!"
    except Exception as e:
        return f"Возникла ошибка: {e}"

key = '420a69538d734305b55566a2e5894b65'
city="Ростов"
coord=get_coord(city, key)
print(f"Координаты города {city} : {coord}")