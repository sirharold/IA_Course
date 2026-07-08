from __future__ import annotations

import requests


def call_get() -> None:
    # Hacer una llamada GET a https://httpbin.org/get
    # Incluir al menos 2 o 3 query params
    # Validar el status_code o usar raise_for_status()
    # Convertir la respuesta a JSON
    # Imprimir solo la informacion relevante:
    # - status
    # - url final
    # - args recibidos
    pass


def call_post() -> None:
    # Hacer una llamada POST a https://httpbin.org/post
    # Enviar un body JSON con al menos 3 campos
    # Validar el status_code o usar raise_for_status()
    # Convertir la respuesta a JSON
    # Imprimir solo la informacion relevante:
    # - status
    # - url final
    # - json reflejado por la API
    pass


if __name__ == "__main__":
    call_get()
    call_post()
