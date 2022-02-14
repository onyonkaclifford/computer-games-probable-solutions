[![tests](https://github.com/onyonkaclifford/computer-games-probable-solutions/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/onyonkaclifford/computer-games-probable-solutions/actions/workflows/tests.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/onyonkaclifford/wordscapes/blob/main/LICENSE)

Possible solutions to select computer games

# Wordscapes

Wordscapes is a mobile game for the android operating system, downloadable from the
[play store](https://play.google.com/store/apps/details?id=com.peoplefun.wordcross)

#### Usage

`python wordscapes.py [--help] --characters CHARACTERS --pattern PATTERN [--wordlist WORDLIST]`

- --characters (-c): scrambled characters from which real words are to be formed
- --pattern (-p): pattern that the words to be formed need to conform to, '+' sign is used when the character at a
particular position is unknown
- --wordlist (-w): path to text file containing a list of words

#### Examples

- `python wordscapes.py -c filyar -p ++++`
- `python wordscapes.py -c filyar -p +++l -w wordlists/2.txt`
- `python wordscapes.py -c filyar -p f++l -w wordlists/1.txt`
- `python wordscapes.py -c filyar -p +a+l -w wordlists/1.txt`

# Wordle

Wordle is a mobile game for the android operating system, downloadable from the
[play store](https://play.google.com/store/apps/details?id=com.wekele.words)

#### Usage

`python wordle.py [--help] --wordlist WORDLIST --pattern PATTERN [--consists-of CONSISTS_OF] [--not-consists-of NOT_CONSISTS_OF]`

- --wordlist (-w): path to text file containing a list of words
- --pattern (-p): pattern that the words to be formed need to conform to, '+' sign is used when the character at a
  particular position is unknown
- --consists-of (-c): characters that need to be present in the words to be formed
- --not-consists-of (-nc): characters that need to be absent in the words to be formed

#### Examples

- `python wordle.py -w wordlists/1.txt -p +++++`
- `python wordle.py -w wordlists/1.txt -p +r+++ -nc cza`
- `python wordle.py -w wordlists/2.txt -p +r+s+ -c rhs`
- `python wordle.py -w wordlists/2.txt -p +rus+ -c rhs -nc cza`

# SortPuz

SortPuz is a mobile game for the android operating system, downloadable from the
[play store](https://play.google.com/store/apps/details?id=sortpuz.water.sort.puzzle.game)

#### Usage

`python sortpuz.py [--help] [--quick] [--hide-progress] [--length LENGTH] FORMATION [FORMATION ...]`

- --quick (-q): whether to use depth first search, which most of the time is quicker, though the resultant solution may
  not be optimal. The default is breadth first search, which is guaranteed to provide an optimal solution, though is
  slower most of the time.
- --hide-progress (-hp): whether to hide progress
- --length (-l): length of a full column
- positional arguments: only one positional argument is used, the arrangement of the colour columns

#### Examples

- `python sortpuz.py o,o o,o`
- `python sortpuz.py -q o,o o,o`

# Tests
To run tests: `python -m doctest -v *.py`

# Attribution
The words in the file `wordlists/1.txt` are sourced from [here](https://github.com/dwyl/english-words/blob/master/words_alpha.txt),
and those in the file `wordlists/2.txt` are sourced from [here](https://www.mit.edu/~ecprice/wordlist.10000)
