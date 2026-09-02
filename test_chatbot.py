```python
from funciones_agente.obtener_precio_accion import obtener_precio_accion
from funciones_agente.obtener_clima import obtener_clima
from utils.sanitizar import sanitizar


def test_chatbot():
    """
    Pruebas básicas para verificar que las funciones
    principales del chatbot sigan funcionando.
    """

    print("--- Iniciando Pruebas de Funciones ---")

    # ------------------------------------------------
    # PRUEBA 1: Sanitización
    # ------------------------------------------------
    print("\n[Prueba 1] Sanitización de texto...")

    texto = sanitizar("Oaxaca de Juárez")

    print(f"Resultado: {texto}")

    assert texto == "oaxaca de juarez"

    print("✓ Sanitización correcta.")

    # ------------------------------------------------
    # PRUEBA 2: Precio de Microsoft
    # ------------------------------------------------
    print("\n[Prueba 2] Precio de acción para Microsoft...")

    msft_price = obtener_precio_accion(
        None,
        "precio de la accion Microsoft"
    )

    print(f"Resultado Microsoft: {msft_price}")

    assert msft_price is not None
    assert len(msft_price) > 0

    print("✓ Consulta de Microsoft correcta.")

    # ------------------------------------------------
    # PRUEBA 3: Precio de Apple
    # ------------------------------------------------
    print("\n[Prueba 3] Precio de acción para Apple...")

    apple_price = obtener_precio_accion(
        None,
        "precio de Apple"
    )

    print(f"Resultado Apple: {apple_price}")

    assert apple_price is not None
    assert len(apple_price) > 0

    print("✓ Consulta de Apple correcta.")

    # ------------------------------------------------
    # PRUEBA 4: Clima
    # ------------------------------------------------
    print("\n[Prueba 4] Consulta del clima...")

    clima = obtener_clima(
        None,
        "clima en Ciudad de Mexico"
    )

    print(f"Resultado clima: {clima}")

    assert clima is not None
    assert len(clima) > 0

    print("✓ Consulta del clima correcta.")

    # ------------------------------------------------
    # PRUEBAS TERMINADAS
    # ------------------------------------------------
    print("\n================================")
    print("✓ TODAS LAS PRUEBAS TERMINARON")
    print("================================")


if __name__ == "__main__":
    test_chatbot()
```
