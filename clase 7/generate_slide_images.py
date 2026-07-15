from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


W, H = 1920, 1080
BG = (17, 20, 37)
PANEL = (19, 34, 58)
PANEL_ALT = (16, 31, 53)
WHITE = (247, 247, 244)
MUTED = (214, 221, 238)
PURPLE = (163, 17, 227)
PINK = (255, 0, 155)
CYAN = (64, 236, 212)
BLUE = (76, 89, 255)
LINE = (75, 111, 255)

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "imagenes"


def get_font(size, bold=False):
    candidates = []
    if bold:
        candidates = [
            "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
            "/Library/Fonts/Arial Bold.ttf",
            "/System/Library/Fonts/SFNS.ttf",
        ]
    else:
        candidates = [
            "/System/Library/Fonts/Supplemental/Arial.ttf",
            "/Library/Fonts/Arial.ttf",
            "/System/Library/Fonts/SFNS.ttf",
        ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size=size)
    return ImageFont.load_default()


FONT_HUGE = get_font(76, True)
FONT_TITLE = get_font(56, True)
FONT_SUB = get_font(34, True)
FONT_BODY = get_font(26, False)
FONT_BODY_BOLD = get_font(26, True)
FONT_SMALL = get_font(22, False)
FONT_SMALL_BOLD = get_font(22, True)
FONT_BADGE = get_font(30, True)


def wrap_text(draw, text, font, max_width):
    words = text.split()
    lines = []
    current = ""
    for word in words:
        test = word if not current else f"{current} {word}"
        if draw.textbbox((0, 0), test, font=font)[2] <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_multiline(draw, x, y, text, font, fill, max_width, line_gap=10):
    lines = wrap_text(draw, text, font, max_width)
    yy = y
    for line in lines:
        draw.text((x, yy), line, font=font, fill=fill)
        box = draw.textbbox((x, yy), line, font=font)
        yy += (box[3] - box[1]) + line_gap
    return yy


