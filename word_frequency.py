import string
from art_title import logo

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

word_count = {}
ordered_dict = {}

#filters out everything we don't need
def filter_text(text):
    remove_punctuation_text = text.translate(str.maketrans('', '', string.punctuation))
    remove_uppercase_text = remove_punctuation_text.lower()
    list_text = remove_uppercase_text.split()
    for word in list_text.copy():
        if word in STOP_WORDS:
            list_text.remove(word)
    return list_text

#counts and adds words to dictionary
def count_words(text):
    for word in text:
        if word_count.get(word) == None:
            word_count[word] = 1
        else:
            word_count[word] += 1

#sorts dictionary
def sort_dict(dictionary):
    ordered_keys = sorted(dictionary, key=dictionary.get, reverse=True)

    for key in ordered_keys[:10]:
        ordered_dict[key] = word_count[key]

#prints list of words
def print_top_words(dictionary):
    print(logo)
    for key, value in dictionary.items():
        stars = ''
        for i in range(value):
            stars += '*'
        print(f"{key} | {value} {stars}")

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file) as open_file:
        read_file = open_file.read()
        text_file = read_file
    # print(text_file)

    filtered_text = filter_text(text_file)
    # print(filtered_text)

    count_words(filtered_text)
    # print(word_count)

    sort_dict(word_count)
    # print(ordered_dict)
    print_top_words(ordered_dict)




if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
