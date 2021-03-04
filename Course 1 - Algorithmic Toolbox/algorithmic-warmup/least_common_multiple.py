# Computes the least common multiple of two integers a and b.

# Input: Non-negative integers a,b; separated by a space.
# Output: LCM(a,b)

import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b
    
    
def lcm_fast(a,b):
    lcm = a*b
    
    decrease_in = max(a,b)
    n = lcm - decrease_in
    while n > 0:
        if n < lcm and n%a == 0 and n%b == 0:
            lcm = n
            
        n -= decrease_in
        
    return lcm
    
    
if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_fast(a, b))

