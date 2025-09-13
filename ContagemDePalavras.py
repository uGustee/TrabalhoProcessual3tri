texto = input("Digite um texto: ")

palavras = texto.split()
qtd = len(palavras)
mais_longa = max(palavras, key=len)

# contar a mais repetida
from collections import Counter
contagem = Counter(palavras)
mais_repetida = contagem.most_common(1)[0][0]

print("Quantidade de palavras:", qtd)
print("Palavra mais longa:", mais_longa)
print("Palavra que mais aparece:", mais_repetida)
