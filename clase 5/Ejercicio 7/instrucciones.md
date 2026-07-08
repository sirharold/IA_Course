# Ejercicio 7 - Desacoplar el flujo

## Objetivo

Separar obtencion de datos, validacion y salida para que el cambio de endpoint no obligue a reescribir todo.

## Archivo principal

- `ejercicio7_refactor.py`

## Lo que deben hacer

- partir desde este script;
- levantar la mock API si la van a usar como fuente local;
- separar mejor las funciones;
- dejar el endpoint configurable con variables de entorno;
- preparar el cambio entre fuente publica y local.

## Levantar la fuente local

Si quieren trabajar contra el mock local:

1. Abrir una terminal nueva.
2. Cambiar al directorio:

```bash
cd "clase 5/mock_api"
```

3. Ejecutar:

```bash
python3 mock_service.py
```

4. Tomar la URL base:

```text
http://127.0.0.1:8010
```

5. Exportar variables:

```bash
export API_BASE_URL='http://127.0.0.1:8010'
export DEMO_API_KEY='demo-local-key'
```

## Flujo recomendado con Copilot

### Paso 1. Entrar en modo ASK

Antes de refactorizar, pedir a Copilot que identifique:

- donde esta el acoplamiento;
- que partes deberian separarse;
- como pasar de valores hardcodeados a configuracion.

### Prompt sugerido para Copilot en modo ASK

```text
Revisa este script Python.
Antes de refactorizarlo, explicame:
1. donde esta acoplado al endpoint actual;
2. que partes conviene separar en funciones;
3. que configuracion deberia salir a variables de entorno;
4. como dejarlo listo para cambiar entre una fuente local y otra externa.

No generes aun una solucion demasiado grande.
```

### Paso 2. Volver a modo Agent

Cuando ya tengan claro el problema, pasar a Agent para hacer la refactorizacion.

## Prompt sugerido para Copilot en modo Agent

```text
Revisa este script Python.
Quiero una refactorizacion pequena para separar:
1. obtencion de datos;
2. validacion;
3. salida final.
Mantiene el comportamiento actual, usa variables de entorno y no agregues complejidad innecesaria.
```

## Mejora sugerida

- Dejar una funcion para:
  - leer configuracion;
  - llamar el endpoint;
  - validar la respuesta;
  - presentar la salida.
