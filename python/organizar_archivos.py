import os
import shutil

from config import ESTRUCTURA, LOG_FILE, EXTENSIONES_IMAGEN, EXTENSIONES_TEXTO
from utils import extraer_contexto
from historial import registrar_log
def crear_estructura():
    """
    Verifica si los directorios existen y los crea si no.
    Estructura:
        alumnos/grado1/grupoA  ...grupoB
        alumnos/grado2/grupoA  ...grupoB
        alumnos/grado3/grupoA  ...grupoB
        img/certificados/grado1/grupoA ...grupoB ...grupoC
        img/colegiaturas/grado1/grupoA ...grupoB ...grupoC
    """
    registrar_log("Iniciando verificación/creación de estructura de directorios...")

    for grado, grupos in ESTRUCTURA["alumnos"].items():
        for grupo in grupos:
            ruta = os.path.join("alumnos", grado, grupo)
            if not os.path.exists(ruta):
                os.makedirs(ruta)
                registrar_log(f"Directorio creado: {ruta}")
            else:
                registrar_log(f"Directorio ya existe: {ruta}")

    for categoria, grados in ESTRUCTURA["img"].items():
        for grado, grupos in grados.items():
            for grupo in grupos:
                ruta = os.path.join("img", categoria, grado, grupo)
                if not os.path.exists(ruta):
                    os.makedirs(ruta)
                    registrar_log(f"Directorio creado: {ruta}")
                else:
                    registrar_log(f"Directorio ya existe: {ruta}")

    registrar_log("Estructura de directorios lista.\n")


def organizar_archivos(directorio_origen: str = "."):
    """
    Escanea el directorio origen y mueve cada archivo a su destino correcto.
    Omite directorios, log.txt y main.py.
    """
    registrar_log(f"Iniciando organización de archivos en: {os.path.abspath(directorio_origen)}")
    archivos = [
        f for f in os.listdir(directorio_origen)
        if os.path.isfile(os.path.join(directorio_origen, f))
        and f not in (LOG_FILE, "main.py")
    ]

    if not archivos:
        registrar_log("No se encontraron archivos para organizar.")
        return

    for archivo in archivos:
        origen = os.path.join(directorio_origen, archivo)
        destino_dir = determinar_destino(archivo)

        if destino_dir:
            os.makedirs(destino_dir, exist_ok=True)
            destino = os.path.join(destino_dir, archivo)
            shutil.move(origen, destino)
            registrar_log(f"Archivo movido: {archivo} → {destino_dir}/")
        else:
            registrar_log(f"[OMITIDO] No se pudo determinar destino para: {archivo}")

    registrar_log("Organización completada.\n")

def determinar_destino(nombre_archivo: str) -> str | None:
    """
    Decide la ruta destino basándose en:
    1. Extensión del archivo
    2. Palabras clave en el nombre (grado, grupo, categoría)
    """
    _, ext = os.path.splitext(nombre_archivo)
    ext = ext.lower()
    contexto = extraer_contexto(nombre_archivo)

    grado = contexto["grado"]
    grupo = contexto["grupo"]
    categoria = contexto["categoria"]

    if ext in EXTENSIONES_IMAGEN and categoria and grado and grupo:
        return os.path.join("img", categoria, grado, grupo)

    if ext in EXTENSIONES_IMAGEN and grado and grupo:
        return os.path.join("img", "certificados", grado, grupo)

    if ext in EXTENSIONES_TEXTO and grado and grupo:
        return os.path.join("alumnos", grado, grupo)

    return None
