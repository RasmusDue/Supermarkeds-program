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
        # c = con.cursor()
        # c.execute('DROP TABLE bruger_tabel')
        # con.commit()
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

    def show_all_vare(self):
        list = []
        c = self.con.cursor()
        c.execute('SELECT * from vare_tabel')
        for x in c:
            list.append(x[1],x[2],x[3],x[4],x[5])
        return l
