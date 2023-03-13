while True:
    num = int(input("Digite um número inteiro: "))

    for i in range(1, num + 1):
        soma = 0
        for j in range(1, i):
            if i % j == 0:
                soma += j
        if soma == i:
            print(i)

    resposta = input("Deseja continuar? (sim/não): ")
    if resposta.lower() != "sim":
        break