#!/usr/bin/env python3
from random import randrange

if __name__ == '__main__':
    file = open('./br-utf8.txt', 'r')
    lines = file.readlines()
    num_lines = len(lines)
    passphrases = []
    input_words = input('Quantas palavras você quer em sua senha? (5): ')
    passphrase_words = int(input_words)
    while len(passphrases) < passphrase_words:
        random_line = randrange(num_lines)
        word = lines[random_line].strip()
        print(f'Palavra: {word}')
        input_continue = input('Você quer adicionar esta palavra à sua senha? (y/N): ')
        if input_continue == 'y':
            passphrases.append(word)
        else:
            continue

    print(f'Senha: {" ".join(passphrases)}')
