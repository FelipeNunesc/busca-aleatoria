import psutil
import time
import random
import struct

def monitor():
    process = psutil.Process()
    cpu_usage = process.cpu_percent(interval=1)
    memory_usage = process.memory_info().rss / (1024 * 1024)
    return cpu_usage, memory_usage

def buscar_num(num_procurado):
    # Iniciar a medição do tempo
    start_time = time.time()
    
    # Ler o arquivo e realiza busca
    num_encontrado = False
    with open('teste-1T.bin', 'rb') as file:
        while chunk := file.read(4):
            numero = struct.unpack('i', chunk)[0]
            if numero == num_procurado:
                num_encontrado = True
                break

    if num_encontrado:
        print(f"\n[RESULTADO] O número {num_procurado} \033[92mESTÁ PRESENTE\033[0m no arquivo.")
    else:
        print(f"\n[RESULTADO] O número {num_procurado} \033[91mNÃO FOI ENCONTRADO\033[0m no arquivo.")
    
    
    # Mostrar o tempo de execução
    end_time = time.time()
    execution_time = end_time - start_time

    # Monitorar uso de CPU e RAM
    cpu_usage, memory_usage = monitor()

    print(f"\n[PERFORMANCE]")
    print(f"  - Tempo de execução: {execution_time:.6f} segundos")
    print(f"  - Uso de CPU: {cpu_usage:.2f}%")
    print(f"  - Uso de RAM: {memory_usage:.2f} MB\n")

# Especificar o número a ser procurado
num_procurado = random.randint(0, 1000000)

# Executar a função de busca e monitoramento
buscar_num(num_procurado)