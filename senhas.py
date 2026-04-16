import re

def validar_senha(senha):
    if len(senha)< 8:
        return False
    if " " in senha:
        return False
    
    tem_maiuscula = re.search(r'[A-Z]', senha)
    tem_minuscula = re.search(r'[a-z]', senha)
    tem_numero = re.search(r'[0-9]', senha)
    tem_especial = re.search(r'[!@#$%^&*]', senha)
    
    if not (tem_numero and tem_especial and tem_maiuscula and tem_maiuscula):
        return False
    return True