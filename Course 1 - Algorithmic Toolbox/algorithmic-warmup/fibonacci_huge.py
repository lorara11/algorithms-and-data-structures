# Given two integers n and m, outputs F_n mod m

# Input: two integers n >= 1 and m >= 2 (separated by a space)
# Output: F_n mod m

import sys


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m    


def pisano_period(m):
    counter = 0
    
    previous, current = 0, 1
    
    while not (previous == 0 and current == 1 and (counter > 0)):
        #when sequence returns to 0, 1; period goes over again, so we stop counting
        previous, current = current, (previous + current) % m
        counter += 1
    
    return counter


def fibonacci_modulo(n, m):
    if n <= 1:
        return n
    
    pisano = pisano_period(m)
            
    while n >= pisano:
        if n % pisano != 0:
            n = n % pisano
        else:
            break
        
    return get_fibonacci_huge_naive(n,m)
    


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(fibonacci_modulo(n, m))
