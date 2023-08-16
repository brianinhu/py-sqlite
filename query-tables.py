import sqlite3

with sqlite3.connect("db_biblioteca.db") as cn:
    cursor = cn.cursor()
    cursor.execute("select * from autor")
    for autores in cursor.fetchall():
        print(autores)