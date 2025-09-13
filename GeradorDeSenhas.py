# Q3: Escreva um programa que gere uma senha aleatória de 20 caracteres misturando letras, números e símbolos, porém com uma regra: No meio da senha, o seu nome deverá aparecer.

import random
import string

meuNome = "gustavo"
todos = string.ascii_letters + string.digits + string.punctuation
tamanhoTotal = 20
parteAleatoria_len = tamanhoTotal - len(meuNome)

if parteAleatoria_len < 0:
    print("O nome fixo é maior que 20 caracteres. Ajuste o nome ou o tamanho.")
    
else:
    parteAleatoria = ""
    
    for _ in range(parteAleatoria_len):
        parteAleatoria += random.choice(todos)

    pos = random.randint(0, parteAleatoria_len)
    senha = parteAleatoria[:pos] + meuNome + parteAleatoria[pos:]

    print("Senha gerada:", senha)
