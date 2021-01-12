import sqlite3

class Data():
    def init(reset):
    con = sqlite3.connect('database.db')
    if reset:
        con.execute("DROP TABLE products")

############### Products ###############
    try:
        con.execute("""CREATE TABLE products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            price FLOAT,
            purchase_price FLOAT,
            ammount_off FLOAT,
            stock INTEGER,
            bar_code INTEGER,
            category STRING,
            name STRING)""")
        con.commit()
        print('Sucessfully created products database')
    except Exception as e:
        if str(e) == "table products already exists":
            pass
        else:
            print(f"ERROR : {e}")
