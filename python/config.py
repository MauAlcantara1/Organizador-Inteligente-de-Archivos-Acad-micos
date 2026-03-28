GRADOS = ["grado1", "grado2", "grado3"]
GRUPOS_ALUMNOS = ["grupoA", "grupoB"]
GRUPOS_IMG = ["grupoA", "grupoB", "grupoC"]

ESTRUCTURA = {
    "alumnos": {
        grado: GRUPOS_ALUMNOS for grado in GRADOS
    },
    "img": {
        "certificados": {grado: GRUPOS_IMG for grado in GRADOS},
        "colegiaturas": {grado: GRUPOS_IMG for grado in GRADOS},
    }
}

LOG_FILE = "log.txt"

EXTENSIONES_IMAGEN = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"}
EXTENSIONES_TEXTO = {".txt", ".csv", ".md"}