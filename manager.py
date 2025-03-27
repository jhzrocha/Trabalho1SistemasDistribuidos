from mpi4py import MPI

def main():
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()
    
    if rank == 0:
        print("Manager iniciado. Enviando tarefas para os workers...")
        for i in range(1, size):
            comm.send(f"Tarefa para worker {i}", dest=i)
            print(f"Tarefa enviada para worker {i}")
    else:
        task = comm.recv(source=0)
        print(f"Worker {rank} recebeu: {task}")

if __name__ == "__main__":
    main()