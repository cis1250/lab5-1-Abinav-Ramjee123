#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
# Fibonacci Sequence Exercise with functions

def get_user_input():
    while True:
        user_input = input("Enter how many Fibonacci terms you want: ")
        
        if user_input.isdigit():
            num = int(user_input)
            if num > 0:
                return num
            else:
                print("Please enter a positive number.")
        else:
            print("Invalid input. Please enter a positive integer.")


def generate_fibonacci(n):
    sequence = []
    first, second = 0, 1
    
    for _ in range(n):
        sequence.append(first)
        first, second = second, first + second

    return sequence


def print_sequence(sequence):
    print("\nFibonacci Sequence:")
    for number in sequence:
        print(number)


def main():
    num_terms = get_user_input()
    fib_sequence = generate_fibonacci(num_terms)
    print_sequence(fib_sequence)

main()
