# Calculadora Simples

def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    return x / y

1
while True:
    print("\nEscolha a operação:")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")

    try:
        opcao = input("Digite a opção (1/2/3/4): ")

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == '1':
            print("Resultado:", somar(num1, num2))
        elif opcao == '2':
            print("Resultado:", subtrair(num1, num2))
        elif opcao == '3':
            print("Resultado:", multiplicar(num1, num2))
        elif opcao == '4':
            try:
                print("Resultado:", dividir(num1, num2))
            except ZeroDivisionError:
                print("Erro: divisão por zero não é permitida.")
        else:
            print("Opção inválida.")

    except ValueError:
        print("Erro: por favor, digite apenas números válidos.")
    except Exception as e:
        print("Ocorreu um erro inesperado:", e)

    continuar = input("\nDeseja fazer outra operação? (s/n): ").strip().lower()
    if continuar != 's':
        print("Encerrando a calculadora. Até mais!")
        break