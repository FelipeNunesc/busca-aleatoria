import psutil
import time
import random
import struct

def buscar_num(num_procurado, file_path):
    # Iniciar a medição do tempo
    start_time = time.time()

    # Monitorar uso de CPU antes da execução
    process = psutil.Process()
    cpu_times_start = process.cpu_times()

    # Ler o arquivo e realizar a busca
    num_encontrado = False
    with open(file_path, 'rb') as file:
        while chunk := file.read(4):
            numero = struct.unpack('i', chunk)[0]
            if numero == num_procurado:
                num_encontrado = True
                break
    
    # Mostrar o resultado
    if num_encontrado:
        print(f"\n[RESULTADO] O número {num_procurado} \033[92mESTÁ PRESENTE\033[0m no arquivo.")
    else:
        print(f"\n[RESULTADO] O número {num_procurado} \033[91mNÃO FOI ENCONTRADO\033[0m no arquivo.")
    
    # Mostrar o tempo de execução
    end_time = time.time()
    execution_time = end_time - start_time
    
    # Monitorar uso de CPU após a execução
    cpu_times_end = process.cpu_times()
    
    # Cálculo do tempo total de CPU usado
    cpu_user_time = cpu_times_end.user - cpu_times_start.user
    cpu_system_time = cpu_times_end.system - cpu_times_start.system
    cpu_total_time = cpu_user_time + cpu_system_time

    # Normalizando pelo número de núcleos da CPU
    num_cores = psutil.cpu_count(logical=False)  # Número de núcleos físicos
    cpu_usage = (cpu_total_time / execution_time) * 100 / num_cores

    # Monitorar uso de RAM após a busca
    memory_usage = psutil.Process().memory_info().rss / (1024 * 1024)
    
    print(f"\n[PERFORMANCE]")
    print(f"  - Tempo de execução: {execution_time:.6f} segundos")
    print(f"  - Uso de CPU: {cpu_usage:.2f}%")
    print(f"  - Uso de RAM: {memory_usage:.2f} MB\n")

def main():
    while True:
        # Solicitar ao usuário que escolha o tamanho do arquivo para busca
        print("Escolha o tamanho do arquivo para a busca:")
        print("1 - 1 milhão de números")
        print("2 - 1 bilhão de números")
        print("3 - 1 trilhão de números")
        
        escolha = input("Digite o número correspondente à sua escolha: ")
        
        tam_aquivo = 0
        if escolha == '1':
            file_path = 'numbers/1M.bin'
            tam_aquivo = 1_000_000
        elif escolha == '2':
            file_path = 'numbers/1B.bin'
            tam_aquivo = 1_000_000_000
        elif escolha == '3':
            file_path = 'numbers/1T.bin'
            tam_aquivo = 1_000_000_000_000
        else:
            print("Escolha inválida. Saindo do programa.")
            return
        
        # Especificar o número a ser procurado
        num_procurado = random.randint(1, tam_aquivo)

        # Executar a função de busca e monitoramento
        buscar_num(num_procurado, file_path)

        # Perguntar ao usuário se deseja realizar outra busca ou sair
        repetir = input("Deseja procurar outro número? (s/n): ")
        if repetir.lower() != 's':
            print("Saindo do programa. Até mais!")
            break

if __name__ == "__main__":
    main()