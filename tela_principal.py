import usuarios as user
import funcoes as fun

print("Bem vindo a tela principal")

while True:
    print("1 - Cadastrar novo usuário \n2 - Visualizar usuários criados \n3 - Sair")
    escolha = int(input("O que você deseja fazer:" ))

    if escolha == 1:
        criar = user.cadastro()
        continue
    elif escolha == 2:
        print(user.perfil)
        continue
    elif escolha == 3:
        break

print("Até mais")