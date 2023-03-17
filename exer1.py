def fibonacci(n):
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq

def verifica_fibonacci(num):
    seq = fibonacci(num+1)
    if num in seq:
        return f"{num} pertence à sequência de Fibonacci."
    else:
        return f"{num} não pertence à sequência de Fibonacci."

# Exemplo de uso:
num = int(input("Digite um número inteiro: "))
print(verifica_fibonacci(num))
