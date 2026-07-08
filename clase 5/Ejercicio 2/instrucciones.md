# Ejercicio 2 - API publica y salida util

## Objetivo

Consumir una API publica real y convertir la respuesta en una salida breve y usable, usando primero Copilot en modo ASK para investigar el contexto y luego en modo Agent para ajustar el codigo.

## Archivo principal

- `ejercicio2_meteo.py`

## API usada

- Open-Meteo

## Lo que deben hacer

- partir en modo ASK;
- averiguar cual es el proximo partido del Mundial y en que sede se jugara;
- identificar la ciudad o coordenadas aproximadas de esa sede;
- volver al modo Agent;
- ajustar el script para consultar el pronostico de esa ubicacion;
- cambiar coordenadas, variables y hora o tramo horario si hace falta;
- dejar una salida resumida en consola;
- agregar una validacion pequena.

## Prompt sugerido para Copilot en modo ASK

```text
Estoy trabajando en un ejercicio de Python con Open-Meteo.
Necesito que primero investigues:
1. cual es el proximo partido del Mundial;
2. en que ciudad o estadio se juega;
3. que coordenadas aproximadas deberia usar para consultar el clima;
4. que fecha y hora local son relevantes para mirar el pronostico.

No escribas todavia el codigo final.
Primero dame solo la informacion necesaria para parametrizar la consulta.
```

## Prompt sugerido para Copilot en modo Agent

```text
Ahora ajusta este cliente Python de Open-Meteo usando la informacion investigada.
Quiero que:
1. cambies las coordenadas;
2. revises si conviene ajustar variables u horizonte horario;
3. reduzcas la salida a datos utiles para el partido;
4. agregues una validacion pequena.

Manten el script simple y legible.
```
