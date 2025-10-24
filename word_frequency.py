#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)



import re

def is_sentence(text):
    if not isinstance(text, str) or not text.strip():
        return False
    if not text[0].isupper():
        return False
    if not re.search(r'[.!?]$', text):
        return False
    if not re.search(r'\w+', text):
        return False
    return True


def get_sentence():
    while True:
        sentence = input("Enter a sentence: ")
        if is_sentence(sentence):
            return sentence
        else:
            print("Invalid sentence. Must start with a capital, end with punctuation (!?.), and contain at least one word.")


def calculate_frequencies(sentence):
    words = re.findall(r'\b\w+\b', sentence.lower())  # extract words
    unique_words = []
    frequencies = []

    for word in words:
        if word in unique_words:
            idx = unique_words.index(word)
            frequencies[idx] += 1
        else:
            unique_words.append(word)
            frequencies.append(1)

    return unique_words, frequencies


def print_frequencies(words, frequencies):
    print("\nWord Frequencies:")
    for word, freq in zip(words, frequencies):
        print(f"{word} : {freq}")


def main():
    sentence = get_sentence()
    words, frequencies = calculate_frequencies(sentence)
    print_frequencies(words, frequencies)


if __name__ == "_main_":
    main()
