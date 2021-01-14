import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import tkinter.ttk as ttk
from PIL import ImageTk, Image


class GUI(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.img = ImageTk.PhotoImage(Image.open("Other/martins-logo.png"))

        self.build_GUI()



    def build_GUI(self):
        self.Funktion_1_button = ttk.Button(self,text="Funktion")
        self.Funktion_1_button.grid(column =1, row = 1)
        self.Funktion_2_button = ttk.Button(self,text="Funktion")
        self.Funktion_2_button.grid(column =1, row = 2)
        self.Funktion_3_button = ttk.Button(self,text="Funktion")
        self.Funktion_3_button.grid(column =1, row = 3)



root = tk.Tk()
app = GUI(root)
root.title('Martin´s Supermarked')
root.geometry("800x600")
root.mainloop()
