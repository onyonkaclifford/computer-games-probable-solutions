import argparse


def get_wordlist_of_all_possible_words(characters, length_of_words):
    """Get a list of all words, real and fabricated, of a certain length from the list of characters given

    >>> get_wordlist_of_all_possible_words("filyar", 2)
    ['fi', 'fl', 'fy', 'fa', 'fr', 'if', 'il', 'iy', 'ia', 'ir', 'lf', 'li', 'ly', 'la', 'lr', 'yf', 'yi', 'yl', 'ya', \
'yr', 'af', 'ai', 'al', 'ay', 'ar', 'rf', 'ri', 'rl', 'ry', 'ra']

    :param characters: string of scrambled characters
    :param length_of_words: length of words to be formed
    :return: list of words
    """
    characters = characters.lower()

    if length_of_words == 0:
        return []

    wordlist = [i for i in characters]
    num_of_occurrences = {}
    current_length_of_words = 1

    for i in characters:
        if i not in num_of_occurrences:
            num_of_occurrences[i] = 1
        else:
            num_of_occurrences[i] += 1

    while current_length_of_words < length_of_words:
        replacement_wordlist = []

        for i, value in enumerate(wordlist):
            [
                replacement_wordlist.append(f"{wordlist[i]}{j}") for j in characters
                if value.count(j) < num_of_occurrences[j] and f"{wordlist[i]}{j}" not in replacement_wordlist
            ]

        wordlist = replacement_wordlist
        current_length_of_words += 1

    return wordlist


def get_most_probable_words(wordlist, characters, pattern):
    """Get a list of most probable words

    >>> word_list = ["trail", "banana", "frail", "drain"]
    >>> get_most_probable_words(word_list, "+rail")
    ['trail', 'frail']

    :param wordlist: wordlist to use
    :param characters: scrambled characters
    :param pattern: pattern to match against
    :returns: list of probable words
    """
    characters = characters.lower()
    pattern = pattern.lower()

    results = []
    len_of_pattern = len(pattern)
    non_empty_indices_in_pattern = {i: char for i, char in enumerate(pattern) if char != "+"}

    for word in wordlist:
        to_skip = False
        if len(word) != len_of_pattern:
            continue

        for char in word:
            if char not in characters:
                to_skip = True
                break
        if to_skip:
            continue

        for idx, char in non_empty_indices_in_pattern.items():
            if word[idx] != char:
                break
        else:
            results.append(word)

    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-c", "--characters", type=str, required=True, help="Scrambled characters")
    parser.add_argument("-p", "--pattern", type=str, required=True, help="Pattern to match against")
    parser.add_argument("-w", "--wordlist", type=str, default="", help="Path to wordlist text file")

    args = parser.parse_args()

    if args.wordlist != "":
        with open(args.wordlist, "r") as f:
            wordlist_to_use = f.read().split()
    else:
        wordlist_to_use = get_wordlist_of_all_possible_words(args.characters, len(args.pattern))

    most_probable_words = get_most_probable_words(wordlist_to_use, args.characters, args.pattern)

    print(most_probable_words)
