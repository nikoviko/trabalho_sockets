import socket

# No teste local use '127.0.0.1'. Em duas máquinas, use o IP real do servidor.
IP_SERVIDOR = '127.0.0.1'
PORTA_SERVIDOR = 12000

def run_cliente():
    print("=== Cliente IMC (TCP) ===")
    try:
        peso = input("Digite o peso em kg (ex: 82.5): ").strip()
        altura = input("Digite a altura em metros ou cm (ex: 1.75 ou 175): ").strip()

        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.settimeout(5.0)

        print(f"[*] Conectando a {IP_SERVIDOR}:{PORTA_SERVIDOR}...")
        cliente.connect((IP_SERVIDOR, PORTA_SERVIDOR))

        payload = f"{peso},{altura}"
        cliente.sendall(payload.encode('utf-8'))

        resposta = cliente.recv(1024).decode('utf-8')
        print(f"\n[+] Veredito do Servidor: {resposta}\n")

    except ConnectionRefusedError:
        print("[-] Erro: Servidor não encontrado ou porta fechada.")
    except socket.timeout:
        print("[-] Erro: Tempo de resposta esgotado.")
    except Exception as e:
        print(f"[-] Erro: {e}")
    finally:
        cliente.close()

if __name__ == '__main__':
    run_cliente()