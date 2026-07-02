# Documentación de normalizers.py

## Propósito

El módulo `payment_review/normalizers.py` centraliza la limpieza y estandarización de datos de entrada antes de aplicar reglas de negocio.

Su objetivo es reducir inconsistencias en campos clave de pagos (nombre de cliente, canal y moneda) para que el resto del sistema trabaje con valores más predecibles y comparables.

Funciones incluidas:

- `normalize_customer_name(raw_name)`
- `normalize_channel(channel)`
- `normalize_currency(currency)`

---

## normalize_customer_name(raw_name)

### Propósito

Normalizar el nombre del cliente para presentarlo en un formato legible y consistente.

### Parámetros

- `raw_name` (`Any`): valor crudo del nombre del cliente. Puede venir como `None`, string o cualquier otro tipo convertible a string.

### Retorno

- `str`: nombre normalizado.
   - Retorna cadena vacía `""` cuando el valor no existe o queda vacío luego del `strip()`.
   - Separa por `_` y `-` (convirtiéndolos a espacios).
   - Cada parte con longitud menor o igual a 2 se convierte a mayúscula completa (ejemplo: `"id" -> "ID"`).
   - Cada parte con longitud mayor a 2 se convierte con primera letra en mayúscula y resto en minúscula.

### Supuestos

- Se asume que una capitalización simple por token es suficiente para el dominio.
- Se asume que tokens cortos (<= 2) representan siglas o abreviaciones.
- No se preserva puntuación especial distinta de `_` y `-`.

---

## normalize_channel(channel)

### Propósito

Estandarizar el canal de pago para reducir variantes de escritura y mapear alias comunes.

### Parámetros

- `channel` (`Any`): canal crudo de entrada (`None`, string u otro tipo convertible a string).

### Retorno

- `str`: canal normalizado.
  - Si `channel` es `None`, retorna `"unknown"`.
   - Convierte a minúsculas y elimina espacios exteriores.
   - Aplica alias:
    - `webapp`, `browser` -> `web`
    - `app`, `ios`, `android` -> `mobile`
  - Si no hay alias, devuelve el valor normalizado.
   - Si el valor resultante queda vacío, devuelve `"unknown"`.

### Supuestos

- Se asume que solo existen los alias definidos en el diccionario local.
- Se asume que `unknown` es una categoría válida para canales no informados.
- No hay validación contra un catálogo maestro de canales.

---

## normalize_currency(currency)

### Propósito

Normalizar el código de moneda para usar convenciones estables en reglas y reportes.

### Parámetros

- `currency` (`Any`): valor de moneda crudo.

### Retorno

- `str`: moneda normalizada.
  - Si `currency` es falsy (`None`, `""`, etc.), retorna `"CLP"`.
   - Convierte a mayúsculas y elimina espacios exteriores.
  - Mapeos especiales:
    - `"$"` -> `"CLP"`
    - `"USD$"` -> `"USD"`
   - Para otros casos, devuelve el valor en mayúsculas.

### Supuestos

- Se asume `CLP` como moneda por defecto del sistema.
- Se asume que los símbolos tratados (`$`, `USD$`) cubren los formatos observados en datos de ejemplo.
- No se valida el código contra ISO 4217.

---

## Supuestos Globales del Módulo

- La normalización se ejecuta antes de evaluar reglas de riesgo.
- Los datos pueden venir con ruido (espacios, mayúsculas/minúsculas mixtas, separadores inconsistentes).
- El módulo prioriza simplicidad y legibilidad por sobre cobertura total de casos lingüísticos o regionales.

---

## Futuras Mejoras

1. Reemplazar la lógica de `normalize_customer_name` por una estrategia más robusta para nombres reales:
   - Manejar apostrofes, preposiciones (`de`, `del`, `van`), acentos y casos compuestos.
   - Evitar sobre-normalizar siglas legítimas.

2. Externalizar alias de canal y moneda a configuración:
   - Mover diccionarios a archivo de configuración (`json/yaml`) o constantes de dominio.
   - Permitir cambios sin editar codigo.

3. Agregar validaciones explícitas y observabilidad:
   - Registrar valores desconocidos de canal/moneda para análisis posterior.
   - Incorporar conteos de frecuencia para detectar nuevas variantes.

4. Implementar pruebas unitarias dedicadas al modulo:
   - Casos nominales.
   - Casos borde (`None`, vacíos, tipos inesperados).
   - Regresiones por alias y defaults.

5. Definir contratos de tipos mas estrictos:
   - Agregar type hints en todas las funciones.
   - Considerar `TypedDict` o modelos de datos para entradas normalizadas.

6. Unificar criterios de defaults con reglas de negocio:
   - Revisar junto al motor de reglas si `CLP` y `unknown` siguen siendo defaults adecuados para todos los escenarios.
