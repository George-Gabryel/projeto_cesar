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
        telefone = input("Informa um telefone: ")
        if validar.validar_telefone(telefone):
            print("O telefone cadastrado eh: ", telefone)
            break
        else:
            print("Por favor, digite um número válido válida")

    senha = input("Informa uma senha: ")

    tipo_perfil = ["Funcionário", "Cliente", "Gerente", ]

    while True:
        print(f"Perfis de usuários: {tipo_perfil}")
        perfil = input(f"Informe qual o tipo de perfil do usuário:")
        if perfil == "Funcionário" or perfil == "funcionário" or perfil == "funcionario":
            print("Cadastrado como funcionário")
            break
        elif perfil == "Cliente" or perfil == "cliente":
            print("Cadastrado como cliente")
            break
        elif perfil == "Gerente" or perfil == "gerente":
            print("Cadastrado como gerente")
            break
        else:
            print("Escolha um tipo de permissão válida")
            continue

    print(f"Usuário ", perfil," cadastrado com suceso")

    fun.inserindo(padrao, email_usuario, nome_usuario, telefone, senha, perfil)
