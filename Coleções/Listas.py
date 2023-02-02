carros = ["Ford", "Fiat", "Kia"]

for elemento, carro in enumerate(carros):
    print(f"carro: {carro} elemento: {elemento}")

numeros = [2, 10, 5, 9, 11, 23, 25]
divididos_por_cinco = [numero for numero in numeros if numero % 5 == 0]

print(divididos_por_cinco)