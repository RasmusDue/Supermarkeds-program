import tkinter as tk
from tkinter.scrolledtext import ScrolledText
# import tkinter.ttk as ttk
from PIL import ImageTk, Image

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.status = 0

        self.img = ImageTk.PhotoImage(Image.open("Other/martins-logo.png"))

        if self.status == 0:
            self.login_screen()
        elif self.status == 1:
            self.program_screen()

    def refresh(self):
        self.destroy()
        self.update()

    def logo(self):
        img = Image.open("Other/martins-logo.png")
        #img = img.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = tk.Label(root, image=img)
        panel.image = img
        panel.grid(column =1, row = 0)

    def login_screen(self):
        self.logo()

        lbl_login = tk.Label(text='Login')
        lbl_login.grid(column =1, row = 1)

        lbl_id = tk.Label(text='Bruger id')
        lbl_id.grid(column =1, row = 2)
        self.en_id = tk.Entry()
        self.en_id.grid(column=1, row=2)

        lbl_kode = tk.Label(text='Password')
        lbl_kode.grid(column =0, row =3)
        self.en_kode = tk.Entry()
        self.en_kode.grid(column =1, row =3)

        but_login = tk.Button(text="Login", command=lambda: self.user_login())
        but_login.grid(column =1, row =4)
        print("Status: {}".format(self.status))

    def user_login(self):
        bruger_id = self.en_id.get()
        password = self.en_kode.get()
        print("id: {}  pass: {}".format(bruger_id, password))
        print("Bruger login udført")
        self.status = 1
        print("Status: {}".format(self.status))
        print("her er jeg")
        self.refresh()
        self.en_id.delete(0,"end")

    def program_screen(self):
        tk.delete("all")
        #self.logo()
        print("_______jeg er ker i koden _____")
        print("Status: {}".format(self.status))
        lbl_test = tk.Label(text='Test1234')
        #pack(side="top")





root = tk.Tk()
app = Application(root)
root.title('Martin´s Supermarked')
root.geometry("800x800")
root.mainloop()
