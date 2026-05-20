verificacao = input("Informe o e-mail do usuário que será alterado: ")
   
encontrado = False

for posicao_email, email_atual in enumerate(padrao["email"]):
        if email_atual == verificacao:
            for posicao_usuario in (padrao["usuario"]):
                if posicao_email == posicao_usuario:
                    nome_novo = input("Qual o novo nome: ")
                    padrao["usuario"][posicao_usuario] = nome_novo
                    encontrado = True
                    break

padrao = {
        "usuario" : []
    }

padrao["usuario"[posicao_email]]