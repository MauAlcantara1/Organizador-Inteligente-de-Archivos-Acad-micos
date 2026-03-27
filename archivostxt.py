import os
import datetime

def iniciandoAnalisis():
    timestamp = os.path.getatime("alumnos")
    print("se encuentra en " + os.path.abspath("alumnos"))
    print("Iniciando analisis de archivo")
    print("Tamaño del archivo:", os.path.getsize("alumnos"))
    print("Último acceso:", datetime.datetime.fromtimestamp(timestamp))
    
alumnos_iniciales = {
    "Mariana": "10",
    "Alan": "9",
    "Martin": "11",
    "Bruno": "8"
}

with open("alumnos", "w") as alumnos:
    for nombre, calificacion in alumnos_iniciales.items():
        alumnos.write(nombre + "    " + calificacion + "\n")

if os.path.exists("alumnos"):
    print("El archivo se encuentra")
    iniciandoAnalisis()
else:
    print("El archivo no se encuentra")