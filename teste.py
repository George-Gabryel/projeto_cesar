import validacao as validar


padrao = {
        "usuario" : ["George", "Hugo", "Fábio"],
        "email" : ["george.gabryel07@gmail.com", "hugo.leonardo@gmail.com", "fabio.viana@gmail.com"],
        "telefone" : [],
        "senha" : [],
        "tipo_perfil": []
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

while True:

    telefone = input("Informa um telefone: ")
    if validar.validar_telefone(telefone):
        print("O telefone cadastrado eh: ", telefone)
        break
    else:
        print("Por favor, digite um número válido válida")

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
