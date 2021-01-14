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

        # c = self.con.cursor()
        # c.execute('INSERT INTO bruger_tabel (navn,password) VALUES (?,?)', ("Palle", "1234"))
        # self.con.commit()

    def tjek_password(self, bruger):
        c = self.con.cursor()
        c.execute('SELECT password FROM bruger_tabel WHERE bruger_tabel.navn = (?)', (bruger,))
        return c.fetchone()[0]
