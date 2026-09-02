```python
import yfinance as yf
from utils.sanitizar import sanitizar


# Diccionario de empresas y sus símbolos bursátiles
COMPANY_TICKERS = {
    "microsoft": "MSFT",
    "msft": "MSFT",

    "apple": "AAPL",
    "aapl": "AAPL",

    "google": "GOOGL",
    "alphabet": "GOOGL",
    "googl": "GOOGL",

    "amazon": "AMZN",
    "amzn": "AMZN",

    "tesla": "TSLA",
    "tsla": "TSLA",

    "meta": "META",
    "facebook": "META",
    "meta platforms": "META",

    "netflix": "NFLX",
    "nflx": "NFLX",

    "nvidia": "NVDA",
    "nvda": "NVDA",
}


def obtener_precio_accion(driver, user_input):
    """
    Obtiene el precio actual de una acción utilizando Yahoo Finance.

    El parámetro driver se mantiene porque forma parte de la interfaz
    utilizada por el chatbot y permite utilizar Selenium posteriormente.
    """

    texto = sanitizar(user_input)

    # Buscar primero empresas conocidas dentro de la consulta
    ticker = None
    empresa_encontrada = None

    # Ordenamos por longitud para detectar primero nombres compuestos
    # como "meta platforms".
    empresas = sorted(
        COMPANY_TICKERS.keys(),
        key=len,
        reverse=True
    )

    for empresa in empresas:
        if empresa in texto:
            ticker = COMPANY_TICKERS[empresa]
            empresa_encontrada = empresa
            break

    # Si no encontramos una empresa conocida, intentamos obtener
    # un símbolo bursátil de la consulta.
    if ticker is None:
        palabras = texto.split()

        for palabra in palabras:
            palabra_limpia = palabra.strip(".,!?¿¡")

            if palabra_limpia.upper() in COMPANY_TICKERS:
                ticker = COMPANY_TICKERS[palabra_limpia.lower()]
                empresa_encontrada = palabra_limpia
                break

    # Si no se encontró ninguna empresa
    if ticker is None:
        return (
            "No reconocí la empresa. Puedes consultar, por ejemplo: "
            "Microsoft, Apple, Google, Amazon, Tesla, Meta, Netflix o Nvidia."
        )

    try:
        # Obtener información de Yahoo Finance
        accion = yf.Ticker(ticker)

        datos = accion.history(period="1d")

        if datos.empty:
            return (
                f"No se encontraron datos para {empresa_encontrada} "
                f"({ticker})."
            )

        # Obtener el último precio disponible
        precio = datos["Close"].iloc[-1]

        if precio is None:
            return "No se pudo obtener el precio de la acción."

        # Mostrar el precio con dos decimales
        precio_formateado = f"{float(precio):,.2f}"

        nombre_mostrado = empresa_encontrada.capitalize()

        return f"{nombre_mostrado} ({ticker}): ${precio_formateado}"

    except Exception as e:
        print(f"Error al consultar Yahoo Finance: {e}")

        return (
            f"No se pudo obtener el precio de {empresa_encontrada} "
            f"en este momento."
        )
```
