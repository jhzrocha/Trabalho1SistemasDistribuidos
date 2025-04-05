import socket
import time  # Para tentar reconectar em caso de erro

HOST = "worker"
PORT = 5000
LIMIT = 5000

numerosPrimos = []

def isNumeroPrimo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                print("Tentando conectar ao worker...")
                s.connect((HOST, PORT))
                print("Conectado!")

                # Adiciona o 2 à lista de números primos
                numerosPrimos.append(2)

                contador = 3  # Começa em 3 pois o 2 já foi adicionado
                while contador <= LIMIT:
                    
                    s.sendall(str(contador).encode())
                    data = s.recv(1024).decode()
                    
                    if data and data != "-1":
                        numerosPrimos.append(int(data))
                    
                    (f"Testando {contador+2}")
                    if (isNumeroPrimo(contador+2)):
                        numerosPrimos.append(int(contador+2))
                        print(f"{contador+2} é Primo")
                    contador += 4
                break
                
        except ConnectionRefusedError:
            print("Erro de conexão")
    print(numerosPrimos)

if __name__ == "__main__":
    main()
