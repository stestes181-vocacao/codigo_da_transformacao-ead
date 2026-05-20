try:
    idade = int(input("Digite sua idade: "))
#sem dar negativo
    if idade < 0:
        print("❌ A idade não pode dar erro.")

    else:
        print(f"✅ Idade cadastrada com sucesso: {idade} anos.")

except ValueError:
    print("❌ Erro: digite apenas números inteiros.")