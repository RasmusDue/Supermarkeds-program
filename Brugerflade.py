import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import tkinter.ttk as ttk
from PIL import ImageTk, Image

from Datalag import Data
#d = Data()

class Application(ttk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.img = ImageTk.PhotoImage(Image.open("Other/martins-logo.png"))
        self.data = Data()

        self.program_screen()

    def program_screen(self):
        self.Login_button = ttk.Button(self, text="Login", command= self.login_screen)
        self.Login_button.grid(column =0, row = 0)
        self.Funktion_1_button = ttk.Button(self, text="Funktion")
        self.Funktion_1_button.grid(column =0, row = 1)
        self.Funktion_2_button = ttk.Button(self, text="Funktion")
        self.Funktion_2_button.grid(column =0, row = 2)
        self.Funktion_3_button = ttk.Button(self, text="Funktion")
        self.Funktion_3_button.grid(column =0, row = 3)
        self.Vare_liste = tk.Listbox(self, width=40)
        self.Vare_liste.grid(column =1, row = 1)

        self.pack()

    def logo(self, frame, x, y):
        img = Image.open("Other/martins-logo.png")
        #img = img.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = tk.Label(frame, image=img)
        panel.image = img
        panel.grid(column =x, row = y)

    def login_screen(self):
        def user_login():
            bruger_id = self.en_id.get()
            password = self.en_kode.get()
            print("id: {}  pass: {}".format(bruger_id, password))
            print("Bruger login udført")
            print(self.data.tjek_password("Palle"))
            #rettighedder
            dlg.destroy()
            dlg.update()

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

        but_login = tk.Button(dlg, text="Login", command= user_login)
        but_login.grid(column =1, row =4)







root = tk.Tk()
root.geometry("800x800")
app = Application(root)
app.master.title('Martin´s Supermarked')
app.mainloop()
