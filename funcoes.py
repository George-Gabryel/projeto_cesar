import validacao as email

def inserindo(perfil,a,b,c,d, e):
    perfil["email"] = a
    perfil["usuario"] = b
    perfil["telefone"] = c
    perfil["senha"] = d
    perfil["tipo_perfil"] = e

def alterar_usuario(perfil, a, b, c, d):
    while True:
    
        a = input("Informe o usuário que deseja alterar: ")
        b = input("Qual será o novo nome de usuário: ")
        
        validar = False
        
        for c, d in enumerate(perfil["usuario"]):
            if d == a:
                perfil["usuario"][c] = b
                validar = True
                break
        if validar:
            print(f"O usuário foi alterado com sucesso!")
            break
        else:
            print(f"O usuário {a} não está cadastrado. Cadastre-o ou informe um usuário válido")

    
def alterar_email(perfil, a, b, c, d):
    while True:
    
        a = input("Qual e-mail será alterado: ")
        b = input("Qual será o novo e-mail do usuário: ")
        
        if email.validar_email(b):
            print("")
            break
        else:
            print("Email inválido")
            continue
        
        validar = False
        
        for c, d in enumerate(perfil["email"]):
            if d == a:
                perfil["email"][c] = b
                validar = True
                break
        if validar:
            print(f"O e-mail foi alterado com sucesso!")
            break
        else:
            print(f"O e-mail {a} não está cadastrado. Cadastre-o ou informe um e-mail válido")

    
def alterar_telefone(perfil, a, b, c, d):
    while True:
    
        a = int(input("Qual será o número de telefone que será inserido"))
        b = int(input("Qual será o novo número de telefone: "))
        
        validar = False
        
        for c, d in enumerate(perfil["telefone"]):
            if d == a:
                perfil["telefone"][c] = b
                validar = True
                break
        if validar:
            print(f"O o telefone foi alterado com sucesso!")
            break
        else:
            print(f"O telefone {a} não está cadastrado. Cadastre-o ou informe um telefone válido")

def alterar_perfil(perfil, a, b, c, d):
    while True:
    
        a = input("")
        b = input("Qual o novo nome: ")
        
        validar = False
        
        for c, d in enumerate(perfil["usuario"]):
            if d == a:
                perfil["usuario"][c] = b
                validar = True
                break
        if validar:
            print(f"O usuário foi alterado com sucesso!")
            break
        else:
            print(f"O usuário {a} não está cadastrado. Cadastre-o ou informe um usuário válido")
    
def alterar_senha(perfil, a, b, c, d):
    while True:
    
        a = input("Informe a sua senha atual: ")
        b = input("Informe a sua nova")
        
        validar = False
        
        for c, d in enumerate(perfil["usuario"]):
            if d == a:
                perfil["usuario"][c] = b
                validar = True
                break
        if validar:
            print(f"O usuário foi alterado com sucesso!")
            break
        else:
            print(f"O usuário {a} não está cadastrado. Cadastre-o ou informe um usuário válido")