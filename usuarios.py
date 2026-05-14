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

permissao = str(input("Informe qual o nível de permissão o usuário terá: "))

niveis_permissoes = ["Funcionário", "Cliente", "Gerente", ]