# Documentación de service.py

## Ubicación

- Módulo: `payment_review/service.py`
- Entrada principal relacionada: `main.py`

## Propósito del módulo

El módulo `service.py` orquesta el flujo completo de revisión de pagos:

1. Carga datos desde un archivo JSON.
2. Normaliza campos clave para estandarizar entradas.
3. Evalúa reglas de riesgo por cada pago.
4. Construye un resumen legible para cada resultado.
5. Imprime un reporte en consola.

No define reglas de negocio ni formato detallado de resumen por sí mismo. Esas responsabilidades se delegan a otros módulos:

- `payment_review.normalizers`
- `payment_review.rules`
- `payment_review.reporting`

## Dependencias internas

`service.py` importa:

- `normalize_customer_name`, `normalize_currency`, `normalize_channel` desde `payment_review.normalizers`
- `evaluate_review` desde `payment_review.rules`
- `build_review_summary` desde `payment_review.reporting`

También usa:

- `json` para leer el archivo de datos
- `pathlib.Path` para construir rutas del proyecto

## Constantes

### `BASE_DIR`

Ruta base del proyecto calculada desde la ubicación del archivo.

### `DEFAULT_DATA_FILE`

Ruta por defecto del dataset:

- `data/sample_reviews.json`

Esta ruta se utiliza como valor predeterminado en todas las funciones públicas del módulo.

## Funciones

## `load_reviews(path=DEFAULT_DATA_FILE)`

### Qué hace

Lee el archivo JSON de entrada y normaliza campos por registro para dejar una estructura uniforme.

### Parámetros

- `path`: ruta del archivo JSON a cargar. Si no se entrega, usa `DEFAULT_DATA_FILE`.

### Retorna

Lista de diccionarios normalizados, uno por pago, con la forma:

- `payment_id`
- `customer_name` (normalizado)
- `amount`
- `currency` (normalizada)
- `channel` (normalizado)
- `tags`
- `notes`

### Flujo interno

1. Abre el archivo con codificación UTF-8.
2. Carga el arreglo JSON.
3. Recorre cada item y aplica normalización campo a campo.
4. Agrega cada registro normalizado a la lista final.

## `review_payments(path=DEFAULT_DATA_FILE)`

### Qué hace

Ejecuta el pipeline de revisión para todos los pagos cargados.

### Parámetros

- `path`: ruta al archivo JSON de entrada.

### Retorna

Lista de resultados empaquetados por pago. Cada elemento incluye:

- `raw`: pago normalizado
- `review`: resultado de reglas (`score`, `status`, `reasons`)
- `summary`: resumen legible (`headline`, `detail`, `priority`, etc.)

### Flujo interno

1. Llama a `load_reviews`.
2. Recorre pagos normalizados.
3. Para cada pago:
   - Evalúa riesgo con `evaluate_review`.
   - Construye resumen con `build_review_summary`.
   - Empaqueta todo en un objeto único.
4. Retorna la colección completa.

## `print_report(path=DEFAULT_DATA_FILE)`

### Qué hace

Imprime en consola un reporte con resultados resumidos de cada pago.

### Parámetros

- `path`: ruta al archivo JSON de entrada.

### Retorna

No retorna valor explícito. Su efecto es de salida por consola.

### Salida esperada

Por cada pago imprime:

- Headline del resumen
- Detalle del resumen
- Prioridad
- Separador visual

## Punto de ejecución directa

Cuando se ejecuta `service.py` como script principal (`python service.py`), llama a:

- `print_report()`

Esto permite correr el módulo de forma autónoma para depuración rápida.

## Supuestos actuales

1. El JSON de entrada existe y tiene formato válido.
2. El contenido del JSON es una lista de objetos de pago.
3. Los campos ausentes pueden resolverse con defaults simples (`""`, `0`, `[]`).
4. La salida estándar (stdout) está disponible para imprimir el reporte.

## Limitaciones observables

1. No hay manejo explícito de errores para archivo inexistente o JSON corrupto.
2. No hay validación estricta de tipos antes de evaluar reglas.
3. El formato del reporte está acoplado a consola (no retorna texto formateado).
4. No hay logging estructurado ni niveles de severidad.

## Mejoras recomendadas

1. Agregar manejo de excepciones en la carga de datos (`FileNotFoundError`, `JSONDecodeError`).
2. Separar lógica de presentación para soportar otros formatos de salida (por ejemplo JSON o CSV).
3. Incorporar type hints en firmas y estructuras de retorno.
4. Añadir pruebas unitarias para `load_reviews`, `review_payments` y `print_report`.
5. Inyectar dependencias de reglas/reporting para facilitar testeo y extensibilidad.

## Relación con el flujo del proyecto

Desde `main.py`, la aplicación invoca `print_report`. Por lo tanto, `service.py` funciona como capa de aplicación que conecta normalización, evaluación y reporte en una sola secuencia ejecutable.
