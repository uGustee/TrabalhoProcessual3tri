# Q1: O usuário digita um texto e o programa deve:
  # - Contar quantas palavras existem;
  # - Mostrar a palavra mais longa;
  # - Mostrar a palavra que mais aparece.

texto = input("Digite um texto: ")
palavras = texto.split()

quantidadePalavras = len(palavras)

maisLonga = palavras[0]
for p in palavras:
    if len(p) > len(maisLonga):
        maisLonga = p

contagem = {}
for p in palavras:
    if p in contagem:
        contagem[p] += 1
    else:
        contagem[p] = 1

maisAparece = None
maiorCcontagem = 0
for p in contagem:
    if contagem[p] > maiorContagem:
        maiorContagem = contagem[p]
        maisAparece = p

print("Quantidade de palavras:", quantidadePalavras)
print("Palavra mais longa:", maisLonga)
print("Palavra que mais aparece:", maisAparece)
