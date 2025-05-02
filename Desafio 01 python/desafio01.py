#desafio 1 finalizado

Constante_bonus = 1000

nome = input("Digite seu nome: ")
print("Seu nome digitado é: ", nome)
while True:
    try:
        salario = float(input("Digite seu salário aqui: "))
        print("Seu salário é:", salario)
        break  
    except ValueError:
        print("Entrada inválida! Por favor, digite um número válido.")

while True:
    try:
        bonus = float(input("Digite o valor do bônus recebido: "))
        print("Seu bônus é:", bonus)
        break  
    except ValueError:
        print("Entrada inválida! Por favor, digite um número válido.")


bonus_recebido = Constante_bonus + salario * bonus

print(f"O usuario {nome} possui o bonus de {bonus_recebido}")


