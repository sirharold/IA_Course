# Preparacion y demos de MCPs - Clase 7

Fecha de revision: 2026-07-15

## Objetivo de este documento

Este documento ya no esta pensado solo como preparacion tecnica.

Tambien sirve como guia de demo para la clase.

La idea es:

1. instalar un MCP;
2. comprobar que aparece activo;
3. ejecutar una prueba sin MCP;
4. ejecutar la misma prueba con MCP;
5. discutir si realmente hubo ganancia.

## Que es un MCP

MCP es una forma estandar de conectar Copilot con herramientas o fuentes externas.

No cambia solo la forma de responder. Cambia a que contexto o herramientas puede acceder el agente.

## Analogia

- si un skill ensena una forma de trabajar mejor;
- un MCP le da nuevos ojos y nuevas manos para interactuar con otros sistemas.

En simple:

- skill:
  - organiza una rutina.
- MCP:
  - abre una puerta hacia otra herramienta o fuente.

## MCPs que si vale la pena preparar para esta clase

### Minimo recomendado

1. GitHub MCP Server
2. Microsoft Learn MCP Server

### Recomendado para demo documental

3. MarkItDown MCP

### Opcional

4. DuckDB MCP

## Como leer los pasos de Visual Studio Code

- `Extensions`:
  - vista de extensiones de Visual Studio Code;
  - Windows: `Ctrl+Shift+X`;
  - macOS: `Cmd+Shift+X`.
- `Paleta de comandos`:
  - cuadro de acciones internas de Visual Studio Code;
  - Windows: `Ctrl+Shift+P`;
  - macOS: `Cmd+Shift+P`.
- `MCP: List Servers`:
  - abre la paleta de comandos;
  - escribe exactamente `MCP: List Servers`;
  - presiona `Enter`.

## 1. GitHub MCP Server

### Que hace este MCP

Este MCP conecta Copilot con GitHub como sistema real, no solo con el repo local abierto en el editor.

### Que herramientas o propiedades aporta

- acceso a issues y pull requests reales;
- lectura de metadata del repo;
- posibilidad de trabajar con contexto remoto y no solo con archivos locales;
- en algunos clientes, puede habilitar acciones sobre GitHub y no solo lectura.

### Instalacion recomendada

1. Abre Visual Studio Code.
2. Abre `Extensions`.
3. En la caja de busqueda, escribe:

```text
@mcp github
```

4. Busca `GitHub MCP server`.
5. Haz clic en `Install`.
6. Si Visual Studio Code pide confirmacion o confianza, aceptala.
7. Abre la paleta de comandos.
8. Ejecuta:

```text
MCP: List Servers
```

9. Verifica que aparezca un servidor relacionado con GitHub.

### Demo sugerida

#### Objetivo de la demo

Mostrar que GitHub MCP puede ser util para acceder a contexto real del repo, pero que en algunos clientes puede sentirse redundante si Copilot ya tiene muy buena integracion con GitHub.

#### Prueba sin MCP

1. Desactiva o deten temporalmente GitHub MCP.
2. En Copilot, escribe:

```text
Lista los issues abiertos del repo sirharold/IA_Course y resume el objetivo de cada uno.
```

3. Observa si responde igual o parecido a lo esperado.

#### Prueba con MCP

1. Activa GitHub MCP.
2. Repite el mismo prompt:

```text
Lista los issues abiertos del repo sirharold/IA_Course y resume el objetivo de cada uno.
```

3. Luego prueba un segundo prompt:

```text
Busca en los issues abiertos del repo sirharold/IA_Course cual habla de evidencia de uso real de MCP y explica por que.
```

#### Que observar

- Si no cambia mucho, eso tambien es un resultado valido.
- En tu entorno, GitHub MCP puede aportar poco si Copilot ya resuelve bien ese caso.
- Ese resultado sirve para enseñar que MCP no siempre agrega valor visible.

#### Mensaje docente

`GitHub MCP no siempre mejora una tarea si el cliente ya tiene una buena integracion nativa con GitHub.`

