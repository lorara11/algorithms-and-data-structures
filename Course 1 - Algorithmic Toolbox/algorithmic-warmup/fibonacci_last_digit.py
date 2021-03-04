# Computes the last digit of the n-th Fibonacci number.

# Input: A non-negative integer n.
# Output: the last digit of the n-th Fibonacci number.

import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


def get_fibonacci_last_digit_with_pisano(n):
    if n <= 1:
        return n

    pisano_period = 60      # Pisano period of 10 is 60
    
    while n >= pisano_period:
        if n % pisano_period != 0:
            n = n % pisano_period
        else:
            break

    return get_fibonacci_last_digit_naive(n)


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_with_pisano(n))
