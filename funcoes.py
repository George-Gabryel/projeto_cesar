import validacao as validar

def inserindo(padrao, a, b, c, d, e):
    padrao["email"].append(a)
    padrao["usuario"].append(b)
    padrao["telefone"].append(c)
    padrao["senha"].append(d)
    padrao["tipo_perfil"].append(e)

def alterar_usuario(padrao):
    nome_antigo = input("Qual nome deseja alterar: ")
    nome_novo = input("Qual o novo nome: ")

    encontrado = False
    
    for posicao_email, email_atual in enumerate(padrao["email"]):
        if email_atual == verificacao:
            for posicao_usuario, usuario in enumerate(padrao["usuario"]):
                if posicao_usuario == posicao_email:
                    print("Nome de usuário -->", padrao["usuario"][posicao_email])
                    usuario = input("Qual será o novo nome do usuário:  ")
                    padrao["usuario"][posicao_email] = usuario
                    encontrado = True
                    break

        if encontrado:
            print("O usuário foi alterado com sucesso!")
            break
        else:
            print(f"O usuário {nome_antigo} não está cadastrado.")
    


def alterar_email(padrao):
    email_antigo = input("Qual email sera alterado: ")
    if validar.validar_email(email_antigo):


        while True:
            email_encontrado = False # Variável de controle
            
            for posicao, email_atual in enumerate(padrao["email"]):
                if email_atual == email_antigo:
                    email_novo = input("Qual será o novo email: ")
                    
                    if validar.validar_email(email_novo):
                        padrao["email"][posicao] = email_novo
                        print("Email alterado")
                        email_encontrado = True
                        return # Para o loop 'for' pois já achou e alterou
                    else:
                        print("Email inválido. Tente novamente.")
                        # Aqui você decide se quer dar break ou tentar de novo
            
            if email_encontrado:
                break # Para o loop 'while True' se desejar encerrar o programa
            else:
                print("E-mail antigo não encontrado.")
                break # Para evitar loop infinito caso não queira pedir o email_antigo de novo

    else:
        print("Email não reconhecido. Tente novamente e escreva um email válido")



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