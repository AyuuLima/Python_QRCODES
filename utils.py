def validar_codigo(codigo, lista_codigos):
    return codigo in lista_codigos


def ja_registrado(codigo, registros):
    return codigo in registros


def pode_entrar(codigo, lista_codigos, registros):
    if codigo not in lista_codigos:
        return "invalido"
    if codigo in registros:
        return "duplicado"
    return "ok"