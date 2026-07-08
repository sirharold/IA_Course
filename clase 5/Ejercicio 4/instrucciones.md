# Ejercicio 4 - Gemini

## Objetivo

Preparar una llamada programatica a Gemini para transformar texto tecnico en salida estructurada.

## Archivo principal

- `ejercicio4_gemini.py`

## Lo que deben hacer

- obtener una API key de Gemini;
- guardarla en la variable de entorno `GEMINI_API_KEY`;
- revisar la estructura del cliente;
- completar variables de entorno;
- ajustar el prompt;
- ejecutar la llamada si cuentan con credenciales;
- si no tienen credenciales, dejar el script listo y explicar que faltaria.

## Variables esperadas

- `GEMINI_API_KEY`
- `GEMINI_MODEL`

## Paso a paso para obtener la API key

1. Abrir [Google AI Studio API Keys](https://aistudio.google.com/app/apikey).
2. Iniciar sesion con la cuenta que usaran para el ejercicio.
3. Crear una API key nueva si no tienen una disponible.
4. Copiar la API key.
5. Volver a la terminal del ejercicio.
6. Exportar la variable de entorno:

```bash
export GEMINI_API_KEY='pega_aqui_tu_api_key'
```

7. Verificar que quedo disponible:

```bash
echo $GEMINI_API_KEY
```

## Paso a paso para elegir el modelo

1. Entrar en modo ASK.
2. Pedir a Copilot que sugiera modelos Gemini razonables para este caso.
3. Elegir uno y exportarlo en la terminal:

```bash
export GEMINI_MODEL='gemini-3.5-flash'
```

4. Si quieren comparar otro modelo, cambiar el valor y volver a ejecutar el script.

## Prompt sugerido para Copilot en modo ASK

```text
Estoy trabajando en un cliente Python para Gemini.
Antes de modificar el codigo, ayudame a decidir que modelo probar.
Necesito que me sugieras 2 o 3 modelos Gemini adecuados para:
1. extraer campos estructurados desde texto tecnico;
2. obtener respuestas breves y consistentes;
3. mantener bajo costo y baja complejidad.

Explica diferencias practicas y propone cual probar primero.
```

## Prompt sugerido para Copilot en modo Agent

```text
Revisa este cliente de Gemini.
Quiero mejorar el payload para pedir una salida JSON con system, severity, symptom y next_step.
Agrega una validacion pequena de la respuesta sin cambiar demasiado el script.
```

## Paso adicional del ejercicio

- Ejecutar el script con un modelo.
- Cambiar `GEMINI_MODEL`.
- Ejecutarlo de nuevo.
- Comparar si cambia:
  - el nivel de detalle;
  - el cumplimiento del formato;
  - la utilidad de la salida.
