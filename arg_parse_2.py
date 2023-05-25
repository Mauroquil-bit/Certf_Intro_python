import argparse

def decode_Caesar_cipher(s, n):
    alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"
    s = s.strip()
    text = ''
    for c in s:
        if c in alpha:
            text += alpha[(alpha.index(c) - n) % len(alpha)]
        else:
            text += c
    return text

def main():
    parser = argparse.ArgumentParser(description='Decodificador de Cifrado César')
    parser.add_argument('file', type=str, help='Ruta del archivo a decodificar')
    args = parser.parse_args()

    filename = args.file
    try:
        with open(filename) as file:
            encoded_text = file.read()
    except FileNotFoundError:
        print(f"El archivo '{filename}' no existe.")
        return

    decoded_text = decode_Caesar_cipher(encoded_text, 13)  # Decodificar con desplazamiento -13

    print(decoded_text)

if __name__ == '__main__':
    main()
