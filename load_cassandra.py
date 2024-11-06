from cassandra.cluster import Cluster
import csv

cluster = Cluster(["localhost"])
session = cluster.connect()

# Crear keyspace y tabla
session.execute("""
    CREATE KEYSPACE IF NOT EXISTS my_database
    WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };
""")
session.execute("USE my_database")
session.execute("""
    CREATE TABLE IF NOT EXISTS users (
        name TEXT,
        email TEXT PRIMARY KEY,
        age INT
    );
""")

# Insertar los datos desde el archivo CSV
with open("data/data.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        session.execute("""
            INSERT INTO users (name, email, age) VALUES (%s, %s, %s)
        """, (row["name"], row["email"], int(row["age"])))
cluster.shutdown()
