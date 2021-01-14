import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import tkinter.ttk as ttk
from PIL import ImageTk, Image


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.status = 0

        self.img = ImageTk.PhotoImage(Image.open("Other/martins-logo.png"))


        self.build_GUI()

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
        #self.en_id.delete(0,"end")

    def program_screen(self):
        #tk.delete("all")
        #self.logo()
        print("_______jeg er ker i koden _____")
        print("Status: {}".format(self.status))
        lbl_test = tk.Label(text='Test1234')
        #pack(side="top")
        self.db_view = ttk.Treeview(XXXXX, column=("column1", "column2", "column3", "column4", "column5"), show='headings')
        self.db_view.bind("<ButtonRelease-1>", self.on_book_selected)
        self.db_view.heading("#1", text="Titel", command=self.sorterTitel)
        self.db_view.column("#1",minwidth=0,width=150, stretch=tk.NO)
        self.db_view.heading("#2", text="Forfatter", command=self.sorterForfatter)
        self.db_view.column("#2",minwidth=0,width=150, stretch=tk.NO)
        self.db_view.heading("#3", text="Årstal", command=self.sorterAarstal)
        self.db_view.column("#3",minwidth=0,width=80, stretch=tk.NO)
        self.db_view.heading("#4", text="Rating", command=self.sorterRating)
        self.db_view.column("#4",minwidth=0,width=80, stretch=tk.NO)
        self.db_view.heading("#5", text="id")

    def build_GUI(self):
        self.tabs = ttk.Notebook(self)
        bog_fane = ttk.Frame(self.tabs)

        self.tabs.add(bog_fane, text='Bøger')

        right_frame = ttk.Frame(bog_fane)
        top_frame = ttk.Frame(right_frame)
        data_frame = ttk.Frame(right_frame)
        knap_frame = ttk.Frame(bog_fane)


        self.edit_button = ttk.Button(knap_frame, text="Rediger bog")
        self.edit_button.pack(side=tk.TOP)

        self.del_button = ttk.Button(knap_frame, text="Slet bog")
        self.del_button.pack(side=tk.TOP)

        self.add_button = ttk.Button(knap_frame, text="Tilføj til kurv")
        self.add_button.pack(side=tk.TOP)

        self.buy_button = ttk.Button(knap_frame, text="Køb")
        self.buy_button.pack(side=tk.TOP)

        self.kurv_text = ScrolledText(knap_frame, state='disabled', width=20,height=5)
        self.kurv_text.pack(side=tk.TOP)
        self.kurv_text.configure(font='TkFixedFont')

        self.db_view = ttk.Treeview(data_frame, column=("column1", "column2", "column3", "column4", "column5"), show='headings')
        self.db_view.bind("<ButtonRelease-1>")
        self.db_view.heading("#1", text="Titel")
        self.db_view.column("#1",minwidth=0,width=150, stretch=tk.NO)
        self.db_view.heading("#2", text="Forfatter")
        self.db_view.column("#2",minwidth=0,width=150, stretch=tk.NO)
        self.db_view.heading("#3", text="Årstal")
        self.db_view.column("#3",minwidth=0,width=80, stretch=tk.NO)
        self.db_view.heading("#4", text="Rating")
        self.db_view.column("#4",minwidth=0,width=80, stretch=tk.NO)
        self.db_view.heading("#5", text="id")
        #Læg mærke til at kolonne 5 ikke bliver vist.
        #Vi kan stadig finde id på den bog der er valgt,
        #men brugeren kan ikke se id.
        self.db_view["displaycolumns"]=("column1", "column2", "column3", "column4")
        ysb = ttk.Scrollbar(data_frame, orient=tk.VERTICAL)
        self.db_view.configure(yscrollcommand=ysb.set)
        self.db_view.pack(side = tk.TOP, fill=tk.BOTH)

        #Top Frame
        self.can = tk.Canvas(top_frame, width=200, height=200)
        self.can.grid(column=1, row=0, rowspan=2)

        self.lbl_titel = ttk.Label(top_frame, text='Titel')
        self.lbl_forfatter = ttk.Label(top_frame, text='Forfatter')
        self.lbl_titel.grid(column=0, row=0)
        self.lbl_forfatter.grid(column=0, row=1)

        top_frame.pack(side=tk.TOP)
        data_frame.pack(side = tk.TOP)
        knap_frame.pack(side = tk.LEFT, fill=tk.Y)
        right_frame.pack(side=tk.RIGHT, fill=tk.Y)

        self.pack()







root = tk.Tk()
app = Application(root)
root.title('Martin´s Supermarked')
root.geometry("800x800")
root.mainloop()
