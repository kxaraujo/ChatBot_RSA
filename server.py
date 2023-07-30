import socket
import rsa

def programa_servidor():
    host = socket.gethostname()
    port = 5013

    servidor_socket = socket.socket()
    servidor_socket.bind((host, port))
    servidor_socket.listen(2)
    conn, endereco = servidor_socket.accept()
    print("Conexão de: " + str(endereco))

    chave_publica, chave_privada = rsa.gerar_chaves()

    # envia o expoente de criptografia para o cliente
    conn.send(str(chave_publica[0]).encode('utf-8'))
    conn.send(str(chave_publica[1]).encode('utf-8'))

    print("\nBem-vindo ao ChatBot Criptografado!")
    print("Digite 'sair/' para encerrar o chat.\n")

    while True:
        data = conn.recv(1024).decode('utf-8')
        if not data:
            break

        mensagem_encriptada = [int(char) for char in data.split()]
        mensagem_decriptografada = rsa.decriptar(mensagem_encriptada, chave_privada)

        print("Mensagem criptografada recebida: " + data)
        print("Mensagem decriptografada: " + mensagem_decriptografada)

        if mensagem_decriptografada.lower().strip() == "sair/":
            print("\nChat encerrado pelo cliente.")
            break

    conn.close()

if __name__ == "__main__":
    programa_servidor()
