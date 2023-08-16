import sqlite3

# Creacion de las tablas
t_pais = """CREATE TABLE pais (
idpais INTEGER PRIMARY KEY AUTOINCREMENT,
pais VARCHAR(40) NOT NULL
)"""

t_autor = """CREATE TABLE autor (
idautor INTEGER PRIMARY KEY AUTOINCREMENT,
nombre VARCHAR(40) NOT NULL,
edad INTEGER,
idpais INTEGER REFERENCES pais
)"""

t_libro = """CREATE TABLE libro (
idlibro INTEGER PRIMARY KEY AUTOINCREMENT,
libro VARCHAR(120) NOT NULL,
stock INTEGER,
idautor INTEGER REFERENCES autor
)"""

# Compromete los cambios y cierra la conexion automáticamente
with sqlite3.connect("db_biblioteca.db") as cn:
    cursor = cn.cursor()
    cursor.execute(t_pais)
    cursor.execute(t_autor)
    cursor.execute(t_libro)
