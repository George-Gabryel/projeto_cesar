def inserindo(perfil,a,b,c,d, e):
    perfil["email"] = a
    perfil["usuario"] = b
    perfil["telefone"] = c
    perfil["senha"] = d
    perfil["tipo_perfil"] = e

def alterar_usuario(perfil, a, b, c):
    while True:
    
        a = input("Qual nome deseja alterar: ")
        b = input("Qual o novo nome: ")
        
        validar = False
        
        for posicao, nome_atual in enumerate(perfil["usuario"]):
            if nome_atual == nome_antigo:
                perfil["usuario"][posicao] = nome_novo
                validar = True
                break
        if validar:
            print(f"O usuário foi alterado com sucesso!")
            break
        else:
            print(f"O usuário {nome_antigo} não está cadastrado. Cadastre-o ou informe um usuário válido")

    
def alterar_email(perfil, a, b, c):
    for posicao, a in enumerate(perfil["email"]):
        if a == b:
            perfil["usuario"][posicao] = c
            break
        else:
            print("Hello")

    print(perfil["usuario"])

    
def alterar_telefone(perfil, a, b, c):
    for posicao, a in enumerate(perfil["telefone"]):
        if a == b:
            perfil["usuario"][posicao] = c
            break
        else:
            print("Hello")

    print(perfil["usuario"])

    
def alterar_perfil(perfil, a, b, c):
    for posicao, a in enumerate(perfil["senha"]):
        if a == b:
            perfil["usuario"][posicao] = c
            break
        else:
            print("Hello")

    print(perfil["usuario"])
    
def alterar_senha(perfil, a, b, c):
    for posicao, a in enumerate(perfil["tipo_perfil"]):
        if a == b:
            perfil["usuario"][posicao] = c
            break
        else:
            print("Hello")

    print(perfil["usuario"])