

def validar_email(email):
    import re
    # Padrão básico para e-mails válidos
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(padrao, email))
 