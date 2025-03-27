from mpi4py import MPI

def main():
    comm = MPI.COMM_WORLD  # Comunicador global
    rank = comm.Get_rank()  # Identificador do processo
    size = comm.Get_size()  # Número total de processos

    if rank == 0:  # Processo manager
        number = 10  # Número a ser enviado ao worker
        print(f"Manager enviando o número: {number}")
        comm.send(number, dest=1, tag=11)  # Envia número para o worker
        result = comm.recv(source=1, tag=22)  # Recebe o resultado do worker
        print(f"Manager recebeu o resultado: {result}")  # Exibe o resultado

    elif rank == 1:  # Processo worker
        number = comm.recv(source=0, tag=11)  # Recebe o número do manager
        print(f"Worker recebeu o número: {number}")
        result = number * 2  # Multiplica o número por 2
        comm.send(result, dest=0, tag=22)  # Envia o resultado de volta ao manager

if __name__ == "__main__":
    main()