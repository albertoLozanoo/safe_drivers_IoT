import weather_condition as wc
from tkinter import * 
from tkinter import messagebox,ttk
import tkinter as tk
import os, subprocess
#from PIL import Image, ImageTk

ci = ""
cities_interface = wc.cities
response = wc.url(ci)

temp_celsius_interface_round = 0.0
clouds_interface = 0
wind_speed_interface_round = 0.0
final_result_interface = 0
color  = "Null"

raiz = Tk()
raiz.geometry("800x750")
raiz.title("Safe Drivers app")

miFrame = Frame(raiz,width=700,height=400,bg='darkgreen',highlightbackground="white", highlightthickness=5,padx=50,pady=30)
miFrameB = Frame(raiz,width=200,height=50,bg='green',highlightbackground="white", highlightthickness=0,padx=10,pady=10)
miFrameA = Frame(raiz,width=200,height=50,bg='green',highlightbackground="white", highlightthickness=0,padx=10,pady=10)
miFrameT = Frame(raiz,width=200,height=50,bg='green',highlightbackground="white", highlightthickness=0,padx=10,pady=10)
#miFrameI = Frame(raiz,width=200,height=50,bg='darkgreen',highlightbackground="white", highlightthickness=5,padx=10,pady=10)

miFrame.pack(padx=5,pady=5,ipadx=30,ipady=30,fill=BOTH,expand=True)

miFrameA.pack(padx=5,pady=5,side=tk.TOP,fill='x',before=miFrame,expand=False)
miFrameT.pack(padx=5,pady=5,side=tk.TOP,fill=BOTH,before=miFrameA,expand=False)
#miFrameI.pack(padx=5,pady=5,side=tk.LEFT,fill=BOTH,before=miFrameT,expand=True)
miFrameB.pack(padx=5,pady=5,side=tk.BOTTOM,before=miFrame,fill='y',expand=False)

raiz.configure(background='green',padx=50,pady=50)
 
title_window = Label(miFrameA, text= "Select a location: ",fg='white', font=("Roboto", 18),bg='green')
title_window.pack(side=tk.LEFT,padx=10,pady=5)

combo = ttk.Combobox(miFrameA)
combo = ttk.Combobox(miFrameA,
    state="readonly",
    values=["Arrigorriaga",'Lemona','Salamanca','Madrid','Zamora','Pamplona','Zaragoza','Palencia','Valencia','Sevilla','Granada','Jaen',"Not Selected"],
    background="darkgreen",
)
combo.pack(padx = 20, pady = 5,after=title_window,side=tk.LEFT,fill='x',expand=True)

welcoming = Label(miFrameT, text= "SAFE DRIVERS",fg='white', font=("Roboto bold", 45),bg='green')
welcoming.pack()

# Create a photoimage object of the image in the path
#image1 = Image.open("E:/Universidad/4ºAño/IoT/final-project/trafico.png")
#test = ImageTk.PhotoImage(image1)
#label1 = Label(miFrameT,image=test,bg="green")
#label1.image = test
# Position image
#label1.place(x=0, y=7)

