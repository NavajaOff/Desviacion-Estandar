# desviación estándar
import numpy as np

def desviacion_estandar_numpy(lista):
    """Calcula la desviación estándar usando numpy."""
    return np.std(lista)

speed = [86,87,88,86,87,85,86]

x = desviacion_estandar_numpy(speed)

print(x)

