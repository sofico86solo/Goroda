from opencage.geocoder import OpenCageGeocode
from tkinter import *
import webbrowser
from tkinter import messagebox as mb

def get_coord(city,key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city,language='ru')
        if results:
            lat= round(results[0]['geometry']['lat'],2)
            lon= round(results[0]['geometry']['lng'],2)
            country=results[0]['components']['country']
            valuta=results[0]['annotations']['currency']['name']
            #print(valuta)
            osm_url=f"https://www.openstreetmap.org/?mlat={lat}&mlon={lon}"
            if 'state' in results[0]['components']:
                region=results[0]['components']['state']
                return {
                    "coord":f"широта: {lat}, долгота: {lon} ,\nстрана: {country}, регион: {region},\n валюта :{valuta}","map_url":osm_url
                    }
            else:
                return {
                    "coord": f"широта: {lat}, долгота: {lon} \n страна: {country}",
                    "map_url": osm_url,"валюта":{valuta}}
        else:
            mb.showerror("Ошибка","Город не найден!")
    except Exception as e:
        return f"Возникла ошибка: {e}"

def show_coord(event=None):
    global map_url
    city=entry.get()
    rezult = get_coord(city, key)
    label.config(text=f"Координаты города {city} :\n {rezult['coord']}")
    map_url=rezult['map_url']

def show_map():
    global map_url
    if map_url:
        webbrowser.open(map_url)

def clear_all():
    global map_url
    label.config(text="")
    entry.delete(0,END)
    map_url=None

key='420a69538d734305b55566a2e5894b65'
map_url=""

win=Tk()
win.title("Координаты городов")
win.geometry("450x250")

entry=Entry()
entry.pack()
entry.bind("<Return>",show_coord)

button=Button(text="Поиск координат",command=show_coord).pack()

label=Label(text="Введите город и нажмите на кнопку поиска")
label.pack()

map_button=Button(text="Показать",command=show_map).pack()
clear_button=Button(text="Очистить",command=clear_all).pack()

win.mainloop()