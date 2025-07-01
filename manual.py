def desviacion_estandar_manual(lista):
    """Calcula la desviación estándar de forma manual."""
    media = sum(lista) / len(lista)
    suma_cuadrados = sum((x - media) ** 2 for x in lista)
    varianza = suma_cuadrados / len(lista)
    return varianza ** 0.5