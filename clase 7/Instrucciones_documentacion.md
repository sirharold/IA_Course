# Instrucciones para generar documentacion con Copilot

## Importante

Los prompts de este documento son solo ejemplos base.

No deben copiarse de forma literal sin cambios.

Cada alumno debe modificarlos segun:

- el producto que quiere crear;
- el tipo de usuario al que apunta;
- el problema que quiere resolver;
- el contexto tecnico de su proyecto;
- las restricciones reales de su trabajo.

La idea no es pedirle a Copilot "cualquier documento".

La idea es pedirle documentos utiles para pensar mejor el producto antes de construirlo.

## Documento 1: problema, usuarios y requerimientos

### Prompt base

```text
Quiero crear un producto/proyecto llamado [NOMBRE DEL PROYECTO].

Su objetivo principal es: [OBJETIVO].

El problema que quiero resolver es: [PROBLEMA].

Los usuarios principales seran: [TIPO DE USUARIOS].

Ayudame a crear un documento inicial que incluya:

1. descripcion del problema u oportunidad;
2. objetivo del producto;
3. alcance inicial;
4. que queda fuera de alcance;
5. usuarios principales;
6. casos de uso principales;
7. requerimientos funcionales;
8. requerimientos no funcionales.

Escribe el documento en formato claro, con titulos y secciones. Si faltan datos, indica explicitamente que son supuestos.
```

### Lo que el alumno debe adaptar

- nombre del proyecto;
- objetivo real;
- problema concreto;
- usuarios reales;
- si es un producto interno, externo, web, automatizacion, API, etc.

## Documento 2: solucion, arquitectura y plan tecnico

### Prompt base

```text
Ya tengo un documento previo de problema, usuarios y requerimientos para mi proyecto [NOMBRE DEL PROYECTO].

Voy a pegar ese documento a continuacion y quiero que lo uses como base principal:

[PEGAR AQUI EL DOCUMENTO 1]

Tomando ese documento como referencia, ayudame a crear un segundo documento tecnico que incluya:

1. propuesta de solucion;
2. arquitectura general;
3. componentes principales;
4. integraciones necesarias;
5. datos que se usaran o generaran;
6. decisiones tecnicas relevantes;
7. pasos tecnicos de implementacion;
8. riesgos tecnicos;
9. dependencias o prerequisitos.

Si hay mas de una opcion tecnica posible, mencionala brevemente y explica cual recomendarias como punto de partida.
```

### Lo que el alumno debe adaptar

- pegar realmente el documento 1;
- agregar restricciones tecnicas propias si faltan;
- aclarar si ya existe un sistema previo;
- aclarar si hay integraciones obligatorias;
- aclarar si el proyecto debe correr en una nube, sistema interno o entorno especifico.

## Documento 3: backlog, validacion y salida

### Prompt base

```text
Ya tengo dos documentos previos para mi proyecto [NOMBRE DEL PROYECTO]:

1. un documento de problema, usuarios y requerimientos;
2. un documento de solucion, arquitectura y plan tecnico.

Voy a pegarlos a continuacion y quiero que los uses como base:

[PEGAR AQUI EL DOCUMENTO 1]

[PEGAR AQUI EL DOCUMENTO 2]

Tomando ambos documentos como referencia, ayudame a crear un documento de ejecucion que incluya:

1. backlog inicial priorizado;
2. epicas o bloques principales de trabajo;
3. tareas iniciales recomendadas;
4. criterios de aceptacion para los entregables principales;
5. plan de validacion o pruebas;
6. riesgos de salida a produccion;
7. plan inicial de despliegue;
8. como deberia medirse el exito del producto.

Organiza el resultado de forma clara y practica, pensando en que este documento me sirva para empezar a trabajar con un equipo tecnico.
```

### Lo que el alumno debe adaptar

- pegar realmente el documento 1 y el documento 2;
- tipo de entregables reales;
- forma de trabajo esperada;
- prioridad real del backlog;
- entorno de despliegue;
- metricas o resultados esperados.

## Recomendacion de uso en clase

1. Elegir uno de los tres documentos.
2. Adaptar el prompt al proyecto real del alumno.
3. Pedir una primera version a Copilot.
4. Revisar criticamente el resultado.
5. Volver a pedir una segunda version mejorada.

## Criterio importante

Si el alumno no adapta el prompt a su proyecto, el resultado sera demasiado generico.

El valor del ejercicio no esta en "generar mucho texto".

El valor esta en obtener documentacion util para tomar mejores decisiones antes de construir.
