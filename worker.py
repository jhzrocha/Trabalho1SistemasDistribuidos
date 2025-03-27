from mpi4py import MPI

def worker():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    task = comm.recv(source=0)
    print(f"Worker {rank} executando: {task}")

if __name__ == "__main__":
    worker()