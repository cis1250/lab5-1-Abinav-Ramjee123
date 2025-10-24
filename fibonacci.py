#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
def get_user_input():
    num = int(input("How many terms? "))
    return num

def generate_fibonacci(n):
    a, b = 0, 1
    seq = []
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

def print_sequence(seq):
    for num in seq:
        print(num)

def main():
    n = get_user_input()
    fib = generate_fibonacci(n)
    print_sequence(fib)

main()
