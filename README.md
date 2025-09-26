# passphrase-ptbr

🔐 A Portuguese-Brazilian interactive passphrase generator using a comprehensive dictionary with over 260,000 words.

## Overview

This tool generates secure passphrases using Portuguese-Brazilian words, making them easier to remember while maintaining security. The generator allows users to interactively select words from a comprehensive dictionary, ensuring both security and usability.

## Features

- 🇧🇷 **Portuguese-Brazilian dictionary**: Uses a comprehensive dictionary with 261,798 words
- 🔄 **Interactive selection**: Choose whether to include each suggested word in your passphrase
- 🎲 **Random word generation**: Cryptographically secure random word selection
- ✨ **Customizable length**: Choose the number of words in your passphrase (default: 5)
- 📝 **Clean output**: Generates space-separated passphrases ready for use

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/rpenido/passphrase-ptbr.git
   cd passphrase-ptbr
   ```

2. Make the script executable (optional):
   ```bash
   chmod +x passphrase.py
   ```

## Usage

Run the passphrase generator:

```bash
python3 passphrase.py
```

### Example Session

```
$ python3 passphrase.py
How many words do you want in your passphrase? (5): 4
Word: biblioteca
Do you want to add this word to your passphrase? (y/N): y
Word: tartaruga
Do you want to add this word to your passphrase? (y/N): y
Word: montanha
Do you want to add this word to your passphrase? (y/N): y
Word: chocolate
Do you want to add this word to your passphrase? (y/N): y
Passphrase: biblioteca tartaruga montanha chocolate
```

### Usage Tips

- **Default length**: Press Enter to use the default 5-word passphrase
- **Word selection**: Type `y` and press Enter to accept a word, or just press Enter (or `N`) to skip
- **Security**: Longer passphrases with more words are more secure
- **Memorability**: Choose words that are meaningful or easy to remember for you

## Dictionary

The `br-utf8.txt` file contains a comprehensive Portuguese-Brazilian dictionary with:
- **261,798 unique words**
- **UTF-8 encoding** for proper Portuguese character support
- **Diverse vocabulary** including common words, proper nouns, and technical terms
- **Clean format** with one word per line

## Security Considerations

- Each word is selected using Python's `random.randrange()` function
- The large dictionary size (261,798 words) provides substantial entropy
- A 4-word passphrase provides approximately 72 bits of entropy
- A 5-word passphrase provides approximately 90 bits of entropy
- Interactive selection allows you to avoid words that might be easily guessed

## File Structure

```
passphrase-ptbr/
├── README.md           # This file
├── LICENSE            # MIT License
├── passphrase.py      # Main passphrase generator script
├── br-utf8.txt        # Portuguese-Brazilian dictionary
└── .gitignore         # Git ignore rules
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Areas for contribution:
- Code improvements and optimizations
- Additional dictionary sources
- Enhanced security features
- User interface improvements
- Documentation updates

## Author

**Rômulo Penido** - Initial work

## Acknowledgments

- Portuguese-Brazilian dictionary contributors
- Python community for the excellent standard library

---

*Made with ❤️ for the Portuguese-speaking community*