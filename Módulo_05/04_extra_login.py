usuarios = {
    "Stefani": "fanny2026"
}
def login(usuario, senha):
    if usuario in usuarios and usuarios[usuario] == senha:

        print("Login correto")
    else:

        print("Usuário ou senha incorretos")

usuario = input("Usuário: ")
senha = input("Senha: ")
login(usuario, senha)
