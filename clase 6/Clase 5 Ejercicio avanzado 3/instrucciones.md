# Ejercicio avanzado 3 - Comparar respuestas entre modelos con OpenRouter

## Objetivo

Comparar varios modelos gratuitos de OpenRouter usando el mismo prompt tecnico y decidir cual entrega la mejor respuesta para este caso.

## Archivos del ejercicio

- `advanced3_openrouter_compare.py`
- `prompt_fijo.txt`
- `selected_models.txt.example`
- `evaluacion_modelos.md`

## Que van a hacer

1. crear una cuenta en OpenRouter;
2. generar una API key;
3. pedir a Copilot modelos gratuitos de OpenRouter que sean realmente diferentes entre si;
4. ejecutar el mismo prompt con cada modelo;
5. registrar las respuestas;
6. comparar los resultados y elegir el mejor modelo.

## Importante

No usen `openrouter/free` para este ejercicio.

Ese router elige modelos al azar y arruina la comparacion, porque ustedes necesitan saber exactamente que modelo respondio.

## Paso 1. Crear cuenta en OpenRouter

1. Entren a [OpenRouter](https://openrouter.ai/).
2. Creen una cuenta o inicien sesion.
3. Una vez dentro, abran la seccion de API keys.
4. Creen una API key nueva.
5. Asignen un nombre reconocible, por ejemplo:
   - `curso-clase-5`
6. Copien la clave generada.
7. No la peguen dentro del codigo.

## Paso 2. Guardar la API key en una variable de entorno

### Opcion A. PowerShell

```powershell
$env:OPENROUTER_API_KEY="pega_aqui_tu_api_key"
```

Para verificarla:

```powershell
echo $env:OPENROUTER_API_KEY
```

### Opcion B. bash

```bash
export OPENROUTER_API_KEY="pega_aqui_tu_api_key"
```

Para verificarla:

```bash
echo $OPENROUTER_API_KEY
```

## Paso 3. Elegir modelos gratuitos y realmente distintos

Antes de escribir codigo o ejecutar el script, entren en modo ASK.

Primero revisen la coleccion oficial de modelos gratis de OpenRouter:

- [OpenRouter Free Models](https://openrouter.ai/collections/free-models)

Luego pidan ayuda a Copilot.

Su objetivo no es pedir "tres modelos gratis" sin mas.
Su objetivo es pedir modelos:

- gratuitos hoy en OpenRouter;
- con slugs exactos;
- de fabricantes o familias distintas cuando sea posible;
- que no sean simples variantes casi iguales;
- que probablemente produzcan respuestas diferentes al responder el mismo prompt tecnico.

### Prompt para Copilot en modo ASK

```text
Quiero comparar modelos gratuitos actuales de OpenRouter.

Necesito que me propongas 3 modelos gratis que sean suficientemente distintos entre si como para que, al responder el mismo prompt tecnico, produzcan respuestas perceptiblemente diferentes.

Condiciones:
1. todos deben estar disponibles gratis hoy en OpenRouter;
2. dame el slug exacto de cada modelo;
3. evita proponer tres variantes casi iguales del mismo fabricante;
4. prioriza diversidad real:
   - al menos 2 fabricantes distintos;
   - idealmente 3 familias distintas;
   - si es posible, combina un modelo pequeno o rapido, uno mas orientado a razonamiento y otro generalista;
5. explica brevemente por que esperas respuestas diferentes entre ellos.

Devuelveme una tabla con:
- slug;
- proveedor o fabricante;
- por que es diferente;
- por que vale la pena compararlo en este ejercicio.
```

## Paso 4. Registrar los modelos elegidos

1. Copien `selected_models.txt.example` a `selected_models.txt`.
2. Reemplacen el contenido con los 3 slugs elegidos por ustedes.
3. Dejen un modelo por linea.

### Opcion A. PowerShell

```powershell
Copy-Item selected_models.txt.example selected_models.txt
```

### Opcion B. bash

```bash
cp selected_models.txt.example selected_models.txt
```

Ejemplo de formato:

```text
modelo-uno
modelo-dos
modelo-tres
```

## Paso 5. Revisar el prompt fijo

El archivo `prompt_fijo.txt` contiene el mismo prompt que se usara para todos los modelos.

No lo cambien al principio.

La comparacion solo tiene sentido si:

- el prompt es exactamente el mismo;
- el orden de ejecucion es comparable;
- las respuestas se registran separadas por modelo.

## Paso 6. Ejecutar el script

Desde la carpeta del ejercicio:

### Opcion A. PowerShell

```powershell
python .\advanced3_openrouter_compare.py
```

### Opcion B. bash

```bash
python3 advanced3_openrouter_compare.py
```

Cuando funcione, el script creara una carpeta `outputs/` con:

- un archivo por modelo;
- un resumen `summary.json`.

## Paso 7. Revisar y evaluar las respuestas

Lean las respuestas generadas en `outputs/`.

Luego completen `evaluacion_modelos.md` con una comparacion simple.

## Que deben observar

No comparen solo "cual respondio mas bonito".

Comparen al menos estos puntos:

- claridad;
- utilidad tecnica;
- especificidad;
- cumplimiento del formato pedido;
- manejo de incertidumbre;
- calidad de la recomendacion final.

## Paso 8. Elegir el mejor modelo

Al final deben poder justificar:

1. cual modelo respondio mejor;
2. por que;
3. en que tipo de caso tecnico volverian a usarlo.

## Prompt para Copilot en modo Agent

Usen este prompt si quieren ayuda para mejorar el script sin reescribirlo completo:

```text
Revisa este script Python que compara respuestas entre modelos de OpenRouter.
Quiero mantenerlo pequeno, pero mejorar:
1. lectura de modelos desde archivo;
2. guardado de respuestas por modelo;
3. manejo simple de errores;
4. resumen final en JSON.

No hagas una refactorizacion grande.
```

## Entregable esperado

- `selected_models.txt` con 3 modelos;
- carpeta `outputs/` con las respuestas;
- `evaluacion_modelos.md` completado;
- una conclusion breve sobre el mejor modelo.

## Referencias oficiales

- [OpenRouter Quickstart](https://openrouter.ai/docs/quickstart)
- [OpenRouter Authentication](https://openrouter.ai/docs/api/reference/authentication)
- [OpenRouter Free Models](https://openrouter.ai/collections/free-models)
