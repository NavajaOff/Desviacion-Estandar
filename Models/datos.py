class DatosPO:
    def __init__(self, id, datos, media, desviacion_estandar, cantidad, fecha):
        self.id = id
        self.datos = [float(x) for x in datos.split(",")]
        self.media = media
        self.desviacion_estandar = desviacion_estandar
        self.cantidad = cantidad
        self.fecha = fecha