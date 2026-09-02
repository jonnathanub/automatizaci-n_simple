import re

from funciones_agente.obtener_precio_accion import obtener_precio_accion
from funciones_agente.obtener_clima import obtener_clima
from utils.sanitizar import sanitizar


def procesar_input(texto):
    texto = sanitizar(texto)

    if texto in ["salir", "exit", "quit", "adios"]:
        return "salir"

    if any(palabra in texto for palabra in [
        "accion",
        "acciones",
        "precio",
        "bolsa"
    ]):
        return "accion"

    if any(palabra in texto for palabra in [
        "clima",
        "temperatura",
        "tiempo"
    ]):
        return "clima"

    return "desconocido"


def main():
    print("======================================")
    print("       CHATBOT v1.0.0")
    print("======================================")
    print("Puedo ayudarte con:")
    print("- Precio de acciones")
    print("- Temperatura actual de una ciudad")
    print("Escribe 'salir' para terminar.")
    print()

    while True:
        try:
            texto = input(">>> ")

            intencion = procesar_input(texto)

            if intencion == "salir":
                print("¡Hasta luego!")
                break

            if intencion == "accion":
                resultado = obtener_precio_accion(None, texto)
                print(resultado)
                continue

            if intencion == "clima":
                resultado = obtener_clima(None, texto)
                print(resultado)
                continue

            print("No entendi la consulta. Prueba, por ejemplo:")
            print("- precio de Microsoft")
            print("- precio de Apple")
            print("- clima en Ciudad de Mexico")

        except KeyboardInterrupt:
            print("\n¡Hasta luego!")
            break

        except Exception as e:
            print(f"Ocurrio un error: {e}")


if __name__ == "__main__":
    main()
