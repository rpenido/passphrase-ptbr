#!/usr/bin/env python3
from random import randrange

if __name__ == '__main__':
    file = open('./br-utf8.txt', 'r')
    lines = file.readlines()
    num_lines = len(lines)
    passphrases = []
    input_words = input('How many words do you want in your passphrase? (5): ')
    passphrase_words = int(input_words)
    while len(passphrases) < passphrase_words:
        random_line = randrange(num_lines)
        word = lines[random_line].strip()
        print(f'Word: {word}')
        input_continue = input('Do you want to add this word to your passphrase? (y/N): ')
        if input_continue == 'y':
            passphrases.append(word)
        else:
            continue

    print(f'Passphrase: {" ".join(passphrases)}')
