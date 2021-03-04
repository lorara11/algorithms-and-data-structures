# Computes the n-th Fibonacci number.

# Input: A non-negative integer n.
# Output: n-th Fibonacci number.

import sys


def fibonacci_recursion(n):         # Way too slow.
    if (n <= 1):
        return n
    
    return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)
    
    
def fibonacci_list(n):          # More efficient.
    if n <= 1:
        return n
        
    fibonacci = [0,1]
    
    for i in range(2,n+1):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    
    return fibonacci[-1]

   
if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_list(n))
