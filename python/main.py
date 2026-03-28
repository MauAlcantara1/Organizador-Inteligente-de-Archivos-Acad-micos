import os
import shutil
import datetime
from organizar_archivos import crear_estructura, organizar_archivos
from analizar_archivos import analizar_archivo

def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Crear carpetas en orden o verificar existencia")
        print("2. Analizar archivos")
        print("3. Analizar alumnos")
        print("4. Ver logs")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            crear_estructura()
            organizar_archivos(".")
            archivo_ejemplo = os.path.join("alumnos", "grado1", "grupoA", "grupoA_grado1.txt")
            if os.path.exists(archivo_ejemplo):
                analizar_archivo(archivo_ejemplo)
            else:
                print(f"[INFO] Coloca archivos en el directorio para que sean organizados automáticamente.")
                print(f"       Ejemplo de nombre válido: 'certificado_grado2_grupoB_Mariana.jpg'\n")
        elif opcion == "2":
            analizar_archivo()
        elif opcion == "3":
            print("aun no disponible")
            #analizar_alumno()
        elif opcion == "4":
            print("aun no disponible")
            #verificar_historial()
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    print("\n╔══════════════════════════════════════════╗")
    print("║   GESTOR DE ARCHIVOS ACADÉMICOS  v1.0   ║")
    print("╚══════════════════════════════════════════╝\n")

    menu()
