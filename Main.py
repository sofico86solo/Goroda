from opencage.geocoder import OpenCageGeocode
from tkinter import *

def get_coord(city,key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city,language='ru')
        if results:
            lat= round(results[0]['geometry']['lat'],2)
            lng= round(results[0]['geometry']['lng'],2)
            country=results[0]['components']['country']
            if 'state' in results[0]['components']:
                region=results[0]['components']['state']
                return f"широта: {lat}, долгота: {lng} \n страна: {country} регион: {region}"
            else:
                return f"широта: {lat}, долгота: {lng} \n страна: {country}"
        else:
            return "Город не найден!"
    except Exception as e:
        return f"Возникла ошибка: {e}"

def show_coord(event=None):
    city=entry.get()
    coord = get_coord(city, key)
    label.config(text=f"Координаты города {city} :\n {coord}")

key='420a69538d734305b55566a2e5894b65'

win=Tk()
win.title("Координаты городов")
win.geometry("400x150")

entry=Entry()
entry.pack()
entry.bind("<Return>",show_coord)

button=Button(text="Поиск координат",command=show_coord).pack()

label=Label(text="Введите город и нажмите на кнопку поиска")
label.pack()

win.mainloop()