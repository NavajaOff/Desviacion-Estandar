import matplotlib.pyplot as plt
from manual import desviacion_estandar_manual
from automatico import desviacion_estandar_numpy
from Database.database import Database

# Datos predefinidos
speed = [86, 87, 88, 86, 87, 85, 86]


def menu():
    print("Cálculo de desviación estándar")
    print("1. Introducir números manualmente")
    print("2. Usar datos predefinidos (speed)")
    opcion = input("Elige una opción (1 o 2): ")
    return opcion


def pedir_numeros():
    while True:
        entrada = input("Introduce los números separados por coma (ejemplo: 10,20,30): ")
        try:
            numeros = []
            for x in entrada.split(","):
                x = x.strip()
                numeros.append(float(x))
            if len(numeros) == 0:
                print("Debes ingresar al menos un número.")
                continue
            return numeros
        except ValueError:
            print("Entrada inválida. Asegúrate de ingresar solo números separados por coma.")


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


def main():
    db = Database()
    opcion = menu()
    if opcion == "1":
        datos = pedir_numeros()
    elif opcion == "2":
        datos = speed
        print("Usando datos predefinidos:", datos)
    else:
        print("Opción no válida.")
        db.cerrar()
        return

    desv_manual = desviacion_estandar_manual(datos)
    desv_numpy = desviacion_estandar_numpy(datos)
    media = sum(datos) / len(datos)

    print(f"Desviación estándar (manual): {desv_manual:.2f}")
    print(f"Desviación estándar (numpy): {desv_numpy:.2f}")

    # Guardar en la base de datos
    db.guardar_datos(datos, media, desv_numpy)

    graficar_datos(datos, desv_numpy)

    # Mostrar historial
    print("\nHistorial de datos guardados:")
    for fila in db.obtener_todos():
        print(f"ID: {fila['id']}, Datos: {fila['datos']}, Media: {fila['media']}, Desviación: {fila['desviacion_estandar']}, Cantidad: {fila['cantidad']}, Fecha: {fila['fecha']}")

    db.cerrar()


if __name__ == "__main__":
    main()

