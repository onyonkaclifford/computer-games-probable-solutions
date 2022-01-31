[![Tests](https://github.com/onyonkaclifford/wordscapes/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/onyonkaclifford/wordscapes/actions/workflows/tests.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/onyonkaclifford/wordscapes/blob/main/LICENSE)

Possible solutions to Wordscapes, a mobile game for the android operating system, downloadable from the
[play store](https://play.google.com/store/apps/details?id=com.peoplefun.wordcross)

## Usage
`python wordscapes.py [--help] --characters CHARACTERS --pattern PATTERN [--wordlist WORDLIST]`

- --characters (-c): scrambled characters from which real words are to be formed
- --pattern (-p): pattern that the words to be formed need to conform to, '+' sign is used when the character at a
particular position is unknown
- --wordlist (-w): path to text file containing a list of words

## Examples
- `python wordscapes.py -c filyar -p ++++`
- `python wordscapes.py -c filyar -p +++l -w wordlists/2.txt`
- `python wordscapes.py -c filyar -p f++l -w wordlists/1.txt`
- `python wordscapes.py -c filyar -p +a+l -w wordlists/1.txt`

## Tests
To run tests: `python -m doctest -v wordscapes.py`

## Attribution
The words in the file `wordlists/1.txt` are sourced from [here](https://github.com/dwyl/english-words/blob/master/words_alpha.txt),
and those in file `wordlists/2.txt` are sourced from [here](https://www.mit.edu/~ecprice/wordlist.10000).
