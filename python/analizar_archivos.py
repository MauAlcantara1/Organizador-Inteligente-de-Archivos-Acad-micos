import datetime
import os
import historial as registrar_log

def analizar_archivo(ruta_archivo: str):
    """Muestra metadatos de un archivo: tamaño, fechas y ruta absoluta."""
    if not os.path.exists(ruta_archivo):
        print(f"[ERROR] El archivo '{ruta_archivo}' no existe.")
        return

    nombre = os.path.basename(ruta_archivo)
    tamanio = os.path.getsize(ruta_archivo)
    ultimo_acceso = datetime.datetime.fromtimestamp(os.path.getatime(ruta_archivo))
    ultima_modificacion = datetime.datetime.fromtimestamp(os.path.getmtime(ruta_archivo))
    ruta_abs = os.path.abspath(ruta_archivo)

    print("\n" + "=" * 45)
    print(f"  ANÁLISIS DE ARCHIVO: {nombre}")
    print("=" * 45)
    print(f"  Ruta absoluta      : {ruta_abs}")
    print(f"  Tamaño             : {tamanio} bytes")
    print(f"  Último acceso      : {ultimo_acceso.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  Última modificación: {ultima_modificacion.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 45 + "\n")

    registrar_log(f"Análisis realizado sobre: {ruta_abs} ({tamanio} bytes)")



