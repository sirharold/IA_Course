# Clase 8 Laboratorio 4 - Acceso a Gmail desde Copilot con MCP

## Objetivo

Conectar GitHub Copilot en Visual Studio Code con Gmail usando el MCP remoto oficial de Gmail para que el agente pueda:

- buscar correos;
- resumir correos o hilos;
- listar etiquetas;
- responder preguntas sobre correos recibidos;
- hacer estadisticas simples sobre el correo;
- crear borradores de respuesta o seguimiento.

## Duracion sugerida

- 20 minutos para la configuracion de Google Cloud.
- 15 minutos para configurar el servidor MCP en VS Code.
- 20 minutos para autenticar y probar consultas.
- 10 minutos para revision y cierre.

## Modalidad

- Profesor guiando el paso a paso en vivo.
- Alumnos replicando el mismo flujo en sus equipos.
- Individual.

## Requisitos

- Visual Studio Code con GitHub Copilot activo.
- Acceso al Chat de Copilot.
- Una cuenta de Google con Gmail habilitado.
- Acceso a Google Cloud Console.
- Conexion a internet.

## Advertencia de privacidad

Este laboratorio da acceso al correo del alumno a un agente a traves de OAuth.

Antes de empezar:

1. Recomendar usar una cuenta de Gmail de pruebas o secundaria.
2. No usar una cuenta con informacion sensible si no es necesario.
3. No usar una cuenta corporativa si la politica de la empresa no lo permite.

## Costo para el alumno

Para uso normal de laboratorio, el costo esperado es bajo o nulo.

Puntos importantes:

- Google indica que el uso estandar de Gmail API esta disponible sin costo adicional.
- Google tambien indica que exceder los limites de cuota tiene previsto generar cargos al billing account mas adelante en 2026.
- Crear el proyecto, la pantalla de consentimiento OAuth y el client ID no deberia generar costo por si solo.
- Si el alumno activa billing en Google Cloud, no deberia tener cobros por un laboratorio pequeno de lectura y busqueda de correo, pero el riesgo no es literalmente cero.
- Si el alumno usa otros servicios pagos de Google Cloud fuera de este laboratorio, eso si puede generar costo.

## Fuentes base de este laboratorio

