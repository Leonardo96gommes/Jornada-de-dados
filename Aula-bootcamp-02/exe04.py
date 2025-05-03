#Classificador de Números

def classificar_numero():
    while True:
        try:
            numero = float(input("Digite um número: "))

            if numero > 0:
                print("O número é positivo.")
            elif numero < 0:
                print("O número é negativo")
            else:
                print("O número é zero.")
        except ValueError:
            print("Entrada inválida! Por favor, Digite um número.")
        
        continuar = input("Deseja continuar? (s/n)").strip().lower()
        if continuar != 's':
            print("Programa encerrado.")
            break

classificar_numero()