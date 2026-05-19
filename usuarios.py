#Dicionário com todos os usuários
perfil = {
        "usuario" : ["George", "Fábio"],
        "email" : ["george.gabryel07@gmai.com"],
        "telefone" : ["81973169780"],
        "senha" : ["gsgs"],
        "tipo_perfil": ["Funcionário"]

    }


#Criando novo usuário
# def cadastro():


#     import funcoes as f
#     import validacao as email
#     while True:
#         email_usuario = input("Escreva um e-mail válido: ")
#         if email.validar_email(email_usuario):
#             print("")
#             break
#         else:
#             print("Email inválido")
#             continue

#     nome_usuario = input("Informe o nome de usuário: ")

#     while True:
#         try:

#             telefone = int(input("Informa um telefone: "))
#             break

#         except ValueError:
#             print("Por favor, digite um número válido válida")
            
#     senha = input("Informa uma senha: ")

#     inserir_dados = f.inserindo(perfil, email_usuario, nome_usuario, telefone, senha, tipo_perfil)

#     tipo_perfil = ["Funcionário", "Cliente", "Gerente", ]

#     while True:
#         print(f"Perfis de usuários: {tipo_perfil}")
#         permissao = input(f"Informe qual o tipo de perfil do usuário:")
#         if permissao == "Funcionário" or permissao == "funcionário" or permissao == "funcionario":
#             print("Cadastrado como funcionário")
#             break
#         elif permissao == "Cliente" or permissao == "cliente":
#             print("Cadastrado como cliente")
#             break
#         elif permissao == "Gerente" or permissao == "gerente":
#             print("Cadastrado como gerente")
#             break
#         else:
#             print("Escolha um tipo de permissção válida")
#             continue


#     print(f"Usuário {perfil['usuario']} cadastrado com suceso")

# Atualizando informações

while True:
    
        nome_antigo = input("Qual nome deseja alterar: ")
        nome_novo = input("Qual o novo nome: ")
        
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

              

                


print(perfil["usuario"])