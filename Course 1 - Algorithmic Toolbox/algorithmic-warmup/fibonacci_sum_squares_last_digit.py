# Given a non-negative integer n, compute the last digit of 
# (F_O)**2 + (F_1)**2 + ... + (F_n)**2.

# Input: a non-negative integer n.
# Output: the last digit of (F_O)**2 + (F_1)**2 + ... + (F_n)**2.


from sys import stdin


def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

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


def fibonacci_sum_squares_with_rectangle(n):
    # Lemma: (F_O)**2 + (F_1)**2 + ... + (F_n)**2 = F_n * F_(n+1)
    
    # We compute the last digit of F_n * F_(n+1)
    
    last_digit_1 = get_fibonacci_last_digit_with_pisano(n)
    last_digit_2 = get_fibonacci_last_digit_with_pisano(n+1)
    
    return (last_digit_1 * last_digit_2) % 10


if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_with_rectangle(n))
    
