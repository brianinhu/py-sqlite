import sqlite3

# Creacion de las listas con los datos a insertar en cada tabla
l_pais = [
    ("Mexico",),
    ("Colombia",),
    ("Chile",),
    ("Perú",),
    ("Uruguay",)
]

l_autor = [
    ("Mario Vargas Llosa", 80, 1),
    ("Abraham Valdelomar", 65, 2),
    ("José María Arguedas", 70, 2),
    ("Ricardo Palma", 55, 4),
    ("César Vallejo", 65, 5),
    ("Alfredo Bryce Echenique", 90, 3),
    ("Clorinda Matto de Turner", 75, 1),
    ("José Santos Chocano", 82, 2),
    ("Julio Ramón Ribeyro", 102, 5),
    ("Oswaldo Reynoso", 90, 1),
]

l_libro = [
    ("Crimen y castigo", 25, 1),
    ("Orgullo y prejuicio", 30, 2),
    ("1984", 40, 3),
    ("Ulises", 20, 4),
    ("En busca del tiempo perdido", 15, 5),
    ("Matar a un ruiseñor", 10, 6),
    ("El Gran Gatsby", 30, 7),
    ("Cien años de soledad", 45, 1),
    ("La sombra del viento", 28, 2),
    ("Rayuela", 18, 3),
    ("Los detectives salvajes", 12, 4),
    ("Don Quijote de la Mancha", 38, 5),
    ("Ficciones", 23, 6),
    ("Pedro Páramo", 8, 7),
    ("La casa de los espíritus", 33, 8),
    ("Crónica de una muerte anunciada", 12, 9),
    ("La guerra y la paz", 4, 10),
    ("Cien años de soledad", 42, 1),
    ("La sombra del viento", 25, 2),
    ("Rayuela", 16, 3)
]

# Creacion de los scripts insert
in_pais = "INSERT INTO pais(pais) values (?)"
in_autor = "INSERT INTO autor(nombre, edad, idpais) values (?, ?, ?)"
in_libro = "INSERT INTO libro(libro, stock ,idautor) values (?, ?, ?)"

# Ejecutamos todo lo anterior con with
with sqlite3.connect("db_biblioteca.db") as cn:
    cursor = cn.cursor()
    cursor.executemany(in_pais, l_pais)
    cursor.executemany(in_autor, l_autor)
    cursor.executemany(in_libro, l_libro)