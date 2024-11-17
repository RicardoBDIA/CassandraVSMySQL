import mysql.connector
import csv
from mysql.connector import Error

def insertar_datos():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='user',
            password='password'

        )
        if conn.is_connected():
            print("Conexion creada")
            cursor = conn.cursor()

            # Verificar si la base de datos existe, si no, crearla
            cursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
            print("Base de datos 'mydatabase' creada o ya existe")

            # Usar la base de datos
            cursor.execute("USE mydatabase")

            # Crear la tabla si no existe
# Crear tabla
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users(
                    name VARCHAR(50) NOT NULL,
                    email VARCHAR(50),
                    age INT
                )
            """)
            print("tabla users creados")
#borrar todos los registros de la tabla usuarios para que no hayan copias
            cursor.execute("DELETE FROM users")
            conn.commit()
            print("registros anteriores eliminados")
            #leer datos del archivo csv
            with open('data.csv', mode='r') as archivo_csv:
                df = csv.reader(archivo_csv)
                next(df)             
                #insertar los datos
                for fila in df:
                    cursor.execute("""
                        INSERT INTO users(name, email, age)
                        values(%s,%s,%s)
                    """,fila)
            #confirmar los cambios
            conn.commit()
            print("Se han insertado los registros en la base de datos")

    except Error as e:
        print("error al conectar a la base de datos o al insertar los datos", e)
        
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("conexion cerrada")

insertar_datos()
