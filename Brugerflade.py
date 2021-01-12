import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import tkinter.ttk as ttk
from PIL import ImageTk, Image

from Datalag import Data

class Application(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.status = 0
        self.img = ImageTk.PhotoImage(Image.open("Other/martins-logo.png"))
        #self.data = Data()

        self.program_screen()

    def logo(self, frame, x, y):
        img = Image.open("Other/martins-logo.png")
        #img = img.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = tk.Label(frame, image=img)
        panel.image = img
        panel.grid(column =x, row = y)

    def login_screen(self):
        dlg = tk.Toplevel()
        dlg.geometry("250x250")
        dlg.title('Martin´s Login')
        self.logo(dlg, 1, 0)

        lbl_login = tk.Label(dlg, text='Login')
        lbl_login.grid(column =1, row = 1)

        lbl_id = tk.Label(dlg, text='Bruger id')
        lbl_id.grid(column =0, row = 2)
        self.en_id = tk.Entry(dlg)
        self.en_id.grid(column=1, row=2)

        lbl_kode = tk.Label(dlg, text='Password')
        lbl_kode.grid(column =0, row =3)
        self.en_kode = tk.Entry(dlg)
        self.en_kode.grid(column =1, row =3)

        but_login = tk.Button(dlg, text="Login", command=lambda: user_login())
        but_login.grid(column =1, row =4)

        def user_login():
            bruger_id = self.en_id.get()
            password = self.en_kode.get()
            print("id: {}  pass: {}".format(bruger_id, password))
            print("Bruger login udført")
            print("Status: {}".format(self.status))
            print("her er jeg")
            dlg.destroy()
            dlg.update()
            self.status = 1

    def program_screen(self):
        print("_______jeg er ker i koden _____")
        lbl_test = ttk.Label(self, text='Test1234')
        lbl_test.pack(side="top")
        but_login = tk.Button(self, text="Login", command=self.login_screen)
        but_login.pack(side="top")
        self.pack()


root = tk.Tk()
root.geometry("800x800")
app = Application(root)
app.master.title('Martin´s Supermarked')
app.mainloop()
