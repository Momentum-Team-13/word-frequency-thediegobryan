import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

word_count = {}

def filter_text(text):
    remove_punctuation_text = text.translate(str.maketrans('', '', string.punctuation))
    remove_uppercase_text = remove_punctuation_text.lower()
    list_text = remove_uppercase_text.split()
    for stop_word in STOP_WORDS:
        for word in list_text:
            if stop_word == word:
                list_text.remove(word)
    return list_text

# def count_words(text):
#     for word in text:

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file) as open_file:
        read_file = open_file.read()
        text_file = read_file
    # print(text_file)

    filtered_text = filter_text(text_file)
    print(filtered_text)
    # count_words(filtered_text)


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
