# Conversão de Tipo com Validação

N = input("Digite um numero: ")

try:
    N = int(N)
    print(f"Você digitou o número: {N}")
except ValueError:
    print("Erro: Isso não é um número inteiro válido.")