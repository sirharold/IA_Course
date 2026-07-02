# Ejercicios adicionales - Clase 3

## Objetivo

Tener actividades cortas de 5 a 15 minutos para grupos que avancen rapido.

## Ejercicio 1. Del texto al diagrama

### Tarea

Tomar una explicacion en lenguaje natural de Copilot sobre `service.py` y convertirla en un diagrama Mermaid mas simple y preciso.

### Que observar

- si el alumno logra eliminar pasos inventados;
- si el diagrama queda mas claro que el texto original.

## Ejercicio 2. Dependencia mas fragil

### Tarea

Pedir a Copilot la dependencia mas fragil del sistema y luego dibujarla en el diagrama de dependencias usando una marca especial o comentario.

### Que observar

- si puede justificar por que es fragil;
- si conecta codigo y datos, no solo imports.

## Ejercicio 3. Warning sin stack trace

### Tarea

Usar `reconciliation_warning.log` para redactar una hipotesis de problema sin mirar primero el codigo y luego corregirla despues de leer `matcher.py`.

### Que observar

- cuanto cambia la hipotesis con evidencia adicional;
- si el alumno detecta el limite del log.

## Ejercicio 4. Mejor log faltante

### Tarea

Pedir a Copilot que proponga una mejora de observabilidad:

- que dato falta en el log;
- donde deberia registrarse;
- como ayudaria al triage.

### Que observar

- si la propuesta responde a una necesidad real;
- si no se transforma en una reescritura completa.

## Ejercicio 5. Prueba mas valiosa

### Tarea

Elegir una sola prueba que reduzca mas riesgo que las demas y justificarla en una frase.

### Que observar

- criterio tecnico;
- conexion con un riesgo real del repo.
