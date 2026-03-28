import datetime

LOG_FILE = "log.txt"

def registrar_log(mensaje: str):
    """Escribe una entrada en log.txt con timestamp."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entrada = f"[{timestamp}] {mensaje}\n"
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(entrada)
    print(entrada.strip())