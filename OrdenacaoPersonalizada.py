numeros = []
print("Digite 10 números (um deles deve ser seu número da chamada):")
for i in range(10):
    n = int(input(f"Número {i+1}: "))
    numeros.append(n)

print("Lista original:", numeros)

numeros_ordenados = sorted(numeros)
print("Lista ordenada crescente:", numeros_ordenados)

sem_repetidos = []
for n in numeros:
    if n not in sem_repetidos:
        sem_repetidos.append(n)
print("Lista sem números repetidos:", sem_repetidos)
