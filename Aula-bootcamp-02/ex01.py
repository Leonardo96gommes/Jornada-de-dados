# Conversor de Temperatura Celsius para Fahrenheit

try:
    C = float(input("Digite a temperatura em Celsius: "))
    F = (C * 9/5) + 32
    print(f"{C}°C equivalem a {F}°F")
except ValueError:
     print("Por favor, digite um número válido.")