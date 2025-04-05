# Usa a imagem base Ubuntu com MPICH
FROM ubuntu:22.04

# Instala dependências
RUN apt-get update && apt-get install -y \
    python3 python3-pip mpich

# Instala mpi4py
RUN pip3 install mpi4py
