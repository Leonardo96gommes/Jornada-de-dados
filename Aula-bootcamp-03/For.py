words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))


nome = ['Luciano']
for letra in nome:
    print(letra)


nome = 'Luciano'
for letra in nome:
    print(letra)


for i in range(5):
    print(i)


list(range(5, 10))           # [5, 6, 7, 8, 9]
list(range(0, 10, 3))        # [0, 3, 6, 9]
list(range(-10, -100, -30))  # [-10, -40, -70]


a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])


texto = "a raposa marrom salta sobre o cachorro preguiçoso"
# ...
print(contagem_palavras)


numeros = [10, 20, 30, 40, 50]
# ...
print(normalizados)


usuarios_validos = [usuario for usuario in usuarios if usuario["email"]]


pares = [x for x in numeros if x % 2 == 0]


vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800}
]

total_por_categoria = {}
for venda in vendas:
    categoria = venda["categoria"]
    valor = venda["valor"]
    if categoria in total_por_categoria:
        total_por_categoria[categoria] += valor
    else:
        total_por_categoria[categoria] = valor

print(total_por_categoria)
