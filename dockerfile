# Usar a imagem base do Python
FROM python:3.9

# Instalar dependências do sistema para MPICH ou Open MPI
RUN apt-get update && apt-get install -y \
    build-essential \
    libopenmpi-dev \
    && rm -rf /var/lib/apt/lists/*  # Limpar cache de pacotes após instalação

# Instalar mpi4py e numpy
RUN pip install mpi4py numpy

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o código Python para dentro do container
COPY mpi_prime.py /app

# Definir o comando padrão (isso será sobrescrito no docker-compose)
CMD ["python", "mpi_prime.py"]