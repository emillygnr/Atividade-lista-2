num = int(input("Digite um número inteiro: "))
binario = ""

while num > 0:
    resto = num % 2
    binario = str(resto) + binario
    num = num // 2

print("O número em binário é:", binario)