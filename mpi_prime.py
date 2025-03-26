from mpi4py import MPI
import numpy as np

# Inicializando MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
print(rank)
print(size)

# Verificar se o número de processos é maior que 1
#if size <= 1:
#   print("Erro: O número de processos MPI deve ser maior que 1!")


# Definir o número máximo a ser testado
N = 10000000000000

# Dividir o trabalho entre os processos
step = N // (size - 1)
start = rank * step + 1
end = (rank + 1) * step if rank != size - 1 else N

# Criar a lista de números a serem testados
primes = []
for num in range(start, end + 1):
    if all(num % i != 0 for i in range(2, num)):
        primes.append(num)

# Coletar os resultados no processo root (gerente)
all_primes = comm.gather(primes, root=0)

# O processo root imprime os números primos encontrados
if rank == 0:
    primes_flat = [prime for sublist in all_primes for prime in sublist]
    primes_flat.sort()
    print("Números primos encontrados:", primes_flat)