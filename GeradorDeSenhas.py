import random
import string

nome = input("Digite seu nome: ")

caracteres = string.ascii_letters + string.digits + string.punctuation

senha_base = ''.join(random.choice(caracteres) for _ in range(20 - len(nome)))

pos = random.randint(0, len(senha_base))
senha = senha_base[:pos] + nome + senha_base[pos:]

print("Senha gerada:", senha)
