# Ejercicios - Clase 6

## Objetivo general

Practicar GitHub Copilot CLI como apoyo para operar, explicar, validar y mejorar flujos tecnicos desde terminal, partiendo por acceso basico al CLI y avanzando hacia una operacion mas repetible del proyecto aplicado.

## Regla comun para todos los ejercicios

Antes de ejecutar comandos o aceptar cambios, cada alumno o pareja debe dejar claro:

- que quiere lograr con el comando o flujo;
- que archivos, carpetas o scripts podrian verse afectados;
- que validacion hara antes o despues de ejecutar;
- que parte esta usando Copilot CLI y que parte sigue siendo criterio humano.

## Regla comun para el uso de Copilot CLI

No usar Copilot CLI solo para "pedir comandos". Usarlo para:

- explicar que hace un comando antes de correrlo;
- proponer una variante mas segura o mas clara;
- ayudar a ubicar archivos y scripts relevantes;
- refinar pequenos cambios en scripts existentes;
- dejar una forma de ejecucion mas repetible y entendible.

## Como entrar a GitHub Copilot CLI

Usen estas instrucciones en el ejercicio 1 y reutilicen el mismo patron en el resto de la clase.

### Opcion interactiva recomendada

1. Abrir una terminal.
2. Ir al directorio de trabajo del ejercicio o proyecto. Por ejemplo, a la carpeta de la clase correspondiente.

En `bash` o `zsh`:

```bash
cd "ruta/a/la/carpeta/de/la/clase"
```

En `PowerShell`:

```powershell
Set-Location "ruta\\a\\la\\carpeta\\de\\la\\clase"
```

3. Iniciar Copilot CLI:

En `bash`, `zsh` o `PowerShell`:

```bash
copilot
```

4. Si es la primera vez, autenticarse dentro del CLI con:

```text
/login
```

5. Seguir el flujo de autenticacion en navegador.
6. Cuando el CLI pregunte si confian en el directorio actual, leer antes de aprobar.
7. Si necesitan ver comandos disponibles, usar:

```text
/help
```

### Opcion alternativa desde terminal

Si prefieren autenticar antes de entrar al modo interactivo:

En `bash` o `zsh`:

```bash
copilot login
copilot
```

En `PowerShell`:

```powershell
copilot login
copilot
```

## Ejercicio 1. Entrar al CLI y pedir una explicacion segura

### Objetivo

Entrar correctamente a GitHub Copilot CLI, autenticar si hace falta y usarlo para explicar un comando simple antes de ejecutarlo.

### Carpeta de trabajo

- `clase 6`

### Lo que deben hacer

- abrir terminal;
- entrar a la carpeta de la clase;
- iniciar GitHub Copilot CLI;
- autenticarse si hace falta;
- pedirle que explique un comando simple de inspeccion del entorno;
- ejecutar solo despues de entender que hace.

### Comando sugerido para revisar

- `pwd`
- `ls -la`

### Prompt sugerido para Copilot CLI

```text
Explicame que hace `ls -la` en esta carpeta, que tipo de informacion me mostrara y por que seria util antes de trabajar con archivos del proyecto.
```

### Entregable esperado

- evidencia de que pudieron entrar al CLI;
- una explicacion clara de al menos un comando simple;
- una salida real de terminal revisada por ustedes.

### Validacion minima

- confirmar que estan en la carpeta correcta;
- distinguir entre "explicar" y "ejecutar";
- no aprobar nada que no entiendan.

## Ejercicio 2. Entender y ejecutar un script ya existente desde terminal

### Objetivo

Tomar un script de la clase 5, pedir a Copilot CLI que lo explique y ejecutarlo con una validacion minima.

### Archivo sugerido

- `../clase 5/Ejercicio 1/ejercicio1_http.py`

### Lo que deben hacer

- entrar a la carpeta del ejercicio;
- listar archivos desde terminal;
- pedir a Copilot CLI que explique rapidamente que hace el script;
- ejecutar el script;
- revisar si la salida coincide con la intencion del ejercicio.

### Prompt sugerido para Copilot CLI

```text
Revisa este directorio y ayudame a entender que hace `ejercicio1_http.py`.
Quiero un resumen corto de:
1. entrada del script;
2. llamadas que realiza;
3. salida esperada;
4. que deberia validar yo despues de ejecutarlo.
```

### Entregable esperado

- ejecucion del script desde terminal;
- resumen del flujo entregado por Copilot CLI y revisado por ustedes;
- una nota corta sobre si la salida fue la esperada o no.

### Validacion minima

- confirmar que el script corre sin editarlo primero;
- confirmar que la salida no es solo ruido;
- identificar al menos un dato importante de la salida.

## Ejercicio 3. Buscar informacion util del proyecto sin abrir todo manualmente

### Objetivo

Usar Copilot CLI para localizar archivos, scripts, variables o endpoints relevantes sin recorrer el proyecto a ciegas.

### Carpetas sugeridas

- `../clase 5/Ejercicio 3`
- `../clase 5/mock_api`

### Lo que deben hacer

- ubicar donde se usa `DEMO_API_KEY`;
- ubicar el endpoint del mock relacionado con autenticacion;
- pedir a Copilot CLI un comando o secuencia segura para encontrar esa informacion;
- ejecutar la busqueda y revisar si los resultados tienen sentido.

### Prompt sugerido para Copilot CLI

```text
Necesito encontrar rapidamente en este proyecto:
1. donde se usa `DEMO_API_KEY`;
2. que archivo define el endpoint del mock;
3. que comando de terminal conviene usar para buscar esto sin modificar nada.
Propone una opcion segura y explicala antes de ejecutarla.
```

### Entregable esperado

