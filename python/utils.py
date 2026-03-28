from config import GRADOS

def extraer_contexto(nombre_archivo: str) -> dict:
    nombre = nombre_archivo.lower()
    contexto = {"grado": None, "grupo": None, "categoria": None}

    for g in GRADOS:
        if g in nombre:
            contexto["grado"] = g
            break

    for gr in ["grupoa", "grupob", "grupoc"]:
        if gr in nombre:
            contexto["grupo"] = gr[:5] + gr[5].upper()
            break

    if "certificado" in nombre:
        contexto["categoria"] = "certificados"
    elif "colegiatura" in nombre:
        contexto["categoria"] = "colegiaturas"

    return contexto