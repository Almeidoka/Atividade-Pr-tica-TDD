import re

def validacao_senha(senha: str) -> bool:
    
    padrao = (
        r'^(?=.*[A-Z])'
        r'(?=.*[a-z])'
        r'(?=.*\d)'
        r'(?=.*[!@#$%^&*()_+={}\[\]|\\:;,.<>?/])'
        r'(?!.*\s)'
        r'.{8,}$'
    )

    return re.match(padrao, senha) is not None