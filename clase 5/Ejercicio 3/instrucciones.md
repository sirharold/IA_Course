# Ejercicio 3 - Variables de entorno y autenticacion

## Objetivo

Consumir una API local con header de autenticacion y configuracion leida desde entorno.

## Archivo principal

- `ejercicio3_auth.py`

## API usada

- `../mock_api/mock_service.py`

## Lo que deben hacer

- levantar el mock local si no esta levantado;
- exportar `DEMO_API_KEY`;
- ejecutar el script;
- probar un error 401 cambiando la clave.

## Prompt sugerido para Copilot

```text
Revisa este cliente Python.
Quiero leer API key desde os.getenv, manejar 401 con un mensaje claro y no hardcodear configuracion dentro del script.
Haz cambios pequenos.
```
