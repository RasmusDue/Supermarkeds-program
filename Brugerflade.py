import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import tkinter.ttk as ttk

class Book_gui(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)

        self.data = Books_data(False)
        self.kurv = self.data.create_new_transaction()

        self.build_GUI()

        self.opdater_transaktions_tabel()
        self.opdater_tabel()
