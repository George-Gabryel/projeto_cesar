import validacao as validar


padrao = {
        "usuario" : ["George", "Hugo", "Fábio"],
        "email" : ["george.gabryel07@gmail.com", "hugo.leonardo@gmail.com", "fabio.viana@gmail.com"],
        "telefone" : ["81973169780", "81996287191"],
        "senha" : ["gsgs07", "gsgs11"],
        "tipo_perfil": ["Cliente", "Gerente"]
    }

# verificacao = input("Informe o e-mail do usuário que será alterado: ")
   
# encontrado = False

# for posicao_email, email_atual in enumerate(padrao["email"]):
#         if email_atual == verificacao:
#             for posicao_usuario, usuario in enumerate(padrao["usuario"]):
#                 if posicao_usuario == posicao_email:
#                     print("Nome de usuário -->", padrao["usuario"][posicao_email])
#                     usuario = input("Qual será o novo nome do usuário:  ")
#                     padrao["usuario"][posicao_email] = usuario
#                     encontrado = True
#                     break


# # print(padrao["usuario"])
# email_antigo = input("Qual email sera alterado: ")
# if validar.validar_email(email_antigo):


#     while True:
#         email_encontrado = False # Variável de controle
        
#         for posicao, email_atual in enumerate(padrao["email"]):
#             if email_atual == email_antigo:
#                 email_novo = input("Qual será o novo email: ")
                
#                 if validar.validar_email(email_novo):
#                     padrao["email"][posicao] = email_novo
#                     print("Email alterado")
                    
#                     email_encontrado = True
#                     break  # Para o loop 'for' pois já achou e alterou
#                 else:
#                     print("Email inválido. Tente novamente.")
#                     # Aqui você decide se quer dar break ou tentar de novo
        
#         if email_encontrado:
#             break # Para o loop 'while True' se desejar encerrar o programa
#         else:
#             print("E-mail antigo não encontrado.")
#             break # Para evitar loop infinito caso não queira pedir o email_antigo de novo

# else:
#     print("Email não reconhecido. Tente novamente e escreva um email válido")




# email_antigo = input("Qual e-mail você deseja alterar o telefone cadastrado: ")

# if validar.validar_email(email_antigo):
#     while True:
#             telefone_encontrado = False # Variável de controle
            
#             for posicao, email_atual in enumerate(padrao["email"]):
#                 if email_atual == email_antigo:
#                     print(f"Telefone cadastrado --> {padrao["telefone"][posicao]}")
#                     telefone_novo = input("Qual será o novo telefone: ")
                    
#                     if validar.validar_telefone(telefone_novo):
#                         padrao["telefone"][posicao] = telefone_novo
#                         print("Telefone Alterado com sucesso!!")
#                         telefone_encontrado = True
#                         break # Para o loop 'for' pois já achou e alterou
#                     else:
#                         print("Telefone inválido. Tente novamente.")
#                         # Aqui você decide se quer dar break ou tentar de novo
            
#             if telefone_encontrado:
#                 break # Para o loop 'while True' se desejar encerrar o programa
#             else:
#                 print(f"O telefone {email_antigo} não foi encontrado. Cadastre-o ou escreva um telefone já cadastrado")
#                 break # Para evitar loop infinito caso não queira pedir o email_antigo de novo

# else:
#     print(f"O email {email_antigo} não foi encontrado. Cadastre-o ou escreva um email válido")


# while True:
#         email_encontrado = False
#         usuario = input("Informe seu usuario: ")
        
#         if usuario not in padrao["usuario"]:
#             print(f"O usuario '{usuario}' n esta cadastrado.")
#             continue

#         email_antigo = input("Informe seu e-mail: ")
#         if validar.validar_email(email_antigo):
#             for posicao, email_atual in enumerate(padrao["email"]):
#                     if email_atual == email_antigo:
#                         senha_atual = input("Informe sua senha atual: ")
#                         posicao = padrao["email"].index(email_antigo)
#                         if padrao["senha"][posicao] != senha_atual:
#                             print("Senha atual ta incorreta")
#                             continue
#                         senha_nova = input("Informe a nova senha: ")
#                         padrao["senha"][posicao] = senha_nova
#                         print("Senha alterada")
#                         email_encontrado = True
#                         break
#         if email_encontrado:
#             break 

#         else:
#             print(f"O email {email_antigo} não foi encontrado. Cadastre-o ou escreva um email já cadastrado")
#             break 


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
                        print("1 - Sim \n2 - Não")
                        validar_remocao = int(input("Tem certeza que deseja remover os registros desse usuário:"))
                        if validar_remocao == 1:
                            padrao["email"].pop(posicao)
                            padrao["usuario"].pop(posicao)
                            padrao["telefone"].pop(posicao)
                            padrao["senha"].pop(posicao)
                            padrao["tipo_perfil"].pop(posicao)
                            print("Remoção realizada com sucesso")
                            email_encontrado = True
                            break
                        elif validar_remocao == 2:
                            print("Remoção Cancelada")
                            break
                        else:
                            print("Opção inválida")
                            break

        if email_encontrado:
            break

        else:
            print(f"O email {email_antigo} não foi encontrado. Cadastre-o ou escreva um email já cadastrado")
            break 