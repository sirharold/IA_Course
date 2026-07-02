## Plan: Salidas Excel CSV PDF

Agregar una capa de exportación para que el reporte pueda generarse en csv, excel y pdf, manteniendo la salida actual en consola como comportamiento por defecto. La ejecución se implementará con un flujo: seleccionar formato por argumento/selector, reutilizar review_payments como fuente única de datos y delegar la serialización a exportadores por formato.

### Plan técnico para agente

**Objetivo técnico**
Permitir que el usuario elija formato de salida del reporte entre excel, csv o pdf, generando archivo en disco con manejo de errores y pruebas.

**Fase 1 - Estructura y alcance**
1. Crear carpeta plans dentro de payment_review_assistant.
2. Crear archivo plans/plan_saldiareportes.md con este contenido.
3. Confirmar alcance: solo excel/csv/pdf en esta iteración.
4. Mantener la salida por consola existente como comportamiento por defecto para no romper ejercicios actuales.

**Fase 2 - Selección de formato (entrada de usuario)**
1. Extender main.py para aceptar argumentos de línea de comandos:
   - --format con valores permitidos: excel, csv, pdf.
   - --output para ruta de archivo destino.
   - --input opcional para ruta del JSON de entrada.
2. Validar formato y retornar error legible si no es permitido.
3. Definir mensajes de ayuda (argparse) con ejemplos.

**Fase 3 - Contrato de salida unificado**
1. Definir columnas comunes para todos los formatos, combinando raw/review/summary:
   payment_id, customer_name, amount, currency, channel, status, score, priority, headline, detail, reasons.
2. Crear función interna para mapear cada item de review_payments a una fila tabular homogénea.
3. Garantizar orden fijo de columnas para consistencia entre csv/excel/pdf.

**Fase 4 - Implementación de exportadores**
1. Crear package payment_review/exporters.
2. Crear interfaz base o contrato común de exportación.
3. Implementar csv_exporter:
   - UTF-8.
   - Cabeceras fijas.
   - Escape correcto de comillas/comas/saltos de línea.
4. Implementar excel_exporter:
   - Archivo .xlsx.
   - Hoja única "Payment Review".
   - Cabeceras en primera fila.
   - Dependencia recomendada: openpyxl.
5. Implementar pdf_exporter:
   - Título + fecha + tabla resumida.
   - Paginación para datasets largos.
   - Dependencia recomendada: fpdf2 o reportlab.
6. Implementar fábrica/registro de exportadores para resolver por formato.

**Fase 5 - Orquestación en servicio**
1. En service.py agregar export_report(path, format, output_path).
2. Reutilizar review_payments(path) como única fuente de datos.
3. Delegar la escritura al exportador correspondiente.
4. Mantener print_report(path) sin cambios funcionales, excepto reutilización interna si conviene.

**Fase 6 - Errores y resiliencia**
1. Formato inválido: error claro con formatos soportados.
2. Ruta de salida no escribible: error controlado.
3. Dependencia faltante (excel/pdf): instrucción de instalación explícita.
4. Dataset vacío: generar archivo válido con cabeceras (o aviso controlado).

**Fase 7 - Pruebas**
1. Pruebas unitarias por exportador (csv/excel/pdf).
2. Pruebas de integración de flujo completo desde main/service.
3. Comparar consistencia de columnas y número de filas entre formatos.
4. Casos borde: caracteres especiales, texto largo, valores nulos.

**Fase 8 - Documentación**
1. Actualizar README del módulo con ejemplos de uso.
2. Documentar instalación de dependencias de exportación.
3. Agregar troubleshooting para errores comunes.

**Criterios de aceptación**
1. Usuario puede elegir excel/csv/pdf desde ejecución.
2. Se generan archivos válidos en la ruta indicada.
3. Salida por consola sigue funcionando sin argumentos.
4. Pruebas principales pasan sin regresiones.

### Resumen para humano

La propuesta es separar el “qué se calcula” del “cómo se entrega”.

Hoy el sistema ya calcula y resume pagos correctamente; solo imprime en consola. El cambio consiste en añadir una capa de exportación para que el usuario elija si quiere el reporte en csv, excel o pdf. Así, no se toca la lógica de negocio (reglas y normalización), solo la forma de salida.

Beneficios:
1. Menor riesgo de romper lo existente.
2. Diseño extensible para formatos futuros.
3. Mejor experiencia para usuario no técnico que necesita archivos compartibles.

Resultado esperado:
Con un comando, el usuario elige formato y obtiene su archivo de reporte listo para abrir o enviar.