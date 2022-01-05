import argparse


def get_all_possible_words(characters, length_of_words):
    """Get a list of all words, real and fabricated, of a certain length from the list of characters given

    >>> get_all_possible_words("filyar", 2)
    ['fi', 'fl', 'fy', 'fa', 'fr', 'if', 'il', 'iy', 'ia', 'ir', 'lf', 'li', 'ly', 'la', 'lr', 'yf', 'yi', 'yl', 'ya', \
'yr', 'af', 'ai', 'al', 'ay', 'ar', 'rf', 'ri', 'rl', 'ry', 'ra']

    :param characters: string of scrambled characters
    :param length_of_words: length of words to be formed
    :return: list of words
    """
    if length_of_words == 0:
        return []

    choices = [i for i in characters]
    num_of_occurrences = {}
    current_length_of_words = 1

    for i in characters:
        if i not in num_of_occurrences:
            num_of_occurrences[i] = 1
        else:
            num_of_occurrences[i] += 1

    while current_length_of_words < length_of_words:
        replacement_choices = []

        for i, value in enumerate(choices):
            [
                replacement_choices.append(f"{choices[i]}{j}") for j in characters
                if value.count(j) < num_of_occurrences[j] and f"{choices[i]}{j}" not in replacement_choices
            ]

        choices = replacement_choices
        current_length_of_words += 1

    return choices


def get_filtered_words(words, wordlist_file_path, pattern):
    """Get a list of words that have been filtered based on being matched to some wordlist and some pattern

    >>> get_filtered_words(["fraz", "fail", "past", "msdkl"], "wordlists/2.txt", "+a+l")
    ['fail']

    :param words: list of unfiltered words
    :param wordlist_file_path: path to text file containing wordlist to use
    :param pattern: pattern to match against the unfiltered words
    :return: list of filtered words
    """
    results = []
    len_of_pattern = len(pattern)
    non_empty_indices_in_pattern = {i: char for i, char in enumerate(pattern) if char != "+"}

    with open(wordlist_file_path, "r") as f:
        english_words_list = f.read().split()  # Should convert to lowercase in case wordlist uses capital letters

    for word in words:
        if len(word) != len_of_pattern:
            continue

        for idx, char in non_empty_indices_in_pattern.items():
            if word[idx] != char:
                break
        else:
            if word in english_words_list:
                results.append(word)

    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-w", "--wordlist", type=str, required=True,
        help="Path to file containing English words"
    )
    parser.add_argument(
        "-c", "--characters", type=str, required=True,
        help="Scrambled characters from which English words are to be formed"
    )
    parser.add_argument(
        "-p", "--pattern", type=str, required=True,
        help="Pattern that the English words to be formed need to conform to"
    )

    args = parser.parse_args()
    wordlist_to_use = args.wordlist
    scrambled_characters = args.characters.lower()
    pattern_to_use = args.pattern
    length_of_word_being_sought = len(pattern_to_use)

    all_possible_words = get_all_possible_words(scrambled_characters, length_of_word_being_sought)
    most_probable_required_words = get_filtered_words(all_possible_words, wordlist_to_use, pattern_to_use)

    print(most_probable_required_words)
