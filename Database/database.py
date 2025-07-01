import mysql.connector
from mysql.connector import Error
from datetime import datetime

class Database:
    def __init__(self, host="localhost", user="root", password="", database="ds"):
        try:
            self.connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password
            )
            self.cursor = self.connection.cursor(dictionary=True)
            self.create_database(database)
            self.connection.database = database
            self.create_table()
        except Error as e:
            print(f"Error connecting to MySQL: {e}")

    def create_database(self, database):
        try:
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
        except Error as e:
            print(f"Error creating database: {e}")

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS datos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            datos VARCHAR(255) NOT NULL,
            media FLOAT,
            desviacion_estandar FLOAT,
            cantidad INT,
            fecha DATETIME
        );
        """
        self.cursor.execute(query)
        self.connection.commit()

    def guardar_datos(self, valores, media, desviacion):
        query = """
        INSERT INTO datos (datos, media, desviacion_estandar, cantidad, fecha)
        VALUES (%s, %s, %s, %s, %s);
        """
        fecha_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute(query, (
            ",".join(map(str, valores)),
            media,
            desviacion,
            len(valores),
            fecha_actual
        ))
        self.connection.commit()

    def obtener_todos(self):
        query = "SELECT * FROM datos;"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def cerrar(self):
        self.cursor.close()
        self.connection.close()