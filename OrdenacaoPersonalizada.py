numeros = []
for i in range(10):
    n = int(input("Digite um número (um deles deve ser seu número da chamada): "))
    numeros.append(n)

print("Lista original:", numeros)
print("Lista crescente:", sorted(numeros))
print("Lista sem repetidos:", list(set(numeros)))