## 2. Microsoft Learn MCP Server

### Que hace este MCP

Este MCP conecta Copilot con la documentacion oficial de Microsoft Learn para consultar contenido vivo y actualizado.

### Que herramientas o propiedades aporta

- acceso a documentacion oficial actual;
- mejor trazabilidad de respuestas tecnicas;
- menos dependencia de memoria o conocimiento previo del modelo;
- utilidad especial cuando quieres distinguir entre una respuesta generica y una basada en fuente oficial.

### Instalacion recomendada

Importante:

- en pruebas reales de esta clase, buscar `@mcp learn` no siempre devolvio resultados;
- si funciono buscar `@mcp Microsoft` y luego ubicar `Microsoft Learn` en la lista.

Usa ese camino como metodo principal.

1. Abre Visual Studio Code.
2. Abre `Extensions`.
3. En la caja de busqueda, escribe:

```text
@mcp Microsoft
```

4. Dentro de la lista, busca `Microsoft Learn`.
5. Haz clic en `Install`.
6. Si Visual Studio Code lo pide, reinicia la ventana o la aplicacion.
7. Abre la paleta de comandos.
8. Ejecuta:

```text
MCP: List Servers
```

9. Verifica que aparezca `Microsoft Learn`.

### Si no aparece en Extensions

Usa configuracion manual:

1. Abre la paleta de comandos.
2. Ejecuta:

```text
MCP: Open User Configuration
```

3. Agrega esta configuracion:

```json
{
  "servers": {
    "microsoft-learn": {
      "type": "http",
      "url": "https://learn.microsoft.com/api/mcp"
    }
  }
}
```

4. Guarda.
5. Ejecuta `MCP: List Servers`.
6. Verifica que aparezca `microsoft-learn` o `Microsoft Learn`.

### Demo sugerida

#### Objetivo de la demo

Mostrar una diferencia mas visible que con GitHub MCP: acceso a documentacion oficial y actual, no solo respuesta generica.

#### Prueba sin MCP

1. Desactiva o desinstala temporalmente `Microsoft Learn MCP`.
2. En Copilot, escribe:

```text
Explica como se configuran custom instructions en GitHub Copilot y dame 3 buenas practicas recomendadas por la documentacion oficial. Si no estas seguro, dilo explicitamente.
```

3. Observa la respuesta.

#### Prueba con MCP

1. Activa `Microsoft Learn MCP`.
2. En Copilot, escribe:

```text
Usa Microsoft Learn MCP para buscar documentacion oficial sobre custom instructions en GitHub Copilot. Resume como se configuran y dame 3 buenas practicas, dejando claro que viene de documentacion oficial.
```

#### Que observar

- sin MCP, la respuesta puede ser razonable pero mas generica;
- con MCP, deberia estar mas enfocada en documentacion oficial;
- aqui la ganancia no es "mas inteligencia", sino "mejor trazabilidad y menos riesgo de inventar".

#### Mensaje docente

`Este MCP no hace mas inteligente al modelo. Le da acceso controlado a una fuente oficial y actualizada.`

## 3. MarkItDown MCP

### Que hace este MCP

Este MCP convierte documentos como PDF a Markdown u otros formatos de texto mas faciles de reutilizar como contexto.

### Que herramientas o propiedades aporta

- transformacion de documentos a texto estructurado;
- mejor reutilizacion del contenido en prompts o tareas posteriores;
- menos trabajo manual de copiar y pegar;
- utilidad especial cuando el insumo original esta en un formato poco amigable para el analisis.

### Instalacion base

1. Abre una terminal.
2. Ejecuta:

```bash
pip install markitdown-mcp
```

3. Prueba que el comando exista:

```bash
markitdown-mcp
```

4. Si el comando queda esperando y no termina de inmediato, el servidor esta disponible por `stdio`.
5. Sal de esa prueba con `Ctrl+C`.

### Configuracion manual tipica

Si tu cliente te pide configuracion manual, una forma tipica es:

