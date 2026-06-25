def validar_rut(rut: str) -> bool:
    """
    Valida un RUT chileno en formato con o sin puntos/guión.
    Ejemplos válidos: 12.345.678-5, 12345678-5, 123456785
    """
    rut = rut.replace(".", "").replace("-", "").upper().strip()

    if len(rut) < 2:
        return False

    cuerpo = rut[:-1]
    dv = rut[-1]

    if not cuerpo.isdigit():
        return False

    suma = 0
    multiplo = 2

    for digito in reversed(cuerpo):
        suma += int(digito) * multiplo
        multiplo += 1
        if multiplo > 7:
            multiplo = 2

    resto = 11 - (suma % 11)

    if resto == 11:
        dv_calculado = "0"
    elif resto == 10:
        dv_calculado = "K"
    else:
        dv_calculado = str(resto)

    return dv == dv_calculado


print('Hola mundo')

# Ejemplo de uso
rut_ejemplo = "12.345.678-5"
print(f"{rut_ejemplo} es válido? {validar_rut(rut_ejemplo)}")
