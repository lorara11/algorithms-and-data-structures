# Computes the greatest common divisor of two integers a and b.

# Input: Non-negative integers a,b; separated by a space.
# Output: GCD(a,b)


import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd
    
    
def euclidean_algorithm(a, b):
    if not a >= b:
        a, b = b, a
    
    if b == 0:
        return a
    
    remainder = a%b
    
    return euclidean_algorithm(b, remainder)


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(euclidean_algorithm(a, b))

