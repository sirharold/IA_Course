# Clase 8 Laboratorio 2 - Agente de Pruebas Incrementales

## Objetivo

Crear un agente especializado en generar pruebas pequenas y acumulativas a medida que se revisa o modifica codigo Python.

## Duracion sugerida

- 15 minutos para crear el agente.
- 20 minutos para generar el plan de pruebas.
- 15 minutos para crear y ejecutar pruebas.

## Modalidad

- Profesor guiando en vivo.
- Alumnos replicando paso a paso.
- Individual o en parejas.

## Requisitos

- Visual Studio Code o Visual Studio con GitHub Copilot habilitado.
- Acceso a Copilot Chat o Agent Mode.
- Python operativo en terminal.
- `pytest` disponible.

## Carpeta de trabajo

- `clase 4/codigo`

## Archivo principal

- `reconcile_transactions.py`

## Resultado esperado

Al finalizar, cada alumno o pareja deberia tener:

- un agente creado o configurado;
- una lista priorizada de pruebas sugeridas;
- un archivo de pruebas inicial;
- pruebas ejecutadas en terminal;
- un registro de que riesgo cubre cada prueba.

## Preparacion del docente

Antes de iniciar la clase:

1. Abrir la carpeta `clase 4/codigo`.
2. Ejecutar `reconcile_transactions.py`.
3. Verificar que existe la carpeta `output/`.
4. Confirmar que `pytest` esta disponible.
5. Si no existe la carpeta `tests/`, crearla antes del laboratorio.

## Parte 1. Validar el caso base

### Bash

```bash
cd "clase 4/codigo"
python3 reconcile_transactions.py
mkdir -p tests
```

### PowerShell

```powershell
Set-Location "clase 4\codigo"
python reconcile_transactions.py
New-Item -ItemType Directory -Force tests | Out-Null
```

### Que deberia ocurrir

- El script deberia generar `output/reconciliation_report.json`.
- La carpeta `tests/` deberia existir al terminar este paso, aunque todavia no tenga archivos.

## Parte 2. Crear el agente

### Metodo de creacion para este laboratorio

Crear el agente desde el menu `Configure Custom Agents` del chat de Copilot.

### Nombre sugerido

- `Agente de Pruebas Incrementales`

### Como nombrar o invocar este agente

Seleccionar `Agente de Pruebas Incrementales` en el selector de agentes de Copilot.

Antes de enviar cada prompt, confirmar que ese agente sigue siendo el agente activo.

### Paso a paso de creacion

1. Abrir GitHub Copilot Chat.
2. En el selector de agentes o modos del chat, abrir la opcion `Configure Custom Agents`.
3. Elegir `Create new custom agent`.
4. Cuando Copilot pida el nombre, escribir exactamente: `Agente de Pruebas Incrementales`.
5. Si Copilot muestra el campo `Describe the trigger scenario or type of request that should use this agent`, escribir exactamente:

```text
Use this agent when the request is about proposing, prioritizing, or writing small tests for Python code as it evolves, especially when the goal is to cover visible behavior with incremental validation.
```

6. Si Copilot muestra el paso `Where should this agent be saved`, seleccionar exactamente:

```text
Workspace (.github/agents/) Project specific, shared with team
```

7. Si Copilot muestra el paso `Which tool categories should this agent use?`, seleccionar exactamente:

```text
read&edit
```

8. Si Copilot muestra un campo de descripcion corta, escribir exactamente:

```text
Proposes and writes small, prioritized, incremental tests for evolving Python code.
```

9. Pegar las instrucciones base del agente.
10. Guardar el archivo del agente si Copilot abre un archivo `.agent.md`.

En este laboratorio no hace falta usar `Configure tool...` para habilitar `runSubagent`.

### Descripcion sugerida

- Lee codigo Python y propone pruebas pequenas, priorizadas y trazables sin asumir comportamiento que no este visible.

### Instrucciones base del agente

Copiar y pegar este bloque en la configuracion del agente:

