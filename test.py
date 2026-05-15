import pytest_
from senhas import validacao_senha

def test_letra_maiuscula():
    assert validacao_senha("asdadasd09") is False

def test_letra_minuscula():
    assert validacao_senha("ASDASDA!1") is False

def test_numero():
    assert validacao_senha("asdadaA!a") is False

def test_minimo_caracteres():
    assert validacao_senha("123a") is False

def test_caractere_especial():
    assert validacao_senha("123122aA") is False

def test_espacos():
    assert validacao_senha("123 123!aA") is False

def test_senha_aceita():
    assert validacao_senha("123456Gu!") is True