```python
import re

# Importamos las funciones de lógica de negocio
from funciones_agente.obtener_precio_accion import obtener_precio_accion
from funciones_agente.obtener_clima import obtener_clima

# Importamos la utilidad para limpiar el texto
from utils.sanitizar import sanitizar


def chatbot():
    """
    Función principal que inicia el chatbot interactivo por consola.
    Recibe el texto del usuario y determina qué acción realizar.
    """

    print("*** Chatbot v1.0.0 ***")
    print(
        "Hola, soy el Chatbot v1.0.0. Puedo ayudarte a obtener precios "
        "de acciones o indicarte la temperatura actual en cualquier ciudad del mundo."
    )
    print(
        "Me puedes hacer preguntas como:"
    )
    print("¿Cuál es el precio de una acción de Microsoft?")
    print("¿Cuál es la temperatura actual en la Ciudad de México?")
    print("Escribe 'salir' para terminar.\n")

    # Ciclo principal del chatbot
    while True:
        try:
            # Obtener el texto del usuario
            user_input = input("---> ").strip()

            # Si no escribió nada, volvemos a preguntar
            if not user_input:
                continue

            # Limpiar texto
            texto_limpio = sanitizar(user_input)

            # Comprobar si el usuario quiere salir
            if texto_limpio in ["salir", "exit", "quit", "adios"]:
                print(">>> ¡Hasta luego!")
                break

            # -----------------------------------------
            # REGLAS PARA DETECTAR PRECIO DE ACCIONES
            # -----------------------------------------
            stock_match = re.search(
                r"(?:precio|stock|accion|valor)"
                r"\s+(?:de\s+)?"
                r"(?:la\s+|el\s+)?"
                r"(?:accion\s+)?"
                r"(?:de\s+)?"
                r"([\w\s]+)",
                texto_limpio,
                re.IGNORECASE
            )

            # -----------------------------------------
            # REGLAS PARA DETECTAR CLIMA
            # -----------------------------------------
            weather_match = re.search(
                r"(?:temperatura|clima|tiempo)"
                r"\s+(?:(?:en|de)\s+)?"
                r"([\w\s]+)",
                texto_limpio,
                re.IGNORECASE
            )

            # -----------------------------------------
            # CASO 1: PRECIO DE UNA ACCIÓN
            # -----------------------------------------
            if stock_match:
                price = obtener_precio_accion(None, texto_limpio)

                if price:
                    print(f">>> {price}")
                else:
                    print(
                        ">>> Lo siento, no pude encontrar el precio de la acción."
                    )

            # -----------------------------------------
            # CASO 2: CLIMA
            # -----------------------------------------
            elif weather_match:
                temp = obtener_clima(None, texto_limpio)

                if temp:
                    print(f">>> {temp}")
                else:
                    print(
                        ">>> Lo siento, no pude obtener el clima."
                    )

            # -----------------------------------------
            # CASO 3: NO SE RECONOCE LA SOLICITUD
            # -----------------------------------------
            else:
                print(
                    ">>> No estoy seguro de cómo ayudarte con eso. "
                    "Prueba preguntando por el precio de una acción "
                    "o el clima en una ciudad."
                )

        except KeyboardInterrupt:
            print("\n>>> ¡Hasta luego!")
            break

        except Exception as e:
            print(f">>> Ocurrió un error: {e}")


# Punto de entrada principal
if __name__ == "__main__":
    chatbot()
```
