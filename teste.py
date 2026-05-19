import validacao as email

perfil = {
        "usuario" : [],
        "email" : ["george.gabryel07@gmail.com"],
        "telefone" : [],
        "senha" : [],
        "tipo_perfil": []

    }


while True:
    
        a = input("Qual e-mail será alterado: ")
        b = input("Qual será o novo e-mail do usuário: ")
        
        if email.validar_email(b):
            print("")
            break
        else:
            print("Email inválido")
            continue
        
        validar = False
        
        for c, d in enumerate(perfil["email"]):
            if d == a:
                perfil["email"][c] = b
                validar = True
                break
        if validar:
            print(f"O e-mail foi alterado com sucesso!")
            break
        else:
            print(f"O e-mail {a} não está cadastrado. Cadastre-o ou informe um e-mail válido")

print(perfil["email"])