def glow_blob(size, color, blur):
    img = Image.new("RGBA", size, (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.ellipse((0, 0, size[0], size[1]), fill=color)
    return img.filter(ImageFilter.GaussianBlur(blur))


def create_base(label="CLASE 7"):
    img = Image.new("RGBA", (W, H), BG + (255,))
    img.alpha_composite(glow_blob((780, 780), (92, 14, 108, 190), 80), (-120, -90))
    img.alpha_composite(glow_blob((840, 620), (44, 141, 158, 180), 110), (1110, -150))
    img.alpha_composite(glow_blob((520, 520), (36, 114, 104, 120), 90), (1400, 760))

    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle((34, 34, 186, 82), radius=24, fill=BLUE)
    draw.text((52, 42), label, font=FONT_BADGE, fill=WHITE)

    x0 = 1438
    for i in range(5):
        x = x0 + i * 90
        draw.line((x, 34, x, 100), fill=(88, 116, 255), width=4)
        draw.ellipse((x - 8, 92, x + 8, 108), fill=(88, 116, 255))
    for y in [82, 118, 154]:
        draw.line((1760, y, 1894, y), fill=(81, 214, 255), width=4)
        draw.ellipse((1887, y - 7, 1901, y + 7), fill=(81, 214, 255))
    return img, draw


def panel(draw, box, outline=LINE, fill=PANEL, radius=28, width=3):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def numbered_chip(draw, cx, cy, num, fill=PINK):
    draw.ellipse((cx - 26, cy - 26, cx + 26, cy + 26), fill=fill)
    txt = str(num)
    bbox = draw.textbbox((0, 0), txt, font=FONT_SUB)
    draw.text(
        (cx - (bbox[2] - bbox[0]) / 2, cy - (bbox[3] - bbox[1]) / 2 - 2),
        txt,
        font=FONT_SUB,
        fill=WHITE,
    )


def add_title(draw, title, y=124, x=144, max_width=980, font=FONT_HUGE):
    return draw_multiline(draw, x, y, title, font, WHITE, max_width, line_gap=6)


def bullet_list(draw, x, y, items, max_width, bullet_color=CYAN, font=FONT_BODY, gap=18):
    yy = y
    for item in items:
        draw.ellipse((x, yy + 10, x + 16, yy + 26), fill=bullet_color)
        yy = draw_multiline(draw, x + 34, yy, item, font, MUTED, max_width - 34, 6) + gap
    return yy


def slide_agenda():
    img, draw = create_base()
    add_title(draw, "Agenda de la clase 7", x=144, y=120, max_width=760)
    draw_multiline(
        draw,
        146,
        308,
        "Skills, customizacion reusable y MCP: cuando encapsular, cuando ampliar alcance y como leer el ecosistema sin convertirlo en checklist.",
        FONT_BODY,
        MUTED,
        760,
        8,
    )

    times = [
        ("15:00", "Recuperacion de la clase 6 y encuadre"),
        ("15:15", "Del prompt aislado a la capacidad reusable"),
        ("15:35", "Instructions, prompt files y skills"),
        ("15:55", "Beneficios, contras y errores comunes"),
        ("16:15", "Break"),
        ("16:25", "MCP: que es, que aporta y que no aporta"),
        ("16:45", "Panorama rapido: MCPs y skills populares"),
        ("17:05", "Laboratorio guiado: 2 ejercicios base"),
        ("17:50", "Cierre y siguiente trabajo"),
    ]

    x = 930
    y = 184
    step = 78
    for i, (hour, text) in enumerate(times, start=1):
        cy = y + (i - 1) * step + 26
        is_break = text == "Break"
        draw.ellipse((x - 52, cy - 26, x, cy + 26), fill=PINK if is_break else CYAN)
        draw.text((x - 36, cy - 18), str(i), font=FONT_SMALL_BOLD, fill=WHITE)
        panel(draw, (x + 26, cy - 32, 1824, cy + 32), outline=BLUE if is_break else LINE)
        draw.text((x + 46, cy - 19), hour, font=FONT_BODY_BOLD, fill=WHITE)
        draw.text((x + 160, cy - 19), text, font=FONT_SMALL if len(text) > 52 else FONT_BODY, fill=MUTED)

    draw.line((204, 408, 760, 408), fill=CYAN, width=7)
    for step_i, txt in enumerate(["15:00", "16:15", "18:00"]):
        px = 204 + step_i * 278
        draw.ellipse((px - 12, 396, px + 12, 420), fill=CYAN)
        draw.text((px - 26, 442), txt, font=FONT_SMALL_BOLD, fill=WHITE)
    draw.text((146, 500), "Objetivo", font=FONT_SUB, fill=WHITE)
    draw_multiline(
        draw,
        146,
        550,
        "Pasar de prompts aislados a capacidades reutilizables, entender cuando MCP agrega valor real y cerrar con una prueba guiada.",
        FONT_BODY,
        MUTED,
        650,
        10,
    )
    return img


def slide_split(title, left_title, left_items, right_title, right_items, subtitle=None):
    img, draw = create_base()
    title_end = add_title(draw, title, x=144, y=120, max_width=980)
    if subtitle:
        subtitle_end = draw_multiline(draw, 146, title_end + 24, subtitle, FONT_BODY, MUTED, 1000, 8)
        top = subtitle_end + 34
    else:
        top = title_end + 36
    panel(draw, (118, top, 872, 882), outline=CYAN, fill=PANEL_ALT)
    panel(draw, (996, top, 1802, 882), outline=PURPLE, fill=PANEL)
    draw.text((154, top + 36), left_title, font=FONT_SUB, fill=WHITE)
    draw.text((1032, top + 36), right_title, font=FONT_SUB, fill=WHITE)
    bullet_list(draw, 156, top + 106, left_items, 640, bullet_color=CYAN)
    bullet_list(draw, 1034, top + 106, right_items, 660, bullet_color=PINK)
    return img


def slide_compare(title, left_title, left_text, right_title, right_items, footer=None):
    img, draw = create_base()
    title_end = add_title(draw, title, x=144, y=120, max_width=980)
    top = title_end + 36
    panel(draw, (118, top, 858, 872), outline=PINK)
    panel(draw, (1018, top, 1802, 872), outline=CYAN)
    draw.text((152, top + 32), left_title, font=FONT_SUB, fill=WHITE)
    draw_multiline(draw, 152, top + 108, left_text, FONT_TITLE, WHITE, 600, 4)
    draw.text((1052, top + 32), right_title, font=FONT_SUB, fill=WHITE)
    y = top + 116
    for idx, bullet in enumerate(right_items, start=1):
        numbered_chip(draw, 1090, y + 22, idx, fill=CYAN if idx % 2 else PURPLE)
        y = draw_multiline(draw, 1138, y, bullet, FONT_BODY_BOLD if idx < 3 else FONT_BODY, MUTED if idx >= 3 else WHITE, 600, 6) + 28
    if footer:
        panel(draw, (1050, 760, 1768, 852), outline=BLUE, fill=PANEL_ALT, radius=24, width=2)
        draw_multiline(draw, 1080, 786, footer, FONT_SMALL_BOLD, MUTED, 640, 4)
    return img


def slide_cards(title, subtitle, cards):
    img, draw = create_base()
    title_end = add_title(draw, title, x=144, y=120, max_width=980)
    subtitle_end = draw_multiline(draw, 146, title_end + 24, subtitle, FONT_BODY, MUTED, 1100, 8)
    positions = [
        (118, subtitle_end + 36, 872, subtitle_end + 252),
        (996, subtitle_end + 36, 1802, subtitle_end + 252),
        (118, subtitle_end + 304, 872, subtitle_end + 520),
        (996, subtitle_end + 304, 1802, subtitle_end + 520),
    ]
    for i, ((head, body), box) in enumerate(zip(cards, positions), start=1):
        panel(draw, box, outline=CYAN if i % 2 else PURPLE, fill=PANEL_ALT if i % 2 else PANEL)
        numbered_chip(draw, box[0] + 48, box[1] + 48, i, fill=CYAN if i % 2 else PURPLE)
        draw_multiline(draw, box[0] + 94, box[1] + 28, head, FONT_SUB, WHITE, box[2] - box[0] - 120, 4)
        draw_multiline(draw, box[0] + 34, box[1] + 96, body, FONT_BODY, MUTED, box[2] - box[0] - 68, 7)
    return img


def slide_flow(title, steps, footer=None):
    img, draw = create_base()
    title_end = add_title(draw, title, x=144, y=120, max_width=980)
    card_w = 296
    x = 104
    y = title_end + 56
    colors = [CYAN, PURPLE, BLUE, PINK, CYAN, PURPLE]
    for i, (head, body) in enumerate(steps, start=1):
        box = (x, y, x + card_w, y + 286)
        panel(draw, box, outline=colors[(i - 1) % len(colors)], fill=PANEL_ALT if i % 2 else PANEL)
        numbered_chip(draw, x + 52, y + 54, i, fill=colors[(i - 1) % len(colors)])
        draw_multiline(draw, x + 94, y + 30, head, FONT_SUB, WHITE, card_w - 120, 4)
        draw_multiline(draw, x + 30, y + 108, body, FONT_SMALL, MUTED, card_w - 60, 6)
        if i < len(steps):
            mid = x + card_w + 18
            draw.line((mid, y + 142, mid + 22, y + 142), fill=CYAN, width=8)
            draw.polygon([(mid + 22, y + 142), (mid + 6, y + 128), (mid + 6, y + 156)], fill=CYAN)
        x += card_w + 12
    if footer:
        panel(draw, (188, 770, 1728, 900), outline=BLUE, fill=PANEL_ALT, radius=24, width=2)
        draw_multiline(draw, 226, 808, footer, FONT_BODY, MUTED, 1460, 6)
    return img


def slide_timeline(title, items, subtitle=None):
    img, draw = create_base()
    title_end = add_title(draw, title, x=144, y=120, max_width=980)
    if subtitle:
        subtitle_end = draw_multiline(draw, 146, title_end + 24, subtitle, FONT_BODY, MUTED, 1100, 8)
        y = subtitle_end + 44
    else:
        y = title_end + 60
    for i, (head, body) in enumerate(items, start=1):
        color = CYAN if i % 2 else PURPLE
        draw.ellipse((164, y + 6, 216, y + 58), fill=color)
        draw.text((182, y + 16), str(i), font=FONT_SMALL_BOLD, fill=WHITE)
        panel(draw, (244, y - 6, 1760, y + 78), outline=color, fill=PANEL_ALT if i % 2 else PANEL)
        draw.text((274, y + 10), head, font=FONT_BODY_BOLD, fill=WHITE)
        draw.text((600, y + 10), body, font=FONT_BODY, fill=MUTED)
        y += 102
    return img


def slide_dense_list(title, subtitle, left_title, left_items, right_title, right_items):
    img, draw = create_base()
    title_end = add_title(draw, title, x=144, y=120, max_width=1150)
    subtitle_end = draw_multiline(draw, 146, title_end + 18, subtitle, FONT_SMALL, MUTED, 1300, 6)
    top = subtitle_end + 28
    panel(draw, (118, top, 872, 904), outline=CYAN, fill=PANEL_ALT)
    panel(draw, (996, top, 1802, 904), outline=PURPLE, fill=PANEL)
    draw.text((154, top + 28), left_title, font=FONT_SUB, fill=WHITE)
    draw.text((1032, top + 28), right_title, font=FONT_SUB, fill=WHITE)

    y_left = top + 92
    for idx, item in enumerate(left_items, start=1):
        numbered_chip(draw, 170, y_left + 20, idx, fill=CYAN if idx % 2 else BLUE)
        draw_multiline(draw, 214, y_left, item, FONT_SMALL_BOLD, WHITE, 600, 4)
        y_left += 58

    y_right = top + 92
    for idx, item in enumerate(right_items, start=11):
        numbered_chip(draw, 1048, y_right + 20, idx, fill=PURPLE if idx % 2 else PINK)
        draw_multiline(draw, 1092, y_right, item, FONT_SMALL_BOLD, WHITE, 620, 4)
        y_right += 58
    return img


def save(img, name):
    OUT.mkdir(parents=True, exist_ok=True)
    img.convert("RGB").save(OUT / name)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for old_png in OUT.glob("*.png"):
        old_png.unlink()

    slides = [
        ("01-agenda-clase-07.png", slide_agenda()),
        (
            "02-slide-04-cambio-nivel.png",
            slide_split(
                "Cambio de nivel respecto de la clase 6",
                "Clase 6",
                [
                    "Operar mejor con Copilot CLI.",
                    "Explicar, ejecutar y validar desde terminal.",
                ],
                "Clase 7",
                [
                    "Dejar de repetir instrucciones sueltas.",
                    "Formalizar tareas recurrentes.",
                    "Entender cuando hace falta tooling o contexto externo.",
                ],
            ),
        ),
        (
            "03-slide-05-problema-real.png",
            slide_compare(
                "Elegir la capa correcta",
                "Prompt libre",
                "Flexible y rapido, pero depende mucho de quien lo escriba.",
                "Skill y MCP",
                [
                    "Skill: reusable y mas consistente cuando la tarea ya esta clara.",
                    "MCP: agrega alcance y herramientas cuando hace falta salir del repo o del chat.",
                    "No compiten siempre: a veces se complementan.",
                    "Y a veces ninguno hace falta.",
                ],
                footer="La decision importante no es usar mas piezas. Es elegir la capa correcta para la tarea correcta.",
            ),
        ),
        (
            "04-slide-06-instructions-prompt-files-skills.png",
            slide_split(
                "Que es un skill",
                "Que es",
                [
                    "Un paquete de instrucciones especializado para resolver una tarea concreta.",
                    "No es una herramienta externa.",
                    "No es una fuente nueva de datos.",
                    "Organiza una forma de trabajar para repetirla mejor.",
                ],
                "Analogia",
                [
                    "Custom instruction: decirle a un colaborador como te gusta trabajar siempre.",
                    "Prompt file: pasarle una plantilla ya armada.",
                    "Skill: entregarle una guia de trabajo especializada para una tarea recurrente.",
                ],
            ),
        ),
        (
            "05-slide-07-beneficios-limites-skills.png",
            slide_timeline(
                "Ejemplos de skills",
                [
                    ("Logs e incidentes", "Revisar logs o incidentes siempre con la misma estructura."),
                    ("Documentacion", "Generar documentacion tecnica con un formato fijo."),
                    ("Triage", "Hacer triage de bugs recurrentes."),
                    ("Code review", "Revisar codigo con un criterio de equipo ya definido."),
                    ("Reportes", "Preparar reportes operativos repetitivos."),
                    ("Planes tecnicos", "Crear planes o especificaciones con una plantilla estable."),
                ],
                subtitle="Skill sirve mejor cuando la tarea se repite y ya sabes como quieres que se haga.",
            ),
        ),
        (
            "06-slide-08-beneficios-limites-skills.png",
            slide_cards(
                "Beneficios y limites de usar skills",
                "No se trata de usar skills por moda. Se trata de decidir si ayudan a repetir mejor una tarea real.",
                [
                    ("Consistencia", "Misma tarea, misma forma de trabajar, aunque cambie la persona que la ejecuta."),
                    ("Menos repeticion", "Reduce la necesidad de volver a explicar contexto, formato y criterio cada vez."),
                    ("Riesgo de error escalado", "Si el skill esta mal definido, repite el mismo error con disciplina."),
                    ("Validacion sigue viva", "Skill no reemplaza supervision humana, evidencia ni pruebas."),
                ],
            ),
        ),
        (
            "07-slide-09-mcp-en-una-idea.png",
            slide_compare(
                "Que es un MCP",
                "MCP",
                "Es una forma estandar de conectar Copilot con herramientas o fuentes externas.",
                "Analogia y efecto",
                [
                    "Si el skill es una forma de trabajar mejor, el MCP le da nuevos ojos y nuevas manos.",
                    "No cambia solo como responde: cambia a que puede acceder.",
                    "Puede leer contexto que no esta en el chat ni en el repo local.",
                    "Puede usar herramientas conectadas o consultar sistemas externos.",
                ],
                footer="No significa que el modelo se vuelva mas inteligente ni que usarlo siempre mejore la solucion.",
            ),
        ),
        (
            "08-slide-10-ejemplos-mcp.png",
            slide_timeline(
                "Ejemplos de MCP",
                [
                    ("GitHub MCP", "Leer issues y pull requests reales."),
                    ("Microsoft Learn MCP", "Consultar documentacion oficial actual."),
                    ("MarkItDown MCP", "Convertir PDF a Markdown reutilizable."),
                    ("DuckDB MCP", "Consultar CSVs o datos tabulares con precision."),
                    ("Filesystem MCP", "Leer archivos o carpetas fuera del contexto inmediato."),
                    ("Playwright MCP", "Observar o automatizar una interfaz web."),
                ],
            ),
        ),
        (
            "09-slide-11-aporta-no-aporta-mcp.png",
            slide_split(
                "Beneficios y limites de usar MCP",
                "Si aporta",
                [
                    "Cuando falta contexto fuera del repo.",
                    "Cuando hace falta consultar una fuente oficial o un sistema real.",
                    "Cuando el flujo necesita herramientas, no solo texto.",
                ],
                "Analogia de decision",
                [
                    "Skill ensena una rutina; MCP abre una puerta a otra herramienta o fuente.",
                    "Si no hace falta salir de la pieza, abrir esa puerta agrega poco valor.",
                    "Si solo agrega setup y complejidad, no conviene usarlo.",
                ],
            ),
        ),
        (
            "10-slide-12-errores-comunes.png",
            slide_cards(
                "Errores comunes",
                "Los errores de esta etapa aparecen cuando se encapsula o integra antes de entender bien la tarea.",
                [
                    ("Encapsular demasiado pronto", "Formalizar una tarea mal definida solo hace que el error se repita mejor."),
                    ("Confiar ciegamente en el skill", "Un skill no garantiza calidad ni reemplaza juicio tecnico."),
                    ("Meter MCP porque si", "Si el repo local basta, sumar tooling externo puede empeorar el flujo."),
                    ("Olvidar validar", "La salida sigue necesitando evidencia, contraste y supervision humana."),
                ],
            ),
        ),
        (
            "11-slide-13-mcps-populares.png",
            slide_dense_list(
                "10 MCPs populares y su beneficio",
                "Lista orientativa basada en listas curadas, demos y flujos reales del ecosistema 2026.",
                "1 a 5",
                [
                    "GitHub MCP Server: acceso a issues y PRs reales.",
                    "Context7 MCP: documentacion tecnica actual y util para desarrollo.",
                    "Playwright MCP: automatizacion y observacion web.",
                    "Figma MCP: acceso a diseno y handoff de interfaces.",
                    "PostgreSQL MCP: consultas sobre bases relacionales.",
                ],
                "6 a 10",
                [
                    "Supabase MCP: acceso a base, auth y storage en un mismo stack.",
                    "Slack MCP: acceso a conversaciones o contexto de equipo.",
                    "Notion MCP: acceso a documentacion viva del equipo.",
                    "Linear MCP: acceso a backlog e issues operativos.",
                    "Sentry MCP: acceso a errores y contexto de incidentes.",
                    "MarkItDown MCP: conversion de PDF a Markdown.",
                ],
            ),
        ),
        (
            "12-slide-14-skills-populares.png",
            slide_dense_list(
                "10 skills populares y su beneficio",
                "Lista orientativa basada en skills visibles de Awesome Copilot y flujos actuales durante 2026.",
                "1 a 5",
                [
                    "Acquire Codebase Knowledge: mapear y documentar una base de codigo existente.",
                    "Ai Ready: preparar un repo para trabajar mejor con IA.",
                    "Agent Owasp Compliance: revisar riesgos agenticos con foco de seguridad 2026.",
                    "Architecture Blueprint Generator: generar arquitectura tecnica mas consistente.",
                    "Automate This: convertir procesos manuales en automatizacion asistida.",
                ],
                "6 a 10",
                [
                    "Autoresearch: ejecutar ciclos iterativos de mejora o experimentacion.",
                    "Aws Resource Query: consultar recursos AWS en lenguaje natural.",
                    "Azure Architecture Autopilot: disenar o analizar arquitecturas Azure.",
                    "Boost Prompt: refinar prompts de forma guiada.",
                    "Brag Sheet: reconstruir y documentar impacto o trabajo realizado.",
                ],
            ),
        ),
        (
            "13-slide-15-bloque-practico.png",
            slide_timeline(
                "Bloque practico de hoy",
                [
                    ("Comparar", "Prompt libre versus skill sobre una tarea tecnica concreta."),
                    ("Probar", "Instalar y usar algunos skills en tareas reales o semi-reales."),
                    ("Observar", "Detectar donde una herramienta externa o MCP si cambia el alcance."),
                    ("Registrar", "Anotar que mejoro, que se volvio mas complejo y que siguio necesitando validacion."),
                    ("Cerrar", "Preparar el paso a workflows mas ricos en la clase 8."),
                ],
            ),
        ),
        (
            "14-slide-16-cierre.png",
            slide_compare(
                "Cierre",
                "Idea central",
                "Prompt, skill y MCP son capas distintas de trabajo. El valor no esta en usar mas piezas, sino en elegir la capa correcta para la tarea correcta.",
                "Lo que deja instalada esta clase",
                [
                    "Mejor criterio para encapsular tareas repetitivas.",
                    "Mejor criterio para decidir cuando MCP vale la pena.",
                    "Base conceptual para workflows avanzados con agente, CLI y tooling.",
                ],
                footer="Clase 8: skill, agente, CLI y herramientas ya aparecen dentro de un workflow mas integrado.",
            ),
        ),
    ]

    for name, img in slides:
        save(img, name)


if __name__ == "__main__":
    main()
