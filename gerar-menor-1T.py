import random
import struct

# Definir quantidades menores que 1 trilhão
num_quant = 1000000

# Escrever todos os números inteiros no formato binario no arquivo
with open('1mTeste2.bin', 'wb') as file:
    for _ in range(num_quant):
        num_aleatorio = random.randint(0,num_quant)
        file.write(struct.pack('i', num_aleatorio))

print("Arquivo criado com sucesso.")