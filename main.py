
from mpi4py import MPI
import numpy as np

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(start, end):
    return [n for n in range(start, end) if is_prime(n)]

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    # Gerente: distribui tarefas
    N = 1000  # Limite superior da busca
    step = N // (size - 1)
    results = []
    for i in range(1, size):
        start = (i - 1) * step
        end = start + step if i < size - 1 else N
        comm.send((start, end), dest=i)
    
    # Recebe os resultados
    for i in range(1, size):
        primes = comm.recv(source=i)
        results.extend(primes)
    
    # Ordena e exibe os primos encontrados
    results.sort()
    print("Números primos encontrados:", results)
else:
    # Trabalhadores: recebem intervalo e calculam primos
    start, end = comm.recv(source=0)
    primes = find_primes(start, end)
    comm.send(primes, dest=0)

# Criando o docker-compose.yml
with open("docker-compose.yml", "w") as f:
    f.write("""
version: '3.8'
services:
  manager:
    build: .
    container_name: mpi_manager
    command: mpirun --hostfile /etc/hosts -np 3 python mpi_prime.py
    networks:
      - mpinet
  worker:
    build: .
    deploy:
      replicas: 2
    networks:
      - mpinet
networks:
  mpinet:
    driver: bridge
""")
