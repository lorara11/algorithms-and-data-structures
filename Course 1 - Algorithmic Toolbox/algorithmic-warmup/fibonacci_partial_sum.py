# Given two non-negative integers n and m such that m <= n finds the last digit 
# of the sum F_m + F_(m+1) + ... + F_n.

# Input: two non-negative integers n and m such that m <= n; separated by a space.
# Output: Last digit of the sum F_m + F_(m+1) + ... + F_n.

import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10
    
    
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
    
    
def fibonacci_partial_sum_fast(from_, to):
    # Lemma: for an integer k >= 0, the sum of the k first Fibonacci numbers 
    #        is equal to F_(k+2) - 1.
    
    # We compute the last digit of the sum F_0 + ... + F_(m-1) and substract 
    # it to F_0 + F_1 + ... + F_n.
    # That is, the last digit of F_(to + 2) - 1 - (F_((from_ - 1) + 2) - 1)
    # = F_(to + 2) - F_(from_ + 1)
    
    last_digit_to = get_fibonacci_last_digit_with_pisano(to+2)
    last_digit_from = get_fibonacci_last_digit_with_pisano(from_+1)
    
    if last_digit_to - last_digit_from >= 0:
        return last_digit_to - last_digit_from
    else:
        return 10 + (last_digit_to - last_digit_from)


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_fast(from_, to))