- uno o dos comandos de busqueda explicados por Copilot CLI;
- ubicacion correcta de la variable y del endpoint;
- breve explicacion de por que esos archivos importan.

### Validacion minima

- no usar comandos que modifiquen archivos;
- confirmar que el resultado apunta al archivo correcto;
- explicar por que una busqueda textual sirve en este caso.

## Ejercicio 4. Operar un flujo con configuracion y validar antes y despues

### Objetivo

Ejecutar un flujo que depende de variable de entorno, con una validacion previa y otra posterior, usando Copilot CLI para ordenar la secuencia.

### Archivos sugeridos

- `../clase 5/Ejercicio 3/ejercicio3_auth.py`
- `../clase 5/mock_api/mock_service.py`

### Lo que deben hacer

- levantar el mock local si no esta levantado;
- exportar `DEMO_API_KEY`;
- pedir a Copilot CLI una secuencia de pasos segura para:
  - verificar salud del servicio;
  - ejecutar el script;
  - probar un escenario correcto y uno incorrecto;
- ejecutar la secuencia;
- registrar que validaron antes y despues.

### Prompt sugerido para Copilot CLI

```text
Necesito operar este ejercicio desde terminal sin mezclar todo en un solo paso.
Ayudame a definir una secuencia corta para:
1. verificar si el mock esta arriba;
2. exportar la variable de entorno correcta;
3. ejecutar el script;
4. probar un caso de error controlado;
5. validar que el resultado tiene sentido.
Propone pasos pequenos y seguros.
```

### Entregable esperado

- secuencia de ejecucion clara;
- corrida exitosa y corrida con error controlado;
- lista corta de validaciones previas y posteriores.

### Validacion minima

- confirmar que el mock responde antes de correr el cliente;
- no hardcodear la API key;
- diferenciar exito operativo de exito funcional.

## Ejercicio 5. Hacer una mejora pequena sobre un script usando Copilot CLI

### Objetivo

Usar Copilot CLI no solo para ejecutar, sino para proponer y aplicar una mejora pequena, visible y verificable sobre un script existente.

### Archivo sugerido

- `../clase 5/Ejercicio 7/ejercicio7_refactor.py`

### Lo que deben hacer

- pedir a Copilot CLI que revise el script;
- elegir una mejora pequena, por ejemplo:
  - separar mejor una funcion;
  - aclarar un mensaje de salida;
  - hacer configurable un endpoint;
  - agregar una validacion pequena;
- aplicar el cambio;
- volver a ejecutar y comparar antes y despues.

### Prompt sugerido para Copilot CLI

```text
Revisa este script Python y propon una mejora pequena y verificable.
Quiero elegir solo una de estas lineas:
1. separar mejor la validacion;
2. aclarar la salida;
3. hacer configurable un valor que hoy esta acoplado.
No reescribas todo.
Explica primero que cambiarias y por que.
```

### Entregable esperado

- cambio pequeno pero real en el script;
- explicacion de la mejora;
- nueva ejecucion o validacion posterior al cambio.

### Validacion minima

- el cambio debe ser facil de explicar;
- el comportamiento no debe romperse;
- debe quedar claro que problema mejora.

## Ejercicio 6. Dejar una operacion reproducible del flujo

### Objetivo

Cerrar la secuencia dejando una forma repetible de operar un flujo tecnico desde terminal, con instrucciones o script de apoyo que otra persona pueda reutilizar.

### Base sugerida

- cualquier ejercicio de la clase 5 que el alumno ya tenga funcionando;
- idealmente uno de estos:
  - `../clase 5/Ejercicio 3/ejercicio3_auth.py`
  - `../clase 5/Ejercicio 7/ejercicio7_refactor.py`
  - `../clase 5/Ejercicio avanzado 1/advanced_env_client.py`

### Lo que deben hacer

- elegir un flujo pequeno que ya funcione o casi funcione;
- pedir a Copilot CLI ayuda para dejar una operacion mas repetible;
- elegir una de estas salidas:
  - una mini guia de ejecucion;
  - una secuencia documentada de comandos;
  - un script de apoyo con parametros simples;
- incluir al menos:
  - prerequisitos;
  - comando principal;
  - validacion previa;
  - validacion posterior;
  - riesgo conocido.

### Prompt sugerido para Copilot CLI

```text
Quiero dejar este flujo en una forma mas repetible para otro desarrollador.
Ayudame a producir una salida pequena pero util, que puede ser:
1. una mini guia de ejecucion;
2. una secuencia clara de comandos;
3. un script de apoyo simple.
Debe incluir prerequisitos, paso principal, validacion antes y despues, y un riesgo conocido.
No agregues complejidad innecesaria.
```

### Entregable esperado

- una forma reproducible de operar el flujo;
- evidencia de al menos una corrida o validacion;
- una nota sobre que parte sigue siendo manual o fragil.

### Validacion minima

- otra persona deberia poder entender como correr el flujo;
- debe existir al menos un chequeo antes y uno despues;
- la salida debe ser mas operable que al inicio de la clase.

## Ruta sugerida de dificultad

1. Entrar al CLI y entender un comando simple.
2. Explicar y correr un script existente.
3. Buscar informacion util del proyecto desde terminal.
4. Operar un flujo con variables de entorno y validaciones.
5. Aplicar una mejora pequena sobre un script existente.
6. Dejar una operacion reproducible del flujo.

## Criterio docente

- si el tiempo es corto, llegar al menos hasta el ejercicio 4;
- si el grupo avanza bien, usar los ejercicios 5 y 6 para consolidar repetibilidad;
- privilegiar seguridad operativa y criterio humano por sobre cantidad de comandos;
- evitar ejercicios donde el CLI haga cambios grandes o dificiles de auditar;
- conectar siempre cada ejercicio con el flujo real que el alumno trae desde la clase 5.
