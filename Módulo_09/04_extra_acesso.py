usuario_correto = "fanny"
senha_correta = "2026"

tentativas = 3

while tentativas > 0:

    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("✅ Login realizado com sucesso!")
        break

    else:
        tentativas -= 1

        print(
            f"❌ Credenciais inválidas. Tentativas restantes: {tentativas}"
        )

if tentativas == 0:
    print("🔒 Conta bloqueada por excesso de tentativas.")