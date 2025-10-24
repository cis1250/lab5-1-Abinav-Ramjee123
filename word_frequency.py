#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

def get_sentence():
    while True:
        sentence = input("Enter a sentence: ").strip()
        if is_sentence(sentence):
            return sentence
        else:
            print(" Invalid sentence! It must start with a capital letter and end with '.', '?', or '!'. Try again.\n")

# Function 2: Calculate word frequencies
def calculate_frequencies(sentence):
    # Remove the ending punctuation (. ? !)
    if sentence[-1] in ".!?":
        sentence = sentence[:-1]

    # Split into words
    words = sentence.split()

    # Lists to store unique words and their frequencies
    word_list = []
    freq_list = []

    for w in words:
        w = w.lower()  # case-insensitive
        if w in word_list:
            index = word_list.index(w)
            freq_list[index] += 1
        else:
            word_list.append(w)
            freq_list.append(1)

    return word_list, freq_list

# Function 3: Display the results
def print_frequencies(words, frequencies):
    print("\n Word Frequencies:")
    for i in range(len(words)):
        print(f"{words[i]}: {frequencies[i]}")

# Main function to control the program flow
def main():
    sentence = get_sentence()
    words, freqs = calculate_frequencies(sentence)
    print_frequencies(words, freqs)

# Entry point
if __name__ == "_main_":
    main()
