# Ejercicio avanzado 2 - Comparar modo interactivo vs no interactivo

## Objetivo

Resolver la misma mejora tecnica usando:

1. `copilot -p` en modo no interactivo;
2. `copilot` en modo interactivo;
3. una comparacion final entre ambos enfoques.

## Archivos del ejercicio

- `log_quality_check.py`
- `sample_runtime_logs.ndjson`

## Resultado esperado

Al final del ejercicio, el script debe:

- contar errores totales;
- contar errores por servicio;
- contar eventos `WARN` o `ERROR` sin `correlation_id`;
- imprimir un resumen claro en consola.

## Paso 1. Entrar a la carpeta del ejercicio

En `bash` o `zsh`:

```bash
cd "ruta/a/la/carpeta/clase 6/Ejercicio avanzado 2"
ls -la
```

En `PowerShell`:

```powershell
Set-Location "ruta\a\la\carpeta\clase 6\Ejercicio avanzado 2"
Get-ChildItem
```

## Paso 2. Ejecutar el script actual

En `bash` o `zsh`:

```bash
python3 log_quality_check.py
```

En `PowerShell`:

```powershell
python log_quality_check.py
```

## Paso 3. Pedir una propuesta en modo no interactivo

En `bash` o `zsh`:

```bash
copilot -p "Revisa log_quality_check.py y sample_runtime_logs.ndjson. Necesito una mejora pequena para que el script: 1) cuente errores totales, 2) cuente errores por servicio, 3) cuente eventos WARN o ERROR sin correlation_id, 4) imprima un resumen mas claro. Responde con pasos concretos y cambios sugeridos, sin reescribir todo." > propuesta_no_interactiva.md
```

En `PowerShell`:

```powershell
copilot -p "Revisa log_quality_check.py y sample_runtime_logs.ndjson. Necesito una mejora pequena para que el script: 1) cuente errores totales, 2) cuente errores por servicio, 3) cuente eventos WARN o ERROR sin correlation_id, 4) imprima un resumen mas claro. Responde con pasos concretos y cambios sugeridos, sin reescribir todo." > propuesta_no_interactiva.md
```

## Paso 4. Abrir Copilot CLI en modo interactivo

En `bash`, `zsh` o `PowerShell`:

```bash
copilot
```

## Paso 5. Hacer la misma consulta en modo interactivo

Dentro de Copilot CLI, usar este prompt:

```text
Revisa log_quality_check.py y sample_runtime_logs.ndjson.
Quiero la misma mejora que antes:
1. contar errores totales;
2. contar errores por servicio;
3. contar WARN o ERROR sin correlation_id;
4. dejar una salida corta y operativa.
Propon una implementacion pequena, explicable y segura.
```

Guardar o copiar la respuesta en un archivo llamado `propuesta_interactiva.md`.

## Paso 6. Comparar ambas propuestas

Revisar `propuesta_no_interactiva.md` y `propuesta_interactiva.md`.

Elegir una sola ruta de implementacion. No mezclar ideas innecesarias.

## Paso 7. Modificar `log_quality_check.py`

Hagan exactamente estos cambios:

1. Mantener la lectura del archivo NDJSON.
2. Agregar conteo total de `ERROR`.
3. Agregar conteo de `ERROR` por `service`.
4. Agregar conteo de registros `WARN` o `ERROR` sin `correlation_id`.
5. Dejar una salida final de no mas de 8 lineas.

## Paso 8. Ejecutar y validar el resultado

En `bash` o `zsh`:

```bash
python3 log_quality_check.py
```

En `PowerShell`:

```powershell
python log_quality_check.py
```

## Paso 9. Comparacion final con `copilot -p`

En `bash` o `zsh`:

```bash
copilot -p "Compara propuesta_no_interactiva.md, propuesta_interactiva.md y log_quality_check.py. En 5 lineas, dime que modo fue mas util para esta tarea y por que." > comparacion_final.md
```

En `PowerShell`:

```powershell
copilot -p "Compara propuesta_no_interactiva.md, propuesta_interactiva.md y log_quality_check.py. En 5 lineas, dime que modo fue mas util para esta tarea y por que." > comparacion_final.md
```

## Entregables

- `log_quality_check.py` modificado
- `propuesta_no_interactiva.md`
- `propuesta_interactiva.md`
- `comparacion_final.md`
