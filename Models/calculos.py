import numpy as np

def calcular_media(lista):
    return sum(lista) / len(lista)

def desviacion_estandar_manual(lista):
    """Calcula la desviación estándar de forma manual."""
    media = calcular_media(lista)
    suma_cuadrados = sum((x - media) ** 2 for x in lista)
    varianza = suma_cuadrados / len(lista)
    return varianza ** 0.5

def desviacion_estandar_numpy(lista):
    """Calcula la desviación estándar usando numpy."""
    return np.std(lista)