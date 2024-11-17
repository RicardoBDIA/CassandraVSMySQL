from cassandra.cluster import Cluster
import time

# Conexión
cluster = Cluster(["localhost"])
session = cluster.connect()
session.set_keyspace("my_database")

# Consulta 1: Promedio de edades
start_time = time.time()
rows = session.execute("SELECT age FROM users")
ages = [row.age for row in rows]
avg_age = sum(ages) / len(ages)
end_time = time.time()
print(f"Promedio de edad en Cassandra: {avg_age}")
print(f"Tiempo de consulta (promedio de edades): {end_time - start_time:.4f} segundos")

# Consulta 2: Nombres que empiezan con 'R'
start_time = time.time()
rows = session.execute("SELECT name FROM users")
count_names_with_r = sum(1 for row in rows if row.name.startswith('R'))
end_time = time.time()
print(f"Cantidad de nombres que empiezan con 'R' en Cassandra: {count_names_with_r}")
print(f"Tiempo de consulta (nombres con 'R'): {end_time - start_time:.4f} segundos")
