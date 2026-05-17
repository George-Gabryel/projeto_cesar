import usuarios as user
import funcoes as fun

print("Bem vindo a tela principal")

print("1 - Cadastrar novo usuário \n2 - Visualizar usuários criados",)
escolha = int(input("O que você deseja fazer:" ))

if escolha == 1:
    criar = user.cadastro()

else:
    print(user.perfil)