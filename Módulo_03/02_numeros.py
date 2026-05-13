print("=== Descobrindo o maior número ===")

primeiro = int(input("Digite um número: "))
segundo = int(input("Digite outro número: "))

if primeiro > segundo:
    print(f"O maior número é {primeiro}")

elif segundo > primeiro:
    print(f"O maior número é {segundo}")

else:
    print("Os dois são iguais")