from organizar_archivos import organizar_archivos
from analizar_archivos import analizar_archivos
from analizar_alumnos import analizar_alumnos
from historial import ver_logs

print("=== SISTEMA DE ORGANIZACIÓN ACADÉMICA ===")

def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Analizar archivos")
        print("2. Analizar alumnos")
        print("3. Ver logs")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            analizar_archivos()
        elif opcion == "2":
            analizar_alumnos()
        elif opcion == "3":
            ver_logs()
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción no válida")


def main():
    print("Iniciando sistema...\n")

    organizar_archivos()
    analizar_archivos()

    menu()


if __name__ == "__main__":
    main()