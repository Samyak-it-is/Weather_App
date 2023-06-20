from tkinter import *
from tkinter import ttk
import requests

def get_data():
    city=city_name.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=773d06318c58a7e9cb91fa5760ef40e5").json()
    weatherc_label1.config(text=data["weather"][0]["main"])
    weatherd_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    pressure_label1.config(text=data["main"]["pressure"])

win =Tk()

win.title("Weather APP")
win.config(bg ="skyblue")
win.geometry("500x600")

name_label= Label(win,text="Weather App",font=("Times New Roman",30,"bold"))
name_label.place(x=25,y=50,height=50,width=450)
list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

city_name=StringVar()
com= ttk.Combobox(win,text="Weather App",values=list_name,font=("Times New Roman",30,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)

weatherc_label= Label(win,text="Weather Climate",font=("Times New Roman",20))
weatherc_label.place(x=25,y=260,height=50,width=210)
weatherc_label1= Label(win,text="",font=("Times New Roman",20))
weatherc_label1.place(x=250,y=260,height=50,width=210)

weatherd_label= Label(win,text="Weather Discription",font=("Times New Roman",17))
weatherd_label.place(x=25,y=330,height=50,width=210)
weatherd_label1= Label(win,text="",font=("Times New Roman",17))
weatherd_label1.place(x=250,y=330,height=50,width=210)

temp_label= Label(win,text="Temperture",font=("Times New Roman",17))
temp_label.place(x=25,y=400,height=50,width=210)
temp_label1= Label(win,text="",font=("Times New Roman",17))
temp_label1.place(x=250,y=400,height=50,width=210)

pressure_label= Label(win,text="Weather Pressure",font=("Times New Roman",17))
pressure_label.place(x=25,y=470,height=50,width=210)
pressure_label1= Label(win,text="",font=("Times New Roman",17))
pressure_label1.place(x=250,y=470,height=50,width=210)

done_button = Button(win,text="Done",font=("Times New Roman",30,"bold"),command=get_data)
done_button.place(x=200,y=190,height=50,width=100)

win.mainloop()