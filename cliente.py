import socket

def init_client():
    HOST = '' # substituir pelo endereço ip do pc do servidor
    PORT = 12000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM)as s:
        try:
            s.connect((HOST,PORT))
            print("conectado ao servidor\n")

            peso = input("introduza o seu peso em kg's: ")
            altura = input("introduza a sua altura em metros (ex.: 1.80): ")

            mensagem = f"{peso},{altura}"
            s.sendall(mensagem.encode('utf-8'))

            data = s.recv(1024)

            print(f"\nresultado: {data.decode('utf-8')}")
        except ConnectionRefusedError:
            print("erro")

if __name__ == "__main__":
    init_client()