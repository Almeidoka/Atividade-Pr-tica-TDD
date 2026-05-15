import re

def validacao_senha(senha: str) -> bool:
    
    regras =[

        len(senha)< 8,
        " " not in senha,
        re.search(r'[A-Z]', senha),
        re.search(r'[a-z]', senha),
        re.search(r'[0-9]', senha),
        re.search(r'[!@#$%^&*()_+={}\[\]|\\:;,.<>?/]', senha)
    ]
    return all(regras)