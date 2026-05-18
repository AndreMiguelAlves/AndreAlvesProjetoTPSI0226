import re

#validar email
def validar_email(email):
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(padrao, email) is not None

#Formato DD-MM-AAAA
def validar_data(data):
    padrao = r'^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|12)-\d{4}$'
    return re.match(padrao, data) is not None

#2 letras maiúsculas e 4 números
def validar_codigo_colmeia(codigo):
    padrao = r'^[A-Z]{2}\d{4}$'
    return re.match(padrao, codigo) is not None