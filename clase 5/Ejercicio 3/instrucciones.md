# Ejercicio 3 - Variables de entorno y autenticacion

## Objetivo

Consumir una API local con header de autenticacion y configuracion leida desde entorno.

## Archivo principal

- `ejercicio3_auth.py`

## API usada

- `../mock_api/mock_service.py`

## Lo que deben hacer

- levantar el mock local en una terminal separada;
- copiar la URL base de la API local;
- usar esa URL en el cliente;
- exportar `DEMO_API_KEY`;
- ejecutar el script;
- probar un error 401 cambiando la clave.

## Levantar la mock API

1. Abrir una terminal nueva.
2. Cambiar al directorio del ejercicio o a la carpeta `clase 5` del repo.
3. Ejecutar el servicio mock:

```bash
cd "clase 5/mock_api"
python3 mock_service.py
```

4. Observar en consola la URL base del servicio:

```text
http://127.0.0.1:8010
```

5. Copiar esa URL, porque la van a usar en el codigo del cliente.

## Flujo recomendado con Copilot

### Paso 1. Entrar en modo ASK

Antes de modificar el codigo, pedir a Copilot que revise el archivo y explique:

- que configuracion necesita;
- como deberia usarse la URL del mock;
- donde conviene separar configuracion y codigo.

### Prompt sugerido para Copilot en modo ASK

```text
Revisa este cliente Python para una API local.
Necesito que me expliques:
1. que valores deberia parametrizar;
2. donde debo usar la URL base del mock;
3. como deberia leer la API key desde entorno;
4. que errores minimos deberia manejar.

No escribas aun la solucion completa.
```

### Paso 2. Volver a modo Agent

Cuando ya tengan claro el flujo, pasar a modo Agent para modificar el script.

## Prompt sugerido para Copilot en modo Agent

```text
Revisa este cliente Python.
Quiero:
1. leer API key desde os.getenv;
2. usar una BASE_URL configurable para apuntar al mock local;
3. manejar 401 con un mensaje claro;
4. no hardcodear configuracion sensible dentro del script.

Haz cambios pequenos y legibles.
```
