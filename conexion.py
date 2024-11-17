import socket

def check_connection(host, port):
    try:
        with socket.create_connection((host, port), timeout=5):
            print(f"✅ Conexión exitosa con {host}:{port}")
            return True
    except Exception as e:
        print(f"❌ No se pudo conectar con {host}:{port} - {e}")
        return False

if __name__ == "__main__":
    # Configuración de los contenedores
    services = {
        "Cassandra": ("cassandra_container", 9042),
        "MySQL": ("mysql_container", 3306),
    }

    print("📡 Comprobando conexiones...")
    for service_name, (host, port) in services.items():
        print(f"🔍 Verificando {service_name}...")
        check_connection(host, port)
