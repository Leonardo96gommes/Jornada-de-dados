#  Verificador de Palíndromo

# Define uma função chamada 'eh_palindromo' que recebe um texto como parâmetro
def eh_palindromo(texto):
    # Converte o texto para minúsculas e remove espaços e hífens
    texto = texto.lower().replace(" ", "").replace("-", "")
    # Compara o texto com ele mesmo invertido
    return texto == texto[::-1]

while True:
    entrada = input("Digite uma palavra ou frase: ")

    if eh_palindromo(entrada):
        print("✅ É um palíndromo!\n")
    else:
        print("❌ Não é um palíndromo.\n")

    continuar = input("Deseja verificar outra? (s/n): ")
    if continuar.lower() in ["n", "nao", "não"]:
        print("Programa encerrado. Até logo!")
        break
