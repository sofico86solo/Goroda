from opencage.geocoder import OpenCageGeocode
from tkinter import *
import webbrowser

def get_coord(city,key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city,language='ru')
        if results:
            lat= round(results[0]['geometry']['lat'],2)
            lon= round(results[0]['geometry']['lng'],2)
            country=results[0]['components']['country']
            osm_url=f"https://www.openstreetmap.org/?mlat={lat}&mlon={lon}"
            if 'state' in results[0]['components']:
                region=results[0]['components']['state']
                return {
                    "coord":f"широта: {lat}, долгота: {lon} \n страна: {country} регион: {region}",
                    "map_url":osm_url }
            else:
                return {
                    "coord": f"широта: {lat}, долгота: {lon} \n страна: {country}",
                    "map_url": osm_url}

        else:
            return "Город не найден!"
    except Exception as e:
        return f"Возникла ошибка: {e}"

def show_coord(event=None):
    global map_url
    city=entry.get()
    rezult = get_coord(city, key)
    label.config(text=f"Координаты города {city} :\n {rezult['coord']}")
    map_url=rezult['map_url']

def show_map():
    if map_url:
        webbrowser.open(map_url)


key='420a69538d734305b55566a2e5894b65'
map_url=""

win=Tk()
win.title("Координаты городов")
win.geometry("400x150")

entry=Entry()
entry.pack()
entry.bind("<Return>",show_coord)

button=Button(text="Поиск координат",command=show_coord).pack()

label=Label(text="Введите город и нажмите на кнопку поиска")
label.pack()

map_button=Button(text="Показать",command=show_map).pack()

win.mainloop()