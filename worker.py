import socket

HOST = "0.0.0.0"
PORT = 5000

def isNumeroPrimo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()

        while True:
            conn, addr = s.accept()
            print(f"Conectado a {addr}")
            with conn:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break

                    number = int(data.decode())
                    print(f"Recebido número {number} do manager")

                    if isNumeroPrimo(number):
                        print(f"{number} é Primo")
                        conn.sendall(str(number).encode())
                    else:
                        print(f"{number} não é Primo")
                        conn.sendall(b"-1")

if __name__ == "__main__":
    main()
