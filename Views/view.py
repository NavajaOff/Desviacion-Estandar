import matplotlib.pyplot as plt
from colorama import Fore, Style, init
from Models.datos import DatosPO
from tabulate import tabulate

init(autoreset=True)

def mostrar_menu():
    print(Fore.MAGENTA + "\nCálculo de desviación estándar")
    print("1. Introducir números manualmente")
    print("2. Usar datos predefinidos (speed)")
    print("3. Mostrar historial de datos guardados")
    print("4. Eliminar historial")
    print("5. Salir")
    return input(Fore.CYAN + "Elige una opción (1-5): ")

def pedir_numeros():
    while True:
        entrada = input("Ingresa los números separados por coma (ejemplo: 10,20,30): ")
        try:
            numeros = [float(x.strip()) for x in entrada.split(",")]
            if len(numeros) == 0:
                print("Debes ingresar al menos un número.")
                continue
            return numeros
        except ValueError:
            print("Error. Asegúrate de ingresar solo números separados por coma.")

def mostrar_historial(historial):
    if not historial:
        print(Fore.YELLOW + "\nNo hay datos guardados.")
        return

    tabla = []
    for fila in historial:
        po = DatosPO(
            fila['id'],
            fila['datos'],
            fila['media'],
            fila['desviacion_estandar'],
            fila['cantidad'],
            fila['fecha']
        )
        tabla.append([
            po.id,
            po.datos,
            po.media,
            po.desviacion_estandar,
            po.cantidad,
            po.fecha
        ])
    print(Fore.CYAN + "\nHistorial de datos guardados:")
    print(Fore.GREEN + tabulate(
        tabla,
        headers=["ID", "Datos", "Media", "Desviación", "Cantidad", "Fecha"],
        tablefmt="grid"
    ))

def graficar_datos(datos, desviacion):
    import numpy as np
    plt.figure(figsize=(8, 4))
    plt.plot(datos, marker="o", label="Datos")
    plt.axhline(np.mean(datos), color="green", linestyle="--", label="Media")
    plt.title(f"Datos y desviación estándar: {desviacion:.2f}")
    plt.xlabel("Índice")
    plt.ylabel("Valor")
    plt.legend()
    plt.grid(True)
    plt.show()