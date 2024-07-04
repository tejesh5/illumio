#method to load the predefined words
def load_predefined_words(file_path):
    predefined_words = set()
    with open(file_path, 'r') as file:
        for word in file.readlines():
            predefined_words.add(word.strip())
    return predefined_words

#method to clean word
def clean_word(word):
    #checking if it is last word of sentence and contains "."
    if word.endswith('.'):
        word = word[:-1]
    return word.strip()

def match_words(input_file_path, predefined_words_file_path):
    predefined_words = load_predefined_words(predefined_words_file_path)
    matched_words = set()

    with open(input_file_path, 'r') as input_file:
        for line in input_file:
            words = line.strip().split()
            for word in words:
                cleaned_word = clean_word(word)
                if cleaned_word in predefined_words:
                    matched_words.add(cleaned_word)

    return matched_words

if __name__ == "__main__":
    # Input text file path
    input_file_path = 'input_texts.txt'
    # Predefined words file path
    predefined_words_file_path = 'predefined_words.txt'

    matched_words = match_words(input_file_path, predefined_words_file_path)
    print(matched_words)
