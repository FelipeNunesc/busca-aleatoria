import random
import struct

# Definir quantidades de 1 bilhão
num_quant = 1000000000

# Escrever todos os números inteiros no formato binario no arquivo
with open('numbers/1B.bin', 'wb') as file:
    for _ in range(num_quant):
        num_aleatorio = random.randint(0,num_quant)
        file.write(struct.pack('i', num_aleatorio))

print("Arquivo criado com sucesso.")