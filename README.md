# Passphrase PT-BR

Um gerador de senhas em formato de frases usando dicionário português brasileiro.

A passphrase generator using a Brazilian Portuguese dictionary.

## Descrição / Description

Este projeto gera senhas seguras em formato de frases usando palavras aleatórias do dicionário português brasileiro. O script é interativo, permitindo ao usuário escolher quais palavras incluir na sua passphrase.

This project generates secure passphrases using random words from a Brazilian Portuguese dictionary. The script is interactive, allowing the user to choose which words to include in their passphrase.

## Características / Features

- Dicionário com **261.798 palavras** em português brasileiro
- Geração aleatória de palavras
- Interface interativa para seleção de palavras
- Criação de senhas seguras e fáceis de memorizar
- Script simples em Python 3

---

- Dictionary with **261,798 words** in Brazilian Portuguese
- Random word generation
- Interactive interface for word selection
- Creation of secure and memorable passwords
- Simple Python 3 script

## Requisitos / Requirements

- Python 3.x

## Instalação / Installation

1. Clone o repositório / Clone the repository:
```bash
git clone https://github.com/rpenido/passphrase-ptbr.git
cd passphrase-ptbr
```

2. Execute o script / Run the script:
```bash
python3 passphrase.py
```

## Como usar / How to use

1. Execute o script:
```bash
python3 passphrase.py
```

2. Digite o número de palavras desejadas na sua passphrase (padrão: 5):
```
How many words do you want in your passphrase? (5): 4
```

3. Para cada palavra apresentada, digite `y` para aceitar ou pressione Enter para recusar:
```
Word: exemplo
Do you want to add this word to your passphrase? (y/N): y
```

4. Ao final, sua passphrase será exibida:
```
Passphrase: exemplo palavra segura memoravel
```

## Exemplo de uso / Usage example

```bash
$ python3 passphrase.py
How many words do you want in your passphrase? (5): 3
Word: enriquecia
Do you want to add this word to your passphrase? (y/N): y
Word: apeteci
Do you want to add this word to your passphrase? (y/N): y
Word: impressionarias
Do you want to add this word to your passphrase? (y/N): y
Passphrase: enriquecia apeteci impressionarias
```

## Licença / License

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

