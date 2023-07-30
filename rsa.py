import random

def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def inverso_multiplicativo(e, phi):
    d = 0
    x1, x2 = 0, 1
    y1, y2 = 1, 0
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = y2 - temp1 * y1

        x2 = x1
        x1 = x
        y2 = y1
        y1 = y

    if temp_phi == 1:
        d = y2

    return d % phi

def gerar_chaves():
    p = random.choice([17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
    q = random.choice([101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199])

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 3  # o expoente pode ser diferente 3
    while mdc(e, phi) != 1:
        e += 1

    d = inverso_multiplicativo(e, phi)
    return ((e, n), (d, n))

def encriptar(mensagem, chave_publica):
    e, n = chave_publica
    mensagem_encriptada = [pow(ord(char), e, n) for char in mensagem]
    return mensagem_encriptada

def decriptar(mensagem_encriptada, chave_privada):
    d, n = chave_privada
    mensagem_decriptada = [chr(pow(char, d, n)) for char in mensagem_encriptada]
    return ''.join(mensagem_decriptada)