def __init__layer(temp_celsius_interface_round,clouds_interface,wind_speed_interface_round,final_result_interface,color):

    for i in range(0,7):
        miFrame.grid_rowconfigure(i, weight=1)
      
    miFrame.grid_columnconfigure(0, weight=1)
    miFrame.grid_columnconfigure(1, weight=1)
    
    temperature_title = Label(miFrame, text= "Temperature : ",fg='white', font=("Roboto", 14),bg='darkgreen')
    temperature_title.grid(row=2,column=0,padx=10,pady=10)
    temperature = Label(miFrame, text="{} (C)".format(temp_celsius_interface_round),fg='white', font=("Roboto bold", 17),bg='darkgreen')
    temperature.grid(row=2,column=1,padx=10,pady=10)

    clouds_title = Label(miFrame, text= "Clouds : ",fg='white', font=("Roboto", 14),bg='darkgreen')
    clouds_title.grid(row=3,column=0,padx=10,pady=10)
    nubes = Label(miFrame, text ="{}%".format(clouds_interface),fg='white', font=("Roboto bold", 17),bg='darkgreen')
    nubes.grid(row=3,column=1,padx=10,pady=10)

    wind_speed_tittle = Label(miFrame, text= "Wind Speed : ",fg='white', font=("Roboto", 14),bg='darkgreen')
    wind_speed_tittle.grid(row=4,column=0,padx=10,pady=10)
    viento = Label(miFrame,text ="{} m/s".format(wind_speed_interface_round),fg='white', font=("Roboto bold", 17),bg='darkgreen')
    viento.grid(row=4,column=1,padx=10,pady=10)

    result_tittle = Label(miFrame, text= "Result : ",fg='white', font=("Roboto", 14),bg='darkgreen')
    result_tittle.grid(row=5,column=0,padx=10,pady=10)
    resultado_num = Label(miFrame,text="{}/100".format(final_result_interface),fg='white', font=("Roboto bold", 17),bg='darkgreen')
    resultado_num.grid(row=5,column=1,padx=10,pady=10)

    color_tittle = Label(miFrame, text= "Color : ",fg='white', font=("Roboto", 14),bg='darkgreen')
    color_tittle.grid(row=6,column=0,padx=10,pady=10)
    resultado_col = Label(miFrame,text=color,fg='white', font=("Roboto bold", 17),bg='darkgreen')
    resultado_col.grid(row=6,column=1,padx=10,pady=10)


ciudad_title = Label(miFrame, text= "Location : ",fg='white', font=("Roboto", 14),bg='darkgreen')
ciudad_title.grid(row=1,column=0,padx=10,pady=10,sticky="nsew")
ciudad = Label(miFrame, text="Not selected",fg='white', font=("Roboto bold", 17),bg='darkgreen')
ciudad.grid(row=1,column=1,padx=10,pady=10)

__init__layer(temp_celsius_interface_round,clouds_interface,wind_speed_interface_round,final_result_interface,color )

def when_clicked():
    list = miFrame.grid_slaves()
    for l in list:
        l.destroy()

    if (combo.get() == "Not Selected" or combo.get() ==""):
        c = wc.random_city()
        new_response = wc.url(c)
        temp_celsius_interface_round2,clouds_interface,wind_speed_interface_round,final_result_interface,color  = wc.__main__(c,new_response)

        ciudad_title = Label(miFrame, text= "Location : ",fg='white', font=("Roboto", 14),bg='darkgreen')
        ciudad_title.grid(row=1,column=0,padx=10,pady=10)
        ciudad = Label(miFrame, text=c,fg='white', font=("Roboto bold", 17),bg='darkgreen')
        ciudad.grid(row=1,column=1,padx=10,pady=10)

        __init__layer(temp_celsius_interface_round2,clouds_interface,wind_speed_interface_round,final_result_interface,color )
    else:
        for i in range(len(cities_interface)):
            if(cities_interface[i] == combo.get()):
                c = cities_interface[i]
                new_response = wc.url(c)
                temp_celsius_interface_round2,clouds_interface,wind_speed_interface_round,final_result_interface,color  = wc.__main__(c,new_response)

                ciudad_title = Label(miFrame, text= "Location : ",fg='white', font=("Roboto", 14),bg='darkgreen')
                ciudad_title.grid(row=1,column=0,padx=10,pady=10)
                ciudad = Label(miFrame, text=c,fg='white', font=("Roboto bold", 17),bg='darkgreen')
                ciudad.grid(row=1,column=1,padx=10,pady=10)

                __init__layer(temp_celsius_interface_round2,clouds_interface,wind_speed_interface_round,final_result_interface,color )    

boton = Button(miFrameB,text="Buscar",command=when_clicked,fg='white', font=("Roboto bold", 18),bg='darkgreen').pack(expand=False,fill='x')

raiz.mainloop()

