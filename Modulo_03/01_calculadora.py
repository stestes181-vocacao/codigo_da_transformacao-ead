print("=== Calculadora Básica ===")

# Entrada
A = float(input("Me diga um valor: "))
B = float(input("Me diga outro valor: "))

# Processo
Soma = A + B
Subtracao = A - B
Multiplicacao = A * B

# Saída
print("\n---Resultados---")
print(f"{A} + {B} = {Soma}")
print(f"{A} - {B} = {Subtracao}")
print(f"{A} * {B} = {Multiplicacao}")

# Verificação
if B == 0:
    print("Divisão: Não é possível dividir por zero")

else:
    Divisao = A / B
    print(f"{A} / {B} = {Divisao}")