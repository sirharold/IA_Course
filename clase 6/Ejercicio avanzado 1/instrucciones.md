# Ejercicio avanzado 1 - Automatizacion no interactiva con `copilot -p`

## Objetivo

Usar GitHub Copilot CLI en modo no interactivo para:

1. entender un script existente;
2. generar una propuesta de mejora desde terminal;
3. modificar el script;
4. ejecutar una validacion simple;
5. dejar un reporte en Markdown generado por el script.

## Archivos del ejercicio

- `build_status_report.py`
- `sample_tickets.json`

## Resultado esperado

Al final del ejercicio, el script debe:

- leer `sample_tickets.json`;
- generar un archivo `daily_status_report.md`;
- incluir conteo por severidad;
- listar solo tickets no resueltos;
- mostrar tickets abiertos sin owner asignado.

## Paso 1. Entrar a la carpeta del ejercicio

En `bash` o `zsh`:

```bash
cd "ruta/a/la/carpeta/clase 6/Ejercicio avanzado 1"
ls -la
```

En `PowerShell`:

```powershell
Set-Location "ruta\a\la\carpeta\clase 6\Ejercicio avanzado 1"
Get-ChildItem
```

## Paso 2. Revisar el comportamiento actual del script

En `bash` o `zsh`:

```bash
python3 build_status_report.py
```

En `PowerShell`:

```powershell
python build_status_report.py
```

Revisen la salida actual. No modifiquen nada todavia.

## Paso 3. Pedir un analisis no interactivo con `copilot -p`

Generen una nota tecnica en un archivo para no perder el resultado.

En `bash` o `zsh`:

```bash
copilot -p "Revisa build_status_report.py y sample_tickets.json. Explica que hace hoy el script, que le falta para generar un reporte operativo util y propone cambios pequenos para: 1) contar tickets por severidad, 2) listar solo tickets no resueltos, 3) identificar tickets abiertos sin owner, 4) escribir la salida en daily_status_report.md. Responde en espanol con pasos concretos." > plan_mejora.md
```

En `PowerShell`:

```powershell
copilot -p "Revisa build_status_report.py y sample_tickets.json. Explica que hace hoy el script, que le falta para generar un reporte operativo util y propone cambios pequenos para: 1) contar tickets por severidad, 2) listar solo tickets no resueltos, 3) identificar tickets abiertos sin owner, 4) escribir la salida en daily_status_report.md. Responde en espanol con pasos concretos." > plan_mejora.md
```

## Paso 4. Revisar la propuesta generada

Abrir `plan_mejora.md` y verificar que la propuesta no pida reescribir todo el archivo.

## Paso 5. Modificar `build_status_report.py`

Hagan exactamente estos cambios:

1. Mantener la lectura del JSON.
2. Agregar una seccion de conteo por severidad.
3. Filtrar los tickets no resueltos.
4. Detectar tickets abiertos sin owner.
5. Guardar el reporte en `daily_status_report.md`.
6. Imprimir en consola solo un resumen breve de la ejecucion.

## Paso 6. Ejecutar de nuevo el script

En `bash` o `zsh`:

```bash
python3 build_status_report.py
```

En `PowerShell`:

```powershell
python build_status_report.py
```

## Paso 7. Validar que el archivo fue generado

En `bash` o `zsh`:

```bash
ls -la daily_status_report.md
cat daily_status_report.md
```

En `PowerShell`:

```powershell
Get-Item .\daily_status_report.md
Get-Content .\daily_status_report.md
```

## Paso 8. Validacion final con `copilot -p`

En `bash` o `zsh`:

```bash
copilot -p "Revisa build_status_report.py y daily_status_report.md. Dime si se cumplen estos 4 puntos: conteo por severidad, solo tickets no resueltos, tickets abiertos sin owner, y escritura del reporte a archivo. Si falta algo, dilo en una lista corta." > validacion_final.md
```

En `PowerShell`:

```powershell
copilot -p "Revisa build_status_report.py y daily_status_report.md. Dime si se cumplen estos 4 puntos: conteo por severidad, solo tickets no resueltos, tickets abiertos sin owner, y escritura del reporte a archivo. Si falta algo, dilo en una lista corta." > validacion_final.md
```

## Entregables

- `build_status_report.py` modificado
- `daily_status_report.md`
- `plan_mejora.md`
- `validacion_final.md`
