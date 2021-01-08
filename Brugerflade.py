import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import tkinter.ttk as ttk
from PIL import ImageTk, Image

class Application(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)

        self.pack()
        self.Login_Screen()

    def Login_Screen(self):
        # img = ImageTk.PhotoImage(Image.open("Other/martins-logo.png"))
        # canvas.create_image(20,20, anchor=NW, image=img)
        # img = ImageTk.PhotoImage(Image.open("Other/martins-logo.png"))
        # self.create_image(20,20, anchor=NW, image=self.img)
        # self.image = self.img

        # load = Image.open("Other/martins-logo.png")
        # render = ImageTk.PhotoImage(load)
        # img = Label(self, image=render)
        # img.image = render
        # img.place(x=0, y=0)

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
root.geometry("800x600")
app = Application(master=root)
app.master.title('Martin´s Supermarked')
app.mainloop()
