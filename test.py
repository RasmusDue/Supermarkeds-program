import tkinter
from tkinter import *
from PIL import ImageTk,Image


master = Tk()
master.title("Tegninger")
e = Entry(master)

canvas=Canvas(master,width=500,height=450)
#hej
#562 x 446
#image=ImageTk.PhotoImage(Image.open("robot2.jpg"))

#canvas.create_image(250,225,anchor=CENTER,image=image)
canvas.pack()

#color#
ColorInput = "light sky blue"

Color = "snow"


Vare_liste = Listbox(master, width=40)
Vare_liste.place(x=250, y=200)
# inkoebs_liste.insert(END, '')

title_supermarkede = Label(master, text= 'Supermarkede', width = 50, height = 2, bg = ColorInput).place(x=80, y=10)
#title_supermarkede.grid(column =2, row = 0)

Vare = Label(master, text= 'Vare', width = 35, height = 2, bg = ColorInput).place(x=230, y=100)


Funktioner = Label(master, text= 'Funktioner', width = 22, height = 2, bg = ColorInput).place(x=50, y=100)

Funktion1 = Button(master, text="Funktion1", width = 22, height = 2, bg = ColorInput).place(x=50, y=200)

Funktion2 = Button(master, text="Funktion2", width = 22, height = 2, bg = ColorInput).place(x=50, y=250)

Funktion3 = Button(master, text="Funktion3", width = 22, height = 2, bg = ColorInput).place(x=50, y=300)



def slut ():
    master.destroy()

SlutKnap = Button(master, text="End", width = 15, height = 2,command = slut, bg = ColorInput).place(x=185, y=400)

master.mainloop()
