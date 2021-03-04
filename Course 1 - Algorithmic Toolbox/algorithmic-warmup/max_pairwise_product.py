# Description: Find the maximum product of two distinct numbers in a sequence of non-negative integers.

# Input: Two lines. The first line contains an integer n. The second contains n non-negative integers.
# Sample input: 3
#               1 2 3

# Output: The maximum value obtained by multiplying two different elements from the sequence.
# Sample output: 6


def max_pairwise_product(numbers):
	numbers = list(set(numbers))
	numbers.sort()
	return numbers[-1] * numbers[-2]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
