
from tkinter import *
from tkinter import ttk
import datetime
import requests


#database
def data_get():
    city=city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=4a27f7cca4807e26eaf54f2184537f3e").json()

    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    per_label1.config(text=data["main"]["pressure"])

#window
win = Tk()
win.title("Utkarsha`s WeatherApp")
win.config(bg="#0090FF")


#DateTime
date = datetime.datetime.now()
format_date = f"{date:%a, %b %d %Y}"
w = Label(win, text=format_date, fg="white", bg="#0090FF", font=("helvetica", 15,"bold"))
w.place(x=1000,y=25)
img5 = PhotoImage(file="SRC/clouds.png")
image = Label(win, image=img5, bg="#0090FF")
image.place(x=950, y=25, height=50, width=50)

#logo
win.geometry("1200x600")
logo = PhotoImage(file="SRC/cloudy.png")
image = Label(win, image=logo, bg="#0090FF")
image.place(x=15, y=15, height=50, width=50)

#label
name = Label(win,text="Weather Forcasting",font=('Helvetica',35,'bold'),fg="white",bg="#0090FF")
name.place(x=350,y=5,height=65,width=500)

#dropbox
city_name=StringVar()
list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

com = ttk.Combobox(win,text=(""),values=list_name,font=("Helvetica",20,"bold"),textvariable=city_name)
com.place(x=450,y=75,height=50,width=300)

#frame
frame = Frame(win,width=1200,height=400,bg="#2E2626")
frame.pack(side=BOTTOM)

#labels
w_label=Label(win,text=("Weather Climate"),font=("Helvetica",20),bg="#2E2626",fg="White")
w_label.place(x=80,y=260,height=50,width=210)
w_label1=Label(win,text=(""),font=("Helvetica",20,"bold"),bg="#2E2626",fg="White")
w_label1.place(x=95,y=300,height=50,width=210)
img1 = PhotoImage(file="SRC/clear-sky.png")
image = Label(win, image=img1, bg="#2E2626")
image.place(x=130, y=380, height=50, width=50)

wb_label=Label(win,text=("Pressure"),font=("Helvetica",20),bg="#2E2626",fg="White")
wb_label.place(x=850,y=260,height=50,width=210)
wb_label1=Label(win,text=(""),font=("Helvetica",20,"bold"),bg="#2E2626",fg="White")
wb_label1.place(x=375,y=300,height=50,width=210)
img2 = PhotoImage(file="SRC/cloud-data.png")
image = Label(win, image=img2, bg="#2E2626")
image.place(x=420, y=380, height=50, width=50)

temp_label=Label(win,text=("Weather Description"),font=("Helvetica",17),bg="#2E2626",fg="White")
temp_label.place(x=370,y=260,height=50,width=220)
temp_label1=Label(win,text=(""),font=("Helvetica",20,"bold"),bg="#2E2626",fg="White")
temp_label1.place(x=620,y=300,height=50,width=210)
img3 = PhotoImage(file="SRC/Temperature.png")
image = Label(win, image=img3, bg="#2E2626")
image.place(x=700, y=380, height=50, width=50)

per_label=Label(win,text=("Temperature"),font=("Helvetica",20),bg="#2E2626",fg="White")
per_label.place(x=650,y=260,height=50,width=210)
per_label1=Label(win,text=(""),font=("Helvetica",20,"bold"),bg="#2E2626",fg="White")
per_label1.place(x=820,y=300,height=50,width=210)
img4 = PhotoImage(file="SRC/pressure-gauge.png")
image = Label(win, image=img4, bg="#2E2626")
image.place(x=920, y=380, height=50, width=50)

#button
done_button = Button(win,text=("Done"),font=("Helvetica",15,"bold"),command=data_get,cursor="plus")
done_button.place(x=550,y=130,height=50,width=100)

win.mainloop()