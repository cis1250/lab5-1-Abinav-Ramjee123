#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)



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
