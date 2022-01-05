[![Tests](https://github.com/onyonkaclifford/wordscapes/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/onyonkaclifford/wordscapes/actions/workflows/tests.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/onyonkaclifford/wordscapes/blob/main/LICENSE)

Possible solutions to Wordscapes, a mobile game for the android operating system, downloadable from the
[play store](https://play.google.com/store/apps/details?id=com.peoplefun.wordcross)

## Usage
`python main.py [--help] --wordlist --characters --pattern`

- --wordlist: path to text file containing a list of words (short form is -w)
- --characters: scrambled characters from which real words are to be formed (short form is -c)
- --pattern: pattern that the words to be formed need to conform to (short form is -p), '+' sign is used
when the character at a particular position is unknown

## Examples
- `python main.py -w wordlists/2.txt -c filyar -p ++++`
- `python main.py -w wordlists/2.txt -c filyar -p +++l`
- `python main.py -w wordlists/2.txt -c filyar -p f++l`
- `python main.py -w wordlists/2.txt -c filyar -p +a+l`

## Tests
To run tests: `python -m doctest -v main.py`

## Attribution
The words in the file `wordlists/1.txt` are sourced from [here](https://github.com/dwyl/english-words/blob/master/words_alpha.txt),
and those in file `wordlists/2.txt` are sourced from [here](https://www.mit.edu/~ecprice/wordlist.10000).
