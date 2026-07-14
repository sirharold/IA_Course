# Ejercicio 7 - Usar Copilot CLI dentro de un script

## Objetivo

Ejecutar un script en Python que use GitHub Copilot CLI en modo no interactivo para leer una nota tecnica y generar un resumen estructurado en Markdown.

## Archivos del ejercicio

- `copilot_cli_summary.py`
- `incident_note.txt`

## Resultado esperado

Al final del ejercicio, el script debe:

- leer `incident_note.txt`;
- invocar `copilot -p`;
- generar `incident_summary.md`;
- dejar una salida util para revisar desde terminal.

## Paso 1. Entrar a la carpeta del ejercicio

En `bash` o `zsh`:

```bash
cd "ruta/a/la/carpeta/clase 6/Ejercicio 7"
ls -la
```

En `PowerShell`:

```powershell
Set-Location "ruta\a\la\carpeta\clase 6\Ejercicio 7"
Get-ChildItem
```

## Paso 2. Verificar que Copilot CLI esta disponible

En `bash` o `zsh`:

```bash
copilot --help | head
```

En `PowerShell`:

```powershell
copilot --help
```

Si no esta autenticado, ejecutar login antes de seguir.

En `bash` o `zsh`:

```bash
copilot login
```

En `PowerShell`:

```powershell
copilot login
```

## Paso 3. Revisar el script antes de ejecutarlo

Abrir `copilot_cli_summary.py` y confirmar:

1. que archivo lee;
2. como arma el prompt;
3. donde invoca `copilot -p`;
4. que archivo de salida genera.

## Paso 4. Ejecutar el script

En `bash` o `zsh`:

```bash
python3 copilot_cli_summary.py
```

En `PowerShell`:

```powershell
python copilot_cli_summary.py
```

## Paso 5. Revisar la salida generada

En `bash` o `zsh`:

```bash
ls -la incident_summary.md
cat incident_summary.md
```

En `PowerShell`:

```powershell
Get-Item .\incident_summary.md
Get-Content .\incident_summary.md
```

## Paso 6. Mejorar una sola parte del script

Hagan exactamente una mejora pequena. Elegir solo una:

- cambiar el prompt para que pida una salida mas clara;
- cambiar el nombre del archivo de salida usando `--output`;
- mejorar el mensaje de error si falla la llamada a `copilot`;
- agregar validacion para que no acepte un archivo vacio.

## Paso 7. Volver a ejecutar y comparar

En `bash` o `zsh`:

```bash
python3 copilot_cli_summary.py
cat incident_summary.md
```

En `PowerShell`:

```powershell
python copilot_cli_summary.py
Get-Content .\incident_summary.md
```

## Entregables

- `copilot_cli_summary.py` modificado o al menos entendido y ejecutado;
- `incident_summary.md`;
- una explicacion corta de que parte hizo el script y que parte hizo Copilot CLI.
