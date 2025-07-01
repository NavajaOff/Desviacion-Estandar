from Database.database import Database
from Database.datos_dao import DatosDAO
from Models.calculos import calcular_media, desviacion_estandar_manual, desviacion_estandar_numpy
from Views.view import mostrar_menu, pedir_numeros, mostrar_historial, graficar_datos

speed = [86, 87, 88, 86, 87, 85, 86]

def run():
    db = Database()
    dao = DatosDAO(db)
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            datos = pedir_numeros()
            media = calcular_media(datos)
            desv_manual = desviacion_estandar_manual(datos)
            desv_numpy = desviacion_estandar_numpy(datos)
            print(f"Desviación estándar (manual): {desv_manual:.2f}")
            print(f"Desviación estándar (numpy): {desv_numpy:.2f}")
            dao.guardar_datos(datos, media, desv_numpy)
            graficar_datos(datos, desv_numpy)
        elif opcion == "2":
            datos = speed
            print("Usando datos predefinidos:", datos)
            media = calcular_media(datos)
            desv_manual = desviacion_estandar_manual(datos)
            desv_numpy = desviacion_estandar_numpy(datos)
            print(f"Desviación estándar (manual): {desv_manual:.2f}")
            print(f"Desviación estándar (numpy): {desv_numpy:.2f}")
            dao.guardar_datos(datos, media, desv_numpy)
            graficar_datos(datos, desv_numpy)
        elif opcion == "3":
            mostrar_historial(dao.obtener_todos())
        elif opcion == "4":
            print("¡Gracias por usar el sistema!")
            db.close()
            break
        else:
            print("Opción no válida.")