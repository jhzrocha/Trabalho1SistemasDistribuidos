# Usa a imagem base Ubuntu com MPICH
FROM ubuntu:22.04

# Instala dependências
RUN apt-get update && apt-get install -y \
    python3 python3-pip mpich

# Instala mpi4py
RUN pip3 install mpi4py

# Cria diretório de trabalho
WORKDIR /app

# Copia o código para dentro do contêiner
COPY mpi_prime.py /app/mpi_prime.py

# Comando padrão de execução
CMD ["mpiexec", "-n", "2", "python3", "/app/mpi_prime.py"]