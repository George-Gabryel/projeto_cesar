def cadastro():

    import funcoes as f


    perfil = {
        "usuario" : [],
        "email" : [],
        "telefone" : [],
        "senha" : []

    }


    email_usuario = input("Escreva um e-mail válido: ")

    nome_usuario = input("Informe o nome de usuário: ")

    while True:
        try:

            telefone = int(input("Informa um telefone: "))
            break

        except ValueError:
            print("Por favor, digite um número válido válida")
            
    senha = input("Informa uma senha: ")

    inserir_dados = f.inserindo(perfil, email_usuario, nome_usuario, telefone, senha)

    tipo_perfil = ["Funcionário", "Cliente", "Gerente", ]

    while True:
        print(f"Perfis de usuários: {tipo_perfil}")
        permissao = input(f"Informe qual o tipo de perfil do usuário:")
        if permissao == "Funcionário" or permissao == "funcionário" or permissao == "funcionario":
            print("Cadastrado como funcionário")
            break
        elif permissao == "Cliente" or permissao == "cliente":
            print("Cadastrado como cliente")
            break
        elif permissao == "Gerente" or permissao == "gerente":
            print("Cadastrado como gerente")
            break
        else:
            print("Escolha um tipo de permissção válida")
            continue


    print(f"Usuário {perfil['usuario']} cadastrado com suceso")