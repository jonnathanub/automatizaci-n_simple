from funciones_agente.obtener_precio_accion import obtener_precio_accion
from funciones_agente.obtener_clima import obtener_clima
from utils.sanitizar import sanitizar


def test_chatbot():
    print("--- Iniciando Pruebas de Funciones ---")

    print("\n[Prueba 1] Sanitizacion de texto...")
    texto = sanitizar("Oaxaca de Juarez")
    print(f"Resultado: {texto}")
    assert texto == "oaxaca de juarez"
    print("OK - Sanitizacion correcta.")

    print("\n[Prueba 2] Precio de accion para Microsoft...")
    msft_price = obtener_precio_accion(None, "precio de la accion Microsoft")
    print(f"Resultado Microsoft: {msft_price}")
    assert msft_price is not None
    assert len(msft_price) > 0
    print("OK - Consulta de Microsoft correcta.")

    print("\n[Prueba 3] Precio de accion para Apple...")
    apple_price = obtener_precio_accion(None, "precio de Apple")
    print(f"Resultado Apple: {apple_price}")
    assert apple_price is not None
    assert len(apple_price) > 0
    print("OK - Consulta de Apple correcta.")

    print("\n[Prueba 4] Consulta del clima...")
    clima = obtener_clima(None, "clima en Ciudad de Mexico")
    print(f"Resultado clima: {clima}")
    assert clima is not None
    assert len(clima) > 0
    print("OK - Consulta del clima correcta.")

    print("\n================================")
    print("OK - TODAS LAS PRUEBAS TERMINARON")
    print("================================")


if __name__ == "__main__":
    test_chatbot()
