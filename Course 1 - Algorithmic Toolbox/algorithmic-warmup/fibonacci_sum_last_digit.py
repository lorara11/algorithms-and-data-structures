# Given a non-negative integer n, finds the last digit of the sum 
# F_0 + F_1 + ... + F_n.

# Input: A non-negative integer n.
# Output: Last digit of the sum F_0 + F_1 + ... + F_n.

import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    total_sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        total_sum += current

    return total_sum % 10
    
    
def get_fibonacci_last_digit_with_pisano(n):
    if n <= 1:
        return n

    pisano_period = 60      # Pisano period of 10 is 60
    
    while n >= pisano_period:
        if n % pisano_period != 0:
            n = n % pisano_period
        else:
            break
    
    # Compute the n_th Fibonacci number
    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
    
    return current % 10
    
    
def fibonacci_sum_fast(n):
    # Lemma: for n >= 0, the sum of the n first Fibonacci numbers 
    #        is equal to F_(n+2) - 1.
    
    # We compute the last digit of F_(n+2) and substract 1 to it.
    
    last_digit = get_fibonacci_last_digit_with_pisano(n+2)
    
    if last_digit == 0:
        last_digit = 9
    else:
        last_digit -= 1
        
    return last_digit
    

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_fast(n))