- Google Developers: [Configure the Gmail MCP server](https://developers.google.com/workspace/gmail/api/guides/configure-mcp-server)
- Google Developers: [MCP Reference: gmailmcp.googleapis.com](https://developers.google.com/workspace/gmail/api/reference/mcp)
- Google Cloud: [Configure MCP in an AI application](https://docs.cloud.google.com/mcp/configure-mcp-ai-application)
- VS Code Docs: [Add and manage MCP servers in VS Code](https://code.visualstudio.com/docs/agent-customization/mcp-servers)
- Google Developers: [Usage limits | Gmail API](https://developers.google.com/workspace/gmail/api/reference/quota)

## Resultado esperado

Al finalizar, cada alumno deberia tener:

- un proyecto de Google Cloud listo para OAuth;
- un servidor MCP de Gmail agregado en VS Code;
- autenticacion completada contra Gmail;
- al menos 5 consultas exitosas sobre su correo;
- una nota corta de riesgos, limites y cuidados.

## Parte 1. Crear o seleccionar un proyecto en Google Cloud

1. Ir a [Google Cloud Console](https://console.cloud.google.com/).
2. Crear un proyecto nuevo o seleccionar uno existente.
3. Anotar el nombre del proyecto.

### Recomendacion

Usar un proyecto exclusivo para esta clase, por ejemplo:

`curso-ia-copilot-gmail-lab`

## Parte 2. Habilitar Gmail API

1. Ir a [API Library](https://console.cloud.google.com/apis/library).
2. Buscar `Gmail API`.
3. Entrar a `Gmail API`.
4. Hacer click en `Enable`.

## Parte 3. Configurar la pantalla de consentimiento OAuth

1. Ir a `Google Auth Platform > Branding`.
2. Completar los campos minimos que pida Google.
3. Guardar.

### Nombre sugerido de la app

`Curso IA Copilot Gmail Lab`

### Correo de soporte

Usar el propio correo del alumno.

## Parte 4. Crear un OAuth Client ID

1. Ir a `Google Auth Platform > Clients`.
2. Hacer click en `Create Client`.
3. En `Application type`, elegir exactamente:

`Web application`

4. En `Name`, escribir por ejemplo:

`VS Code Gmail MCP Lab`

5. En `Authorized redirect URIs`, agregar el URI que usara el cliente.

### Importante

Este paso depende del cliente MCP.

Como en este laboratorio usaremos VS Code como cliente MCP general, primero se intentara autenticacion dinamica desde VS Code.

Si VS Code pide explicitamente `OAuth Client ID` y `OAuth Client Secret`, usar este cliente web.

Si el flujo de autenticacion de la extension o cliente que use el alumno muestra un callback especifico, usar ese callback exacto.

### Si necesitas un URI manual para probar

Antes de crear el cliente, revisar si VS Code o el proveedor de autenticacion muestra el callback esperado.

Si el profesor ya tiene un callback confirmado para su instalacion, todos los alumnos deben usar ese mismo callback durante la clase.

### Entregable de esta parte

Guardar:

- `Client ID`
- `Client Secret`

## Parte 5. Agregar el servidor MCP de Gmail en VS Code

1. Abrir Visual Studio Code.
2. Abrir la paleta de comandos.
3. Ejecutar:

`MCP: Add Server`

4. Elegir:

`HTTP (HTTP or server-sent events)`

5. Cuando pida la URL del servidor MCP, escribir exactamente:

```text
https://gmailmcp.googleapis.com/mcp/v1
```

6. Cuando pida el nombre del servidor, escribir exactamente:

```text
gmail
```

7. Cuando pregunte donde guardarlo, elegir:

`Workspace`

### Que deberia ocurrir

VS Code actualiza el `mcp.json` del workspace con el servidor `gmail`.

## Parte 6. Preparar Copilot para usar el servidor MCP

1. Abrir el Chat de Copilot.
2. En el chat, seleccionar:

`Set agent -> Agent`

3. Verificar que el servidor MCP `gmail` este habilitado.

Si no aparece:

1. Ir al panel de MCP servers.
2. Confirmar que `gmail` esta `Enabled`.
3. Reiniciar el chat o VS Code si hace falta.

## Parte 7. Autenticacion desde VS Code

La primera vez que el agente intente usar una tool del servidor `gmail`, VS Code deberia pedir autenticacion.

### Paso a paso

1. En el chat de Copilot, enviar este prompt:

```text
Lista las tools disponibles del servidor MCP gmail.
```

2. Cuando VS Code pida autenticacion, elegir el flujo de OAuth.
3. Si VS Code solicita `OAuth Client ID`, pegar el `Client ID` creado en Google Cloud.
4. Si VS Code solicita `OAuth Client Secret`, pegar el `Client Secret`.
5. En la ventana del navegador, iniciar sesion con la cuenta de Gmail elegida para el laboratorio.
6. Revisar los permisos que pide Google.
7. Hacer click en `Allow` si el alumno decide continuar.

### Si VS Code no toma nuevas credenciales

1. Abrir la paleta de comandos.
2. Ejecutar:

`Authentication: Remove dynamic authentication providers`

3. Seleccionar el client ID anterior.
4. Recargar VS Code.
5. Intentar otra vez.

## Parte 8. Verificar que el acceso a Gmail funciona

Ejecutar estas pruebas, una por una.

### Prueba 1

```text
Usa el servidor MCP gmail para listar las etiquetas disponibles en mi cuenta.
```

### Prueba 2

```text
Busca hilos de correo recibidos en los ultimos 7 dias con la palabra "factura".
```

### Prueba 3

```text
Resume en 5 lineas el hilo mas reciente que coincida con la palabra "reunion".
```

### Prueba 4

```text
Dime cuantos hilos relacionados con "curso" o "clase" aparecen en mi correo reciente.
```

### Prueba 5

```text
Indica que remitentes aparecen con mas frecuencia en los resultados de busqueda de "pago" durante los ultimos 30 dias.
```

## Parte 9. Consultas sugeridas para analisis y estadisticas

Estas consultas estan pensadas para hacer preguntas utiles sin modificar el correo.

### Busquedas

```text
Busca hilos con la palabra "contrato" y ordenalos del mas reciente al mas antiguo.
```

```text
Busca correos no leidos de la ultima semana relacionados con "soporte".
```

```text
Busca correos enviados por una misma persona y dame un resumen breve por hilo.
```

### Resumenes

```text
Resume los 3 hilos mas recientes relacionados con "proyecto".
```

```text
Explica en formato breve que acciones pendientes aparecen en estos hilos recientes sobre "reunion".
```

### Estadisticas

```text
Calcula cuantas conversaciones relacionadas con "factura" llegaron en los ultimos 30 dias.
```

```text
Agrupa por remitente los resultados de la busqueda "pago" y dime quienes aparecen mas veces.
```

```text
Dime cuantas etiquetas diferentes aparecen en los hilos encontrados para "curso".
```

## Parte 10. Crear un borrador

El servidor Gmail MCP documenta `create_draft`.

Probar con:

```text
Crea un borrador de correo para pedir una reunion de 20 minutos manana por la tarde. No lo envies.
```

### Validacion

1. Abrir Gmail en el navegador.
2. Ir a `Drafts`.
3. Confirmar que el borrador existe.

## Parte 11. Como probar que el laboratorio quedo bien

El laboratorio queda bien si se cumple todo esto:

1. El servidor `gmail` aparece en VS Code y esta habilitado.
2. El alumno pudo autenticarse con OAuth.
3. Copilot pudo usar al menos una tool de Gmail MCP con exito.
4. El alumno pudo hacer:
   - una busqueda;
   - un resumen;
   - una estadistica simple;
   - y un borrador.
5. El alumno puede explicar que permisos concedio y que riesgo implica.

## Entregable final

Cada alumno debe dejar:

- nombre del proyecto de Google Cloud;
- confirmacion de que `gmail` aparece como servidor MCP activo;
- 3 prompts usados con resultados utiles;
- una estadistica simple obtenida desde el correo;
- confirmacion de si pudo o no crear un borrador;
- una nota breve con:
  - riesgo principal de privacidad;
  - si uso cuenta principal o secundaria;
  - si ve o no riesgo de costo.

## Cierre docente recomendado

Preguntar al grupo:

1. Que tan facil fue autenticar Gmail en VS Code.
2. Que preguntas sobre el correo fueron utiles.
3. Que no deberian delegar a un agente sobre su correo.
4. En que casos reales este acceso agregaria valor y en cuales no.
