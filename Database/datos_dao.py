from datetime import datetime

class DatosDAO:
    def __init__(self, db):
        self.db = db

    def guardar_datos(self, valores, media, desviacion):
        query = """
        INSERT INTO datos (datos, media, desviacion_estandar, cantidad, fecha)
        VALUES (%s, %s, %s, %s, %s);
        """
        fecha_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.db.cursor.execute(query, (
            ",".join(map(str, valores)),
            media,
            desviacion,
            len(valores),
            fecha_actual
        ))
        self.db.connection.commit()

    def obtener_todos(self):
        query = "SELECT * FROM datos;"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()

    def eliminar_historial(self):
        query = "DELETE FROM datos;"
        self.db.cursor.execute(query)
        self.db.connection.commit()