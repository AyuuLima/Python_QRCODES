from utils import validar_codigo, ja_registrado, pode_entrar


def test_codigo_valido():
    assert validar_codigo("123", ["123", "456"]) == True


def test_codigo_invalido():
    assert validar_codigo("999", ["123", "456"]) == False


def test_codigo_ja_registrado():
    assert ja_registrado("123", ["123"]) == True


def test_codigo_nao_registrado():
    assert ja_registrado("456", ["123"]) == False


def test_fluxo_ok():
    assert pode_entrar("123", ["123"], []) == "ok"


def test_fluxo_invalido():
    assert pode_entrar("999", ["123"], []) == "invalido"


def test_fluxo_duplicado():
    assert pode_entrar("123", ["123"], ["123"]) == "duplicado"