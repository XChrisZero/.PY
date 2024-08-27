login = input("Digite o seu login:")
senha = input("Digite sua senha: ")
if login == "user1" and senha == "teste01":
    print("Bem-vindo user1")
elif login == "user2" and senha == "teste02":
    print("Bem-vindo user2")
elif login == "user3" and senha == "teste03":
    print("Bem-vindo user3")
elif login == "user4" and senha == "teste04":
    print("Bem-vindo user4")
else:
    print("Login falhou!")
    print("verifique sua senha e tente novamente!")
