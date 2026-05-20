import usuarios as user
import funcoes as fun

print("Bem vindo a tela principal")

while True:
    print("1 - Cadastrar novo usuário \n2 - Visualizar usuários criados \n3 - Alterar usuario \n4 - Sair")
    escolha = int(input("O que você deseja fazer:" ))

    if escolha == 1:
        criar = user.cadastro()
        continue
    elif escolha == 2:
        print(user.padrao)
        continue
    elif escolha == 3:
        print("O que deseja alterar?")
        print("1 - Nome de usuário\n2 - E-mail\n3 - Telefone\n4 - Senha\n5 - Perfil")
        sub_escolha = int(input("Escolha: "))

        if sub_escolha == 1:
            fun.alterar_usuario(user.padrao)
        elif sub_escolha == 2:
            fun.alterar_email(user.padrao)
        elif sub_escolha == 3:
            fun.alterar_telefone(user.padrao)
        elif sub_escolha == 4:
            fun.alterar_senha(user.padrao)
        elif sub_escolha == 5:
            fun.alterar_perfil(user.padrao)
        else:
            print("Opção inválida")
        continue
    elif escolha == 4:
        break

print("Até mais")