# Q2: O usuário digita 10 números, sendo que um deles deve ser o seu número da chamada. Armazene em uma lista e depois mostre:
    # - A lista original;
    # - A lista ordenada crescente;
    # - A lista sem números repetidos.

numeros = []

print("Digite 10 números (um deles deve ser seu número da chamada):")
for i in range(10):
    n = int(input(f"Número {i+1}: "))
    numeros.append(n)

print("Lista original:", numeros)

numerosOrdenados = sorted(numeros)

print("Lista ordenada crescente:", numerosOrdenados)

semRepetidos = []

for n in numeros:
    if n not in semRepetidos:
        semRepetidos.append(n)
print("Lista sem números repetidos:", semRepetidos)
