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
        right_frame = ttk.Frame()

        self.Funktion_1_button = ttk.Button(right_frame,text="Funktion")
        self.Funktion_1_button.pack()

        # skal være der for at få det hele vist #

        right_frame.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.pack()



root = tk.Tk()
app = GUI(root)
root.title('Martin´s Supermarked')
root.geometry("800x600")
app.mainloop()
