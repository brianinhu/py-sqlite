import sqlite3

# Read
with sqlite3.connect("db_biblioteca.db") as cn:
    cursor = cn.cursor()
    cursor.execute("select * from autor")
    for autores in cursor.fetchall():
        print(autores)

# Insert for table autor
with sqlite3.connect("db_biblioteca.db") as cn:
    cursor = cn.cursor()
    cursor.execute(
        "insert into autor(nombre, edad, idpais) values (?, ?, ?)",
        ("Jose Carlos Mariátegui", 65, 3)
    )

# Update for table autor
with sqlite3.connect("db_biblioteca.db") as cn:
    cursor = cn.cursor()
    cursor.execute("update autor set edad = 120 where idautor = 11")

# Delete for table autor
with sqlite3.connect("db_biblioteca.db") as cn:
    cursor = cn.cursor()
    cursor.execute("delete from autor where idautor = 11")