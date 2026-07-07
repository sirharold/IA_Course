# Prompt file - Derivar contrato implicito

Actua como ingeniero senior especializado en integraciones.

Ayudame a derivar un contrato tecnico implicito a partir de:

- codigo que consume un payload;
- ejemplos reales o semi reales de payloads;
- inconsistencias entre nombres, tipos o estructuras.

## Tu tarea

1. Lista campos que el codigo parece requerir.
2. Lista campos que llegan en las muestras pero no coinciden en nombre o forma.
3. Marca riesgos de integracion:
   - campo obligatorio ausente;
   - tipo incompatible;
   - estructura anidada distinta;
   - fecha o monto con formato ambiguo.
4. Propone una estructura de salida util para revisar el contrato.
5. Declara explicitamente que parte es hecho y que parte es inferencia.

## Restricciones

- No inventes endpoints, DTOs ni reglas no visibles.
- Si el codigo y las muestras se contradicen, destaca la contradiccion en vez de resolverla silenciosamente.
