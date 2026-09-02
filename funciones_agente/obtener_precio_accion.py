import yfinance as yf
from utils.sanitizar import sanitizar


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
    "netflix": "NFLX",
    "nflx": "NFLX",
    "nvidia": "NVDA",
    "nvda": "NVDA",
}


def obtener_precio_accion(driver, texto):
    texto = sanitizar(texto)

    ticker = None
    empresa = None

    for nombre, simbolo in COMPANY_TICKERS.items():
        if nombre in texto:
            ticker = simbolo
            empresa = nombre
            break

    if ticker is None:
        return "No pude identificar la empresa. Prueba con Microsoft, Apple, Google, Amazon, Tesla, Meta, Netflix o Nvidia."

    try:
        accion = yf.Ticker(ticker)
        datos = accion.history(period="1d")

        if datos.empty:
            return f"No se encontraron datos para {empresa}."

        precio = datos["Close"].iloc[-1]

        return f"{empresa.capitalize()} ({ticker}): ${precio:.2f}"

    except Exception as e:
        return f"No fue posible obtener el precio de {empresa}: {e}"
