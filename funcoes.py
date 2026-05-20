import validacao as validar

def inserindo(padrao, a, b, c, d, e):
    padrao["email"].append(a)
    padrao["usuario"].append(b)
    padrao["telefone"].append(c)
    padrao["senha"].append(d)
    padrao["tipo_perfil"].append(e)

def alterar_usuario(padrao):
    verificacao = input("Informe o e-mail do usuário que será alterado: ")
   
    encontrado = False
    for posicao_email, email_atual in enumerate(padrao["email"]):
        if email_atual == verificacao:
            for posicao_usuario in (padrao["usuario"]):
                if posicao_email == posicao_usuario:
                    nome_novo = input("Qual o novo nome: ")
                    padrao["usuario"][posicao_usuario] = nome_novo
                    encontrado = True
                    break

        if encontrado:
            print("O usuário foi alterado com sucesso!")
            break
        else:
            print(f"O usuário {verificacao} não está cadastrado.")
    



def alterar_email(padrao):
    email_antigo = input("Qual email sera alterado: ")

    while True:
        email_novo = input("Qual sera o novo email: ")
        if validar.validar_email(email_novo):
            break
        print("Email invalido, tente novamente.")

    for posicao, email_atual in enumerate(padrao["email"]):
        if email_atual == email_antigo:
            padrao["email"][posicao] = email_novo
            print("Email alterado")
            return
    print(f"email {email_antigo} nao esta cadastrado. Cadastre-o ou informe um email válido")




def alterar_telefone(padrao):
    telefone_antigo = input("Qual telefone sera alterado: ")

    while True:
        telefone_novo = input("Qual sera o novo telefone: ")
        if validar.validar_telefone(telefone_novo):
            break
        print("telefone paia")

    for posicao, telefone_atual in enumerate(padrao["telefone"]):
        if telefone_atual == telefone_antigo:
            padrao["telefone"][posicao] = telefone_novo
            print("Telefone alterado")
            return
    print(f"O telefone {telefone_antigo} nao esta cadastrado. Cadastre-o ou informe um telefone válido")




def alterar_perfil(padrao):
    usuario = input("Informe seu usuário: ")
    
    for posicao, usuario_atual in enumerate(padrao["usuario"]):
        if usuario_atual == usuario:
            perfil_novo = input("Qual o novo tipo de padrao: ")
            padrao["tipo_perfil"][posicao] = perfil_novo
            print("Perfil alterado")
            return
    print(f"O usuario '{usuario}' n esta cadastrado.")




def alterar_senha(padrao):
    while True:
        usuario = input("Informe seu usuario: ")
        
        if usuario not in padrao["usuario"]:
            print(f"O usuario '{usuario}' n esta cadastrado.")
            continue
        
        senha_atual = input("Informe sua senha atual: ")
        posicao = padrao["usuario"].index(usuario)
        
        if padrao["senha"][posicao] != senha_atual:
            print("Senha atual ta errada")
            continue
        
        senha_nova = input("Informe a nova senha: ")
        padrao["senha"][posicao] = senha_nova
        print("Senha alterada")
        break