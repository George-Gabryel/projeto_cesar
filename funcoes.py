import validacao as validar

def inserindo(padrao, email_usuario, nome_usuario, telefone_usuario, senha_usuario, perfil_usuario):
    padrao["email"].append(email_usuario)
    padrao["usuario"].append(nome_usuario)
    padrao["telefone"].append(telefone_usuario)
    padrao["senha"].append(senha_usuario)
    padrao["tipo_perfil"].append(perfil_usuario)

def alterar_usuario(padrao):
   
    verificacao = input("Informe o e-mail que deseja alterar o nome do usuário: ")
    
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
                print(f"O e-mail {verificacao} não foi cadastrado. Verifique o e-mail ou cadastre o usuário")
    


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
    email_antigo = input("Qual e-mail você deseja alterar o telefone cadastrado: ")

    if validar.validar_email(email_antigo):
        while True:
                telefone_encontrado = False 
                
                for posicao, email_atual in enumerate(padrao["email"]):
                    if email_atual == email_antigo:
                        print(f"Telefone cadastrado --> {padrao["telefone"][posicao]}")
                        telefone_novo = input("Qual será o novo telefone: ")
                        
                        if validar.validar_telefone(telefone_novo):
                            padrao["telefone"][posicao] = telefone_novo
                            print("Telefone Alterado com sucesso!!")
                            telefone_encontrado = True
                            return
                        else:
                            print("Telefone inválido. Tente novamente.")
                            break
                
                if telefone_encontrado:
                    break 
                else:
                    print(f"O telefone {email_antigo} não foi encontrado. Cadastre-o ou escreva um telefone já cadastrado")
                    break 

    else:
        print(f"O email {email_antigo} não foi encontrado. Cadastre-o ou escreva um email válido")





def alterar_perfil(padrao):
    email_antigo = input("Qual e-mail você deseja alterar o perfil cadastrado: ")

    if validar.validar_email(email_antigo):
        for posicao, email_atual in enumerate(padrao["email"]):
                    if email_atual == email_antigo:
                        print(f"Perfil cadastrado --> {padrao["tipo_perfil"][posicao]}")
                        perfil_novo = input("Qual será o novo perfil que esse usuário receberá: ")
                        padrao["tipo_perfil"][posicao] = perfil_novo
                        print("Perfil alterado")
                        return
        print(f"O e-mail '{email_antigo}' não está cadastrado. Cadastre-o ou informe um e-mail válido")




def alterar_senha(padrao):
    while True:
        email_encontrado = False
        usuario = input("Informe seu usuario: ")
        
        if usuario not in padrao["usuario"]:
            print(f"O usuario '{usuario}' n esta cadastrado.")
            continue

        email_antigo = input("Informe seu e-mail: ")
        if validar.validar_email(email_antigo):
            for posicao, email_atual in enumerate(padrao["email"]):
                    if email_atual == email_antigo:
                        senha_atual = input("Informe sua senha atual: ")
                        posicao = padrao["email"].index(email_antigo)
                        if padrao["senha"][posicao] != senha_atual:
                            print("Senha atual ta incorreta")
                            continue
                        senha_nova = input("Informe a nova senha: ")
                        padrao["senha"][posicao] = senha_nova
                        print("Senha alterada")
                        email_encontrado = True
                        break
        if email_encontrado:
            break 

        else:
            print(f"O email {email_antigo} não foi encontrado. Cadastre-o ou escreva um email já cadastrado")
            break 