import psycopg2

try:
    connection = psycopg2.connect(
        host='Localhost',
        user='postgres',
        password='',
        database='prueba',
        port='5432'
        
    )
    print("Conexión correcta")

    #Usar cursor

    cursor = connection.cursor ()

    #Crear nueva tabla
    #cursor.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

    #Esto hace la ejecución persistente, si no se borra al cerrar la conexión.
    connection.commit()
    
    #Listar tablas
    cursor.execute("""SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'public'""")



    #Listar tablas
    for table in cursor.fetchall():
        print(table)

    cursor.close()
    connection.close()

except Exception as e:
    print(e)