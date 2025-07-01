import mysql.connector
from mysql.connector import Error

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

    def close(self):
        self.cursor.close()
        self.connection.close()