```json
{
  "mcpServers": {
    "markitdown": {
      "command": "markitdown-mcp"
    }
  }
}
```

### Demo sugerida

#### Objetivo de la demo

Comparar texto copiado manualmente desde un PDF contra una conversion estructurada a Markdown.

#### Archivo sugerido

- [TEMARIO - IA Aplicada Al Desarrollo De Software Con GitHub Copilot..pdf](/Users/haroldgomez/Library/CloudStorage/GoogleDrive-haroldg@gmail.com/My%20Drive/Material%20propio/Curso%20IA%20Github%20Copilot/CursoIA/TEMARIO%20-%20IA%20Aplicada%20Al%20Desarrollo%20De%20Software%20Con%20GitHub%20Copilot..pdf)

#### Prueba sin MCP

1. Abre el PDF.
2. Copia manualmente un fragmento de 1 o 2 paginas.
3. En Copilot, escribe:

```text
Resume este contenido, lista 3 temas centrales y propone una estructura breve.
```

4. Usa como contexto solo el texto copiado manualmente.

#### Prueba con MCP

1. Activa MarkItDown MCP.
2. Pide convertir el mismo PDF a Markdown.
3. Luego pide exactamente la misma tarea:

```text
Resume este contenido, lista 3 temas centrales y propone una estructura breve.
```

4. Usa como contexto el Markdown generado.

#### Que observar

- el punto no es solo ahorrar tokens;
- el punto es si el contexto convertido queda mas ordenado, mas reusable y mas facil de volver a usar;
- este es un mejor ejemplo de valor de MCP que un caso donde el cliente ya resolvia casi todo.

#### Mensaje docente

`Aqui el MCP agrega valor porque transforma el insumo antes de que el modelo trabaje con el.`

## 4. DuckDB MCP

### Que hace este MCP

Este MCP conecta Copilot con una herramienta de consulta tabular para trabajar mejor con CSVs y datos estructurados.

### Que herramientas o propiedades aporta

- consultas mas precisas sobre tablas o archivos CSV;
- agrupaciones, filtros y conteos sin inspeccion manual;
- mejor soporte para preguntas de datos que a ojo son poco confiables;
- utilidad especial cuando hace falta responder con mas precision que un resumen libre.

### Recomendacion

Dejalo como opcional.

No lo conviertas en requisito de clase 7 si no lo probaste antes en tu mismo entorno.

### Demo posible

#### Objetivo de la demo

Mostrar que un MCP de datos puede responder preguntas tabulares con mas precision que inspeccionar un CSV a ojo.

#### Prueba sin MCP

```text
Revisa este CSV y dime cuantos registros criticos hay y que patrones ves.
```

#### Prueba con MCP

```text
Usa el MCP de DuckDB para consultar este CSV y dime cuantos registros criticos hay, agrupados por categoria.
```

#### Mensaje docente

`El valor de un MCP de datos aparece cuando hace falta consultar, agrupar o filtrar con precision.`

## Checklist minimo antes de la clase

1. GitHub MCP aparece en `MCP: List Servers`.
2. Microsoft Learn MCP aparece en `MCP: List Servers`.
3. MarkItDown MCP responde desde terminal si lo vas a usar.
4. Ya probaste al menos una demo sin MCP y con MCP para cada servidor que mostraras.
5. Tienes un plan B si un MCP falla.

## Plan B rapido

- Si falla GitHub MCP:
  - usa esa falla como argumento de que el caso igual puede no mostrar mucha ganancia visible.
- Si falla Microsoft Learn MCP:
  - usa navegador con documentacion oficial y muestra la diferencia igual, aunque sea manual.
- Si falla MarkItDown MCP:
  - deja la demo en comparacion conceptual o usa un Markdown ya preparado.

## Recomendacion final para clase 7

Si quieres una clase estable y con señal clara:

1. usa GitHub MCP como ejemplo de caso donde la ganancia puede ser baja o discutible;
2. usa Microsoft Learn MCP como ejemplo de fuente oficial viva;
3. usa MarkItDown MCP como ejemplo de transformacion util del contexto.
