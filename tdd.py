import unittest

from senhas import validar_senha

class TestSenha(unittest.TestCase):

    def test_senha_curta(self):
        self.assertFalse(validar_senha("Ab1!"))

    def test_senha_sem_maiuscula(self):
        self.assertFalse(validar_senha("senha123!"))

    def test_senha_sem_minuscula(self):
        self.assertFalse(validar_senha("SENHA!123"))

    def test_senha_sem_numero(self):
        self.assertFalse(validar_senha("SenhaNumeros!"))

    def test_senha_sem_caracteresp(self):
        self.assertFalse(validar_senha("SenhaTop1"))

    def test_senha_com_espaco(self):
        self.assertFalse(validar_senha("Senha 123!"))

    def test_senha_valida(self):
        self.assertFalse(validar_senha("Senha123!"))
if __name__ == "__main__":
    unittest.main()