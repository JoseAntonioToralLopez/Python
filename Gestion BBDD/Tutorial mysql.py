import mysql.connector

# ¿Cómo conectar a una base de datos?
connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    port = '3306',
    database = ''
)

# ¿Cómo crear una base de datos?
cursor = connection.cursor()

cursor.execute("SHOW DATABASES")

for db in cursor:
    print(db)

# No olvidar cerrar la BBDD.
connection.close()