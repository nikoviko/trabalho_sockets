import socket

HOST = '0.0.0.0'
PORTA = 12000

def calcular_imc(peso: float, altura: float) -> str:
    # Trata altura se informada em centímetros
    if altura > 3.0:
        altura = altura / 100.0

    if altura <= 0:
        return "Erro: Altura deve ser maior que zero."

    imc = peso / (altura ** 2)
    classificacao = "Fat" if imc >= 25.0 else "Thin"
    return f"{classificacao} (IMC: {imc:.2f})"

def run_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    servidor.bind((HOST, PORTA))
    servidor.listen(1)
    print(f"[*] Servidor TCP escutando em 0.0.0.0:{PORTA}...")

    while True:
        conexao, endereco = servidor.accept()
        print(f"[+] Conexão recebida de {endereco[0]}:{endereco[1]}")

        try:
            dados = conexao.recv(1024).decode('utf-8').strip()
            if not dados:
                continue

            print(f"    Payload recebido: '{dados}'")

            partes = dados.split(',')
            if len(partes) == 2:
                peso = float(partes[0].strip())
                altura = float(partes[1].strip())
                resultado = calcular_imc(peso, altura)
            else:
                resultado = "Erro: Formato inválido. Use 'peso,altura'."

            conexao.sendall(resultado.encode('utf-8'))
            print(f"    Resposta enviada: '{resultado}'")

        except ValueError:
            erro = "Erro: Peso e altura precisam ser numéricos."
            conexao.sendall(erro.encode('utf-8'))
        except Exception as e:
            print(f"[-] Erro interno: {e}")
        finally:
            conexao.close()
            print(f"[-] Conexão com {endereco[0]} fechada.\n")

if __name__ == '__main__':
    run_servidor()