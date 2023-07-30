import socket
import rsa

def programa_cliente():
    host = "192.168.0.100"  # endereço IP dp servidor
    port = 5013

    cliente_socket = socket.socket()
    cliente_socket.connect((host, port))

    chave_publica = (int(cliente_socket.recv(1024).decode('utf-8')), int(cliente_socket.recv(1024).decode('utf-8')))

    print("\nBem-vindo ao ChatBot Criptografado!")
    print("Digite 'sair/' para encerrar o chat.\n")

    while True:
        mensagem = input("Digite sua mensagem: ")
        mensagem_encriptada = rsa.encriptar(mensagem, chave_publica)

        # converte a lista de números inteiros em uma string com os valores separados por espaço
        mensagem_encriptada_str = ' '.join(map(str, mensagem_encriptada))

        cliente_socket.send(mensagem_encriptada_str.encode('utf-8'))

        if mensagem.lower().strip() == "sair/":
            print("\nChat encerrado.")
            break

    cliente_socket.close()

if __name__ == "__main__":
    programa_cliente()
