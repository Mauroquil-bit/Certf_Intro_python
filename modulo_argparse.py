"""
Please note: for now, when you go to the tab IDE, you can solve this problem only via Pycharm. 
We are sorry for the inconvenience, we will fix this as soon as we can. 
If you prefer to solve the problem via a different IDE, 
you should open it manually and then copy the solution to the website.

Professor Moriarty is causing trouble again! Mary managed to get a file with a piece of his plan, 
but it's encoded. Before she could decode it, Moriarty had taken her hostage and Dr. Watson went to the rescue.

Holmes anticipated that and found a simple Caesar cipher decoder on Stack Overflow to deal with it himself. 
Initially, the file Holmes got from Mary was called "13.txt", 
so he presupposed that this might be the offset n. 
Check this theory but keep in mind that for decoding the offset has to be taken with a minus:

def decode_Caesar_cipher(s, n):
    alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"
    s = s.strip()
    text = ''
    for c in s:
        text += alpha[(alpha.index(c) + n) % len(alpha)]
    print('Decoded text: "' + text + '"')
Holmes, however, doesn't know how to work with files, 
so you must help him! You will be given the file Mary got from Moriarty's laptop. 
Using the code Holmes found, write a program that takes a file as an argument, reads it, decodes it, 
and prints the decoded text. Even though the provided piece of code above contains the phrase "Decoded text: 
" and quotes, please output only the decoded text itself.

If your argument --file is stored in the variable args, 
you can read the file you've passed to your script this way:

filename = args.file
opened_file = open(filename)
encoded_text = opened_file.read()  # read the file into a string
opened_file.close()  # always close the files you've opened
Tip:

This is a tricky task, so let's go through it step by step:

most of the code is already written for you. Use what's in the snippets, 
and add some lines to be able to run it in the command line (to get the arguments, parse them and output the result),
remember that n should be -13,
insert the decoded text without quotes.
"""
import argparse

def decode_Caesar_cipher(s, n):
    alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"
    s = s.strip()
    text = ''
    for c in s:
        text += alpha[(alpha.index(c) - n) % len(alpha)]
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
