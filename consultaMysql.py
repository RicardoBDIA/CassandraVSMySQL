import pymysql
import time

# Conexión
conn = pymysql.connect(host="localhost", user="user", password="password", database="mydatabase")
cursor = conn.cursor()

# Consulta 1: Promedio de edades
start_time = time.time()
cursor.execute("SELECT AVG(age) FROM users")
avg_age = cursor.fetchone()[0]
end_time = time.time()
print(f"Promedio de edad en MySQL: {avg_age}")
print(f"Tiempo de consulta (promedio de edades): {end_time - start_time:.4f} segundos")

# Consulta 2: Nombres que empiezan con 'R'
start_time = time.time()
cursor.execute("SELECT COUNT(*) FROM users WHERE name LIKE 'R%'")
count_names_with_r = cursor.fetchone()[0]
end_time = time.time()
print(f"Cantidad de nombres que empiezan con 'R' en MySQL: {count_names_with_r}")
print(f"Tiempo de consulta (nombres con 'R'): {end_time - start_time:.4f} segundos")


cursor.close()
conn.close()