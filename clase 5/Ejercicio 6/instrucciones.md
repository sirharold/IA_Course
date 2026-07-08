# Ejercicio 6 - Prompt como parte del pipeline

## Objetivo

Conectar entrada, request, response y validacion en un flujo pequeno.

## Archivo principal

- `ejercicio6_pipeline.py`

## API usada

- `../mock_api/mock_service.py`

## Lo que deben hacer

- ejecutar el mock local;
- leer una linea de incidentes;
- llamar el endpoint;
- validar campos esperados;
- mejorar la salida con ayuda de Copilot.

## Levantar la mock API

1. Abrir una terminal nueva.
2. Cambiar al directorio del mock:

```bash
cd "clase 5/mock_api"
```

3. Ejecutar el servicio:

```bash
python3 mock_service.py
```

4. Confirmar la URL base:

```text
http://127.0.0.1:8010
```

## Flujo recomendado con Copilot

### Paso 1. Entrar en modo ASK

Antes de modificar el codigo, pedir a Copilot que explique:

- donde entra el texto;
- donde se construye el request;
- donde se procesa la respuesta;
- que validaciones faltan.

### Prompt sugerido para Copilot en modo ASK

```text
Revisa este pipeline pequeno en Python.
Antes de modificarlo, explicame:
1. que parte corresponde a entrada;
2. que parte corresponde al request;
3. que parte corresponde al postproceso;
4. que validaciones minimas faltan.

No escribas aun toda la solucion final.
```

### Paso 2. Volver a modo Agent

Cuando ya tengan claro el flujo, pasar a Agent para ajustar el script.

## Prompt sugerido para Copilot en modo Agent

```text
Revisa este pipeline pequeno en Python.
Quiero validar system, severity, symptom y next_step y luego mostrar una salida reducida.
Haz cambios pequenos.
```

## Mejora sugerida

- Separar en funciones:
  - lectura del incidente;
  - llamada HTTP;
  - validacion de la respuesta;
  - salida final.
