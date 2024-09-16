# Programa para calcular a quantidade de notas de 50, 10 e 1 necessárias para pagar uma conta

# Solicita ao usuário que insira o valor da conta
valor = int(input("Digite o valor da conta: "))

# Calcula a quantidade de notas de 50
notas_50 = valor // 50
resto = valor % 50

# Calcula a quantidade de notas de 10
notas_10 = resto // 10
resto = resto % 10

# Calcula a quantidade de notas de 1
notas_1 = resto

# Exibe o resultado
print("Para pagar a conta de R$",valor, "você precisará de:")
print(notas_50, "nota(s) de 50")
print(notas_10, "nota(s) de 10")
print(notas_1, "nota(s) de 1")
