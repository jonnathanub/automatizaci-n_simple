import unicodedata


def sanitizar(texto):
    texto = texto.lower()

    # Eliminar tildes y diéresis
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(
        caracter
        for caracter in texto
        if unicodedata.category(caracter) != "Mn"
    )

    return texto.replace("ñ", "n")
