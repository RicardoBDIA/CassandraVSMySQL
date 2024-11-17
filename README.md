---

Contenido del README

# Comparación de Rendimiento entre MySQL y Cassandra

Este proyecto tiene como objetivo comparar el rendimiento de las operaciones de agregación entre una base de datos relacional (MySQL) y una base de datos NoSQL (Cassandra). A través de este análisis, mediremos el tiempo de ejecución de consultas que calculan la media de edades almacenadas en ambas bases de datos.

## Tabla de Contenidos

- [Requisitos](#requisitos)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Instrucciones para Ejecutar](#instrucciones-para-ejecutar)
- [Resultados](#resultados)
- [Conclusiones](#conclusiones)

* Requisitos

## Para ejecutar este proyecto, necesitarás tener instalados los siguientes componentes:

- Python 3.x
- MySQL Server
- Apache Cassandra
- Docker (opcional, para contenedores)
- Bibliotecas de Python:
  - `mysql-connector-python`
  - `cassandra-driver`
  - `pandas`
  - `matplotlib`

## Puedes instalar las bibliotecas necesarias usando:

pip install mysql-connector-python cassandra-driver pandas matplotlib

## El proyecto está organizado de la siguiente manera:

/CassandraVSMySQL
│
├── docker-compose.yml # Define los contenedores de MySQL y Cassandra con sus respectivas configuraciones.
├── dataset.py # Script que genera un archivo CSV con datos simulados.
├── cargaDatosCassandra.py # Script para cargar datos en Cassandra
├── cargaDatosMysql.py # Script para cargar datos en Mysql
├── consultaCassandra.py # script para consultas tanto en MySQL como en Cassandra
├── consultaMysql.py # script para consultas tanto en MySQL como en Cassandra
├── colab_notebook.ipynb # notebook para visualizar los resultados
└── README.md # Este archivo contiene requisitos, estructura del proyecto, instrucciones para ejecutar, resultados y conclusiones

## Instrucciones para Ejecutar

## Paso 1: Ejecutar MySQL y Cassandra.

	*Abre una terminal y navega hasta el directorio donde guardaste el archivo docker-compose.yml, luego ejecuta:

	docker-compose up -d

## Paso 2: Ejecutar dataset.py para generar el archivo CSV

	python3 dataset.py

## Paso 3: Carga de datos, ejecuta los dos archivos.py de carga de datos

	python3 script_load_cassandra
	python3 script_load_mysql

## Paso 3: Ejecuta el script de consultas.

	python script_consultas.py

## Paso 4: Visualización de los resultados en Google Colab.

   	*Crear un Notebook en Colab
   	*Abre Google Colab y crea un nuevo notebook.
    	*Sube el archivo script_consultas.py al entorno de Colab. (Puedes abrir el archivo .ipynb directamente) y ejecuta las celdas.

Resultados
Los resultados mostrarán la edad promedio y el tiempo de ejecución de las consultas para ambas bases de datos.

Conclusiones
Este proyecto proporciona una comparación básica entre MySQL y Cassandra en cuanto a rendimiento en operaciones de agregación. Los resultados pueden variar dependiendo de la configuración del entorno y del tamaño de los datos.

En general, Cassandra puede ofrecer un mejor rendimiento para operaciones de escritura y consultas sobre grandes volúmenes de datos, mientras que MySQL es más eficiente para operaciones transaccionales y consultas complejas.