```text
## Constraints
- No inventar reglas de negocio no visibles en el codigo.
- No generar una bateria grande de pruebas en la primera ronda.
- No cambiar el codigo de produccion salvo que se pida explicitamente.
- Si una prueba depende de una suposicion no verificada, debes marcarlo.

## Approach
1. Leer el codigo antes de proponer pruebas.
2. Detectar funciones con mayor riesgo o mayor valor para probar.
3. Proponer primero una lista priorizada de pruebas.
4. Escribir solo pruebas pequenas y acotadas.
5. Priorizar casos base, edge cases y errores.
6. Explicar que riesgo cubre cada prueba.

## Output
Entregar siempre:
- lista priorizada de pruebas;
- riesgo cubierto por cada prueba;
- funciones o areas que quedan fuera de la primera ronda;
- si se solicita codigo, un archivo de pruebas pequeno y claro.
```

## Parte 3. Primera ejecucion del agente

Abrir `reconcile_transactions.py` y enviar este prompt con `Agente de Pruebas Incrementales` activo:

```text
Revisa este archivo y propone un plan de pruebas incrementales.

Necesito:
1. Las 5 pruebas mas valiosas para empezar.
2. El riesgo cubierto por cada una.
3. Que funciones deberian quedar fuera en esta primera ronda.

No escribas aun el archivo de pruebas.
```

## Parte 4. Elegir el primer lote de pruebas

Tomar solo las primeras 3 pruebas sugeridas por el agente.

Pedir despues, manteniendo activo `Agente de Pruebas Incrementales`:

```text
Ahora escribe solo las primeras 3 pruebas.

Condiciones:
1. Crea un archivo de pruebas pequeno y claro.
2. Usa nombres descriptivos.
3. No agregues mas de 3 pruebas en esta ronda.
4. Explica en un comentario corto que cubre cada prueba si no es obvio.
```

## Parte 5. Crear el archivo de pruebas

Usar Copilot para crear un archivo nuevo:

- `tests/test_reconcile_transactions.py`

Si el agente propone otro nombre valido y consistente, se puede usar, pero todo el curso deberia usar el mismo nombre durante la clase.

## Parte 6. Ejecutar las pruebas

### Bash

```bash
python3 -m pytest tests/test_reconcile_transactions.py -q
```

### PowerShell

```powershell
python -m pytest tests/test_reconcile_transactions.py -q
```

### Si una prueba falla

No corregir a ciegas.

Pedir al agente, manteniendo activo `Agente de Pruebas Incrementales`:

```text
Una o mas pruebas fallaron.

Necesito que:
1. Expliques por que fallan.
2. Digas si el problema esta en la prueba o en el codigo.
3. Propongas un ajuste pequeno.
4. No reescribas todo el archivo.
```

## Parte 7. Simular una segunda iteracion

Una vez que el primer lote pase, pedir al agente una segunda ronda con `Agente de Pruebas Incrementales` activo:

```text
Asume que el codigo seguira evolucionando.

Propon ahora:
1. Dos pruebas adicionales que agregaria en la siguiente iteracion.
2. Que cambio o riesgo futuro las justificaria.
3. Cual dejarias para mas adelante y por que.
```

## Parte 8. Como probar que el trabajo quedo bien

El laboratorio queda bien si se cumple todo esto:

1. El agente priorizo pruebas en vez de generar una bateria gigante.
2. Cada prueba cubre un comportamiento visible del codigo.
3. Las pruebas corren en terminal.
4. El alumno puede decir que riesgo cubre cada prueba.
5. Queda claro que pruebas se dejan para una segunda iteracion.

## Entregable final

Cada alumno o pareja debe dejar:

- nombre del agente creado;
- lista priorizada inicial de pruebas;
- archivo `tests/test_reconcile_transactions.py`;
- resultado de ejecucion en terminal;
- nota breve con:
  - riesgo cubierto por cada prueba;
  - siguiente prueba que agregarian en otra iteracion.

## Extension opcional

Si el grupo avanza rapido, pedir una variante sobre una funcion puntual:

```text
Concentrate solo en estas funciones:
- normalize_text
- parse_amount
- classify_status_mismatch

Quiero una matriz corta:
1. caso base;
2. edge case;
3. error esperado.
```
