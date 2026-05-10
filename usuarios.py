import funcoes as f


perfil = {
    "usuario" : [],
    "email" : [],
    "telefone" : [],
    "senha" : []

}

email_usuario = input("Escreva um e-mail válido: ")

nome_usuario = input("Informe o nome de usuário: ")

senha = input("Informa uma senha: ")

telefone = int(input("Informa uma senha: "))

inserir_dados = f.inserindo(perfil, email_usuario, nome_usuario, senha, telefone)

