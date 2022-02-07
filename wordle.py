import argparse


def get_most_probable_words(wordlist, consists_of, not_consists_of, pattern):
    """Get a list of most probable words

    >>> with open("wordlists/2.txt", "r") as file: word_list = file.read().split()
    >>> get_most_probable_words(word_list, "lai", "peno", "+rail")
    ['trail']

    :param wordlist: wordlist to use
    :param consists_of: characters that need to be present
    :param not_consists_of: characters that need to be absent
    :param pattern: pattern to match against
    :returns: list of probable words
    """
    consists_of = consists_of.lower()
    not_consists_of = not_consists_of.lower()
    pattern = pattern.lower()

    results = []
    len_of_pattern = len(pattern)
    count_of_consists_of_characters = {i: consists_of.count(i) for i in consists_of}
    non_empty_indices_in_pattern = {i: char for i, char in enumerate(pattern) if char != "+"}

    for word in wordlist:
        to_skip = False
        if len(word) != len_of_pattern:
            continue

        for char in consists_of:
            if char not in word or word.count(char) > count_of_consists_of_characters[char]:
                to_skip = True
                break
        if to_skip:
            continue

        for char in not_consists_of:
            if char in word:
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

    parser.add_argument("-w", "--wordlist", type=str, required=True, help="Path to wordlist text file")
    parser.add_argument("-p", "--pattern", type=str, required=True, help="Pattern to match against")
    parser.add_argument("-c", "--consists-of", type=str, default="", help="Characters that need to be present")
    parser.add_argument("-nc", "--not-consists-of", type=str, default="", help="Characters that need to be absent")

    args = parser.parse_args()

    with open(args.wordlist, "r") as f:
        english_words = f.read().split()

    most_probable_words = get_most_probable_words(english_words, args.consists_of, args.not_consists_of, args.pattern)

    print(most_probable_words)
