# Ejercicio avanzado 3 - De tarea a cambio revisable en terminal

## Objetivo

Recorrer un flujo completo desde terminal:

1. entender una tarea;
2. pedir una propuesta de cambio;
3. modificar el codigo;
4. ejecutar una validacion;
5. pedir una revision final desde Copilot CLI.

## Archivos del ejercicio

- `sync_incidents.py`
- `sample_incidents.json`
- `validate_sync.py`

## Resultado esperado

Al final del ejercicio, `sync_incidents.py` debe:

- aceptar `--input` y `--output`;
- ignorar registros invalidos en vez de romperse;
- generar un resumen final con cantidad procesada y descartada;
- producir un JSON de salida valido para `validate_sync.py`.

## Paso 1. Entrar a la carpeta del ejercicio

En `bash` o `zsh`:

```bash
cd "ruta/a/la/carpeta/clase 6/Ejercicio avanzado 3"
ls -la
```

En `PowerShell`:

```powershell
Set-Location "ruta\a\la\carpeta\clase 6\Ejercicio avanzado 3"
Get-ChildItem
```

## Paso 2. Ejecutar el script actual

En `bash` o `zsh`:

```bash
python3 sync_incidents.py
```

En `PowerShell`:

```powershell
python sync_incidents.py
```

## Paso 3. Ejecutar el validador actual

En `bash` o `zsh`:

```bash
python3 validate_sync.py incident_sync_output.json
```

En `PowerShell`:

```powershell
python validate_sync.py incident_sync_output.json
```

## Paso 4. Abrir Copilot CLI en modo interactivo

En `bash`, `zsh` o `PowerShell`:

```bash
copilot
```

## Paso 5. Pedir analisis y plan

Dentro de Copilot CLI, usar este prompt:

```text
Revisa sync_incidents.py, sample_incidents.json y validate_sync.py.
Necesito un plan pequeno y seguro para que sync_incidents.py:
1. acepte --input y --output;
2. no falle con registros incompletos;
3. descarte registros invalidos con una razon visible;
4. deje una salida valida para validate_sync.py.
No propongas una reescritura completa.
```

## Paso 6. Implementar exactamente esta ruta de cambio

Modificar `sync_incidents.py` para que:

1. use `argparse` con `--input` y `--output`;
2. mantenga valores por defecto si no se pasan argumentos;
3. valide que cada item tenga:
   - `ticket_id`
   - `service`
   - `severity`
   - `state`
4. descarte registros invalidos;
5. imprima un resumen final:
   - procesados;
   - descartados;
   - archivo de salida.

## Paso 7. Ejecutar el script modificado

En `bash` o `zsh`:

```bash
python3 sync_incidents.py --input sample_incidents.json --output incident_sync_output.json
```

En `PowerShell`:

```powershell
python sync_incidents.py --input sample_incidents.json --output incident_sync_output.json
```

## Paso 8. Validar la salida

En `bash` o `zsh`:

```bash
python3 validate_sync.py incident_sync_output.json
```

En `PowerShell`:

```powershell
python validate_sync.py incident_sync_output.json
```

## Paso 9. Pedir una revision final desde Copilot CLI

Volver a `copilot` y pedir revision con una de estas dos opciones.

Si `/review` esta disponible:

```text
/review sync_incidents.py
```

Si `/review` no esta disponible:

```text
Revisa sync_incidents.py como si fuera una revision de codigo.
Busco hallazgos concretos sobre validacion, claridad operativa y riesgos visibles.
No me des consejos genericos.
```

## Paso 10. Aplicar una sola correccion final

Elegir solo un hallazgo razonable de la revision y corregirlo.

Luego volver a ejecutar:

En `bash` o `zsh`:

```bash
python3 sync_incidents.py --input sample_incidents.json --output incident_sync_output.json
python3 validate_sync.py incident_sync_output.json
```

En `PowerShell`:

```powershell
python sync_incidents.py --input sample_incidents.json --output incident_sync_output.json
python validate_sync.py incident_sync_output.json
```

## Entregables

- `sync_incidents.py` modificado
- `incident_sync_output.json`
- salida valida segun `validate_sync.py`
- una correccion final aplicada despues de la revision
