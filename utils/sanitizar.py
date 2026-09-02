import unicodedata


def sanitizar(texto):
    texto = texto.lower().strip()

    # Eliminar tildes y dieresis
    texto = unicodedata.normalize("NFD", texto)

    texto = "".join(
        caracter
        for caracter in texto
        if unicodedata.category(caracter) != "Mn"
    )

    return texto
