import random

# Definir quantidades e nome da pasta
quant_num = 1000000000
nome_pasta = 'nums-bi.txt'

# Gerar a lista de um milhão números aleatórios
numeros = [str(random.randint(0, 1000000)) for i in range(quant_num)]

# Escrever todos os números no arquivo, separados por quebras de linha
with open(nome_pasta, 'w') as file:
    file.write('\n'.join(numeros))
print("Arquivo criado com sucesso.")