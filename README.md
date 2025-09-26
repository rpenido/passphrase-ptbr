# Passphrase PT-BR

Um gerador de senhas em formato de frases usando dicionário português brasileiro.

## Descrição

Este projeto gera senhas seguras em formato de frases usando palavras aleatórias do dicionário português brasileiro. O script é interativo, permitindo ao usuário escolher quais palavras incluir na sua passphrase.

## Características

- Dicionário com **261.798 palavras** em português brasileiro
- Geração aleatória de palavras
- Interface interativa para seleção de palavras
- Criação de senhas seguras e fáceis de memorizar
- Script simples em Python 3
- **Entropia de segurança:**
  - 3 palavras: 54.0 bits
  - 4 palavras: 72.0 bits
  - 5 palavras: 90.0 bits

## Requisitos

- Python 3.x
- Não utiliza dependências externas (apenas a biblioteca padrão do Python)

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/rpenido/passphrase-ptbr.git
cd passphrase-ptbr
```

2. Execute o script:
```bash
python3 passphrase.py
```

## Como usar

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

## Exemplo de uso

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

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

