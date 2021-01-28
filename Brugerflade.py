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
        #self.data.create_data()

        # Create left and right frames
        left_frame = tk.Frame(self, width=200, height= 400, bg='grey')

        left_frame.grid(row=0, column=0, padx=10, pady=5)

        right_frame = tk.Frame(self, width=650, height=400, bg='grey')
        right_frame.grid(row=0, column=1, padx=10, pady=5)

        #left_frame <---
        self.logo(left_frame,0,0)
        self.Login_button = ttk.Button(left_frame,text="Login", command= self.login_screen)
        self.Login_button.grid(column =0, row = 1, sticky='nesw')
        self.Add_vare_button = ttk.Button(left_frame, text="Tilføj vare", command= self.add_vare)
        self.Add_vare_button.grid(column =0, row = 2,sticky='nesw')
        self.Udsalg_button = ttk.Button(left_frame, text="Udsalg", command= self.udsalg)
        self.Udsalg_button.grid(column =0, row = 3, sticky='nesw')
        self.Kategorier = ttk.Button(left_frame, text="Kategorier", command= self.katagorier)
        self.Kategorier.grid(column =0, row = 4, sticky='nesw')

        #right_frame --->
        self.Vare_liste = ttk.Treeview(right_frame, column=("column1", "column2", "column3", "column4", "column5", "column6"), show='headings')
        self.Vare_liste.bind("<ButtonRelease-1>")
        self.Vare_liste.heading("#1", text="Navn")
        self.Vare_liste.column("#1",minwidth=0,width=100, stretch=tk.NO)
        self.Vare_liste.heading("#2", text="Købs pris")
        self.Vare_liste.column("#2",minwidth=0,width=100, stretch=tk.NO)
        self.Vare_liste.heading("#3", text="salgs_pris")
        self.Vare_liste.column("#3",minwidth=0,width=100, stretch=tk.NO)
        self.Vare_liste.heading("#4", text="Type")
        self.Vare_liste.column("#4",minwidth=0,width=100, stretch=tk.NO)
        self.Vare_liste.heading("#5", text="Lagerstatus")
        self.Vare_liste.column("#5",minwidth=0,width=100, stretch=tk.NO)
        self.Vare_liste.heading("#6", text="id")
        self.Vare_liste.column("#6",minwidth=0,width=100, stretch=tk.NO)

        self.Vare_liste["displaycolumns"]=("column1", "column2", "column3", "column4", "column5")
        ysb = ttk.Scrollbar(right_frame, command=self.Vare_liste.yview, orient=tk.VERTICAL)
        self.Vare_liste.configure(yscrollcommand=ysb.set)
        self.Vare_liste.grid(column = 1, row = 0)

        self.vis_vare()
        # skal være der for at få det hele vist #
        self.pack()

    def vis_vare(self):
        self.Vare_liste.delete(*self.Vare_liste.get_children())
        for x in self.data.show_all_vare():
            self.Vare_liste.insert("", tk.END, values=(x[1], x[2], x[3], x[4], x[5], x[0]))

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
            print(self.data.tjek_password(bruger_id))

            if password == self.data.tjek_password(bruger_id):
                print("Bruger login udført")
                dlg.destroy()
                dlg.update()
            else:
                print("forkert login")

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

    def add_vare(self):
        def add_data():
            self.data.add_vare(self.en_navn.get(), self.en_pris.get(), self.en_sell_pris.get(), self.en_type.get(), self.en_lagerstatus.get())
            close()
            self.vis_vare()

        dlg1 = tk.Toplevel()
        dlg1.geometry("250x250")
        dlg1.title("Tilføj vare")
        self.logo(dlg1, 1, 0)

        self.lbl_navn = ttk.Label(dlg1, text='Navn')
        self.lbl_navn.grid(column =0, row = 1)
        self.en_navn = ttk.Entry(dlg1)
        self.en_navn.grid(column=1, row=1)

        self.lbl_pris = ttk.Label(dlg1, text='Købs pris')
        self.lbl_pris.grid(column =0, row = 2)
        self.en_pris = ttk.Entry(dlg1)
        self.en_pris.grid(column=1, row=2)

        self.lbl_pris = ttk.Label(dlg1, text='Salgs pris')
        self.lbl_pris.grid(column =0, row = 3)
        self.en_sell_pris = ttk.Entry(dlg1)
        self.en_sell_pris.grid(column=1, row=3)

        self.lbl_type = ttk.Label(dlg1, text='Type')
        self.lbl_type.grid(column =0, row = 4)
        self.en_type = ttk.Entry(dlg1)
        self.en_type.grid(column=1, row=4)

        self.lbl_lagerstatus = ttk.Label(dlg1, text='Lagerstatus')
        self.lbl_lagerstatus.grid(column =0, row = 5)
        self.en_lagerstatus = ttk.Entry(dlg1)
        self.en_lagerstatus.grid(column=1, row=5)

        def close():
            dlg1.destroy()
            dlg1.update()

        self.but_annuller = ttk.Button(dlg1, text="Annuller", command=close)
        self.but_annuller.grid(column=1,row=6)
        self.but_ok = ttk.Button(dlg1, text="Tilføj vare", command= add_data)
        self.but_ok.grid(column=0,row=6)

    def katagorier(self):
        def add_kategori():
            if len(self.en_kategori.get())>=1:
                print("Klik")
                self.data.add_katagori(self.en_kategori.get())
                close()

        def close():
            dlg.destroy()
            dlg.update()

        def slet_kategori():


            curItem = self.Kategorier_liste.item(self.Kategorier_liste.focus())['values']
            if len(curItem) > 0:
                print(curItem)
                self.data.slet_kategori(curItem[0])
                close()

        dlg = tk.Toplevel()
        #dlg.geometry("250x250")
        dlg.title("Katagorier")
        self.logo(dlg, 0, 0)
        # self.lbl_dine_kategorier = ttk.Label(dlg, text='Dine kategorier:')
        # self.lbl_dine_kategorier.grid(column =0, row = 1)

        self.Kategorier_liste = ttk.Treeview(dlg, column=("column1"), show='headings')
        self.Kategorier_liste.bind("<ButtonRelease-1>")
        self.Kategorier_liste.heading("#1", text="Kategorier")
        self.Kategorier_liste.column("#1",minwidth=0,width=100, stretch=tk.NO)

        self.Kategorier_liste["displaycolumns"]=("column1")
        ysb = ttk.Scrollbar(dlg, command=self.Kategorier_liste.yview, orient=tk.VERTICAL)
        self.Kategorier_liste.configure(yscrollcommand=ysb.set)
        self.Kategorier_liste.grid(column = 1, row = 0)

        for x in self.data.get_kategorier():
            self.Kategorier_liste.insert("", tk.END, values=(x[1]))

        self.lbl_kategori = ttk.Label(dlg, text='Indtast Kategori')
        self.lbl_kategori.grid(column =0, row = 1)
        self.en_kategori = ttk.Entry(dlg)
        self.en_kategori.grid(column=1, row=1)

        self.but_annuller = ttk.Button(dlg, text="Annuller", command=close)
        self.but_annuller.grid(column=0,row=2)
        self.but_ok = ttk.Button(dlg, text="Tilføj kategori", command= add_kategori)
        self.but_ok.grid(column=1,row=2)



        self.but_slet = ttk.Button(dlg, text="Slet kategori", command= slet_kategori)
        self.but_slet.grid(column=1,row=3)



    def udsalg(self):
        def add_udsalg():
            self.vis_vare()
            dlg.destroy()
            dlg.update()

        def close():
            dlg.destroy()
            dlg.update()

        curItem = self.Vare_liste.item(self.Vare_liste.focus())['values']

        if len(curItem) > 0:

            dlg = tk.Toplevel()
            dlg.geometry("500x300")
            dlg.title("Udsalgs_vare")
            # Create left and right frames
            left_frame = tk.Frame(dlg, width=100, height= 400, bg='grey')
            left_frame.grid(row=0, column=0, padx=10, pady=5)
            right_frame = tk.Frame(dlg, width=150, height=400, bg='grey')
            right_frame.grid(row=0, column=1, padx=10, pady=5)
            self.logo(left_frame, 0, 0)

            self.lbl_udsalgs_pris = ttk.Label(left_frame, text='Udsalgs pris')
            self.lbl_udsalgs_pris.grid(column =0, row = 1,sticky='nesw')
            self.en_udsalgs_pris = ttk.Entry(left_frame)
            self.en_udsalgs_pris.grid(column=0, row=2,sticky='nesw')
            self.but_annuller = ttk.Button(right_frame, text="Annuller", command=close)
            self.but_annuller.grid(column=1,row=2,sticky='nesw')
            self.but_ok = ttk.Button(left_frame, text="Opret udsalg", command= add_udsalg)
            self.but_ok.grid(column=0,row=6,sticky='nesw')

            # tabel
            self.udsalg_liste = ttk.Treeview(right_frame, column=("column1", "column2", "column3", "column4", "column5", "column6"), show='headings')
            self.udsalg_liste.bind("<ButtonRelease-1>")
            self.udsalg_liste.heading("#1", text="Navn")
            self.udsalg_liste.column("#1",minwidth=0,width=100, stretch=tk.NO)
            self.udsalg_liste.heading("#2", text="Normal pris")
            self.udsalg_liste.column("#2",minwidth=0,width=100, stretch=tk.NO)
            self.udsalg_liste.heading("#3", text="Udsalgs_pris")
            self.udsalg_liste.column("#3",minwidth=0,width=100, stretch=tk.NO)
            self.udsalg_liste.heading("#4", text="Type")
            self.udsalg_liste.column("#4",minwidth=0,width=100, stretch=tk.NO)
            self.udsalg_liste.heading("#5", text="Lagerstatus")
            self.udsalg_liste.column("#5",minwidth=0,width=100, stretch=tk.NO)
            self.udsalg_liste.heading("#6", text="id")
            self.udsalg_liste.column("#6",minwidth=0,width=100, stretch=tk.NO)

            self.udsalg_liste["displaycolumns"]=("column1","column3")
            ysb = ttk.Scrollbar(right_frame, command=self.udsalg_liste.yview, orient=tk.VERTICAL)
            self.udsalg_liste.configure(yscrollcommand=ysb.set)
            self.udsalg_liste.grid(column = 1, row = 0)


root = tk.Tk()
root.geometry("900x600")
app = Application(root)
app.master.title('Martin´s Supermarked')
app.mainloop()
