import funcoes as fun
import validacao as validar

padrao = {
        "usuario" : [],
        "email" : [],
        "telefone" : [],
        "senha" : [],
        "tipo_perfil": []
    }

def cadastro():
    while True:
        email_usuario = input("Escreva um e-mail válido: ")
        if validar.validar_email(email_usuario):
            print("O email cadastrado eh: ", email_usuario)
            break
        else:
            print("Email inválido")
            continue
        

    nome_usuario = input("Informe o nome de usuário: ")

    while True:
        
        telefone_usuario = input("Informa um telefone: ")
        if validar.validar_telefone(telefone_usuario):
            print("O telefone cadastrado eh: ", telefone_usuario)
            break
        else:
            print("Por favor, digite um número válido")

    senha_usuario = input("Informa uma senha: ")

    tipo_perfil = ["Funcionário", "Cliente", "Gerente", ]

    while True:
        print(f"Perfis de usuários: {tipo_perfil}")
        perfil_usuario = input(f"Informe qual o tipo de perfil do usuário:")
        if perfil_usuario == "Funcionário" or perfil_usuario == "funcionário" or perfil_usuario == "funcionario":
            print("Cadastrado como funcionário")
            break
        elif perfil_usuario == "Cliente" or perfil_usuario == "cliente":
            print("Cadastrado como cliente")
            break
        elif perfil_usuario == "Gerente" or perfil_usuario == "gerente":
            print("Cadastrado como gerente")
            break
        else:
            print("Escolha um tipo de permissão válida")
            continue

    print(f"Usuário ", perfil_usuario," cadastrado com suceso")

    fun.inserindo(padrao, email_usuario, nome_usuario, telefone_usuario, senha_usuario, perfil_usuario)
