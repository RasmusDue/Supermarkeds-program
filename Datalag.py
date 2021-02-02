import sqlite3
import datetime
datetime.date.fromisoformat('2019-12-04')
#Her oprettes en forbindelse til databasefilen
#Hvis filen ikke findes, vil sqlite oprette en ny tom database.
class Data:
    def __init__(self):
        self.con = sqlite3.connect('data_supermarked.db')
        print('Database åbnet i class')

    def create_data(self):
        # c = self.con.cursor()
        # c.execute('DROP TABLE kategorier')
        # self.con.commit()
        # print('table drop')
        try:
            self.con.execute("""CREATE TABLE bruger_tabel (
        		id INTEGER PRIMARY KEY AUTOINCREMENT,
        		navn STRING,
                password STRING)""")
            print('Tabel oprettet')
        except Exception as e:
            print('Tabellen findes allerede')

        try:
            self.con.execute("""CREATE TABLE vare_tabel (
        		id INTEGER PRIMARY KEY AUTOINCREMENT,
        		navn STRING,
                kobs_pris INTEGER,
                salgs_pris INTEGER,
                type STRING,
                lagerstatus INTEGER)""")
            print('Tabel oprettet')
        except Exception as e:
            print('Tabellen findes allerede')

        try:
            self.con.execute("""CREATE TABLE kategorier (
        		id INTEGER PRIMARY KEY AUTOINCREMENT,
        		kategori TEXT)""")
            print('Tabel oprettet')
        except Exception as e:
            print('Tabellen findes allerede')


        # c = self.con.cursor()
        # c.execute('INSERT INTO bruger_tabel (navn,password) VALUES (?,?)', ("Palle", "1234"))
        # self.con.commit()

    def tjek_password(self, bruger):
        c = self.con.cursor()
        c.execute('SELECT password FROM bruger_tabel WHERE bruger_tabel.navn = (?)', (bruger,))
        return c.fetchone()[0]

    def add_vare(self, navn, kobs_pris, salgs_pris, type, lagerstatus):
        c = self.con.cursor()
        c.execute('INSERT INTO vare_tabel (navn, kobs_pris, salgs_pris, type, lagerstatus) VALUES (?,?,?,?,?)', (navn, kobs_pris, salgs_pris, type, lagerstatus))
        self.con.commit()

    def slet_vare(self, navn):
        c = self.con.cursor()
        c.execute('DELETE FROM vare_tabel WHERE navn = ?', [navn])
        self.con.commit()

    def show_all_vare(self):
        list = []
        c = self.con.cursor()
        c.execute('SELECT * from vare_tabel')
        for x in c:
            list.append(x)
        return list

    def get_vare(self, id):
        c = self.con.cursor()

    def change_pris(self, id, pris):
        c = self.con.cursor()

    def add_katagori(self, navn):
        c = self.con.cursor()
        c.execute('INSERT INTO kategorier (kategori) VALUES (?)', (navn,))
        self.con.commit()

    def get_kategorier(self):
        list = []
        c = self.con.cursor()
        c.execute('SELECT * from kategorier')
        for x in c:
            list.append(x)
        return list

    def slet_kategori(self, k_navn):
        c = self.con.cursor()
        c.execute('DELETE FROM kategorier WHERE kategori = ?', [k_navn])
        self.con.commit()
