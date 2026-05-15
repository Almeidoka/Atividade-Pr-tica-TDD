import pytest_

def test_letra_maiuscula():
    assert validacao_senha("asdadasd09") is False

def test_numero():
    assert validacao_senha("asdadaA!a") is False
