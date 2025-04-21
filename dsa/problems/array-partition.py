"""
Problem Statement:
You are given an array A consisting of N integers. The elements of the array represent the strength of each link in a chain. Your task is to divide this chain into three smaller chains by breaking it at exactly two non-adjacent positions.

More precisely, you must break the chain at two positions P and Q such that:

0 < P < Q < N - 1

Q > P + 1 (i.e., the breaks must be non-adjacent)

After breaking the chain at positions P and Q, it will be split into three subchains:

A[0] to A[P - 1]

A[P + 1] to A[Q - 1]

A[Q + 1] to A[N - 1]

The cost of breaking the chain at positions P and Q is A[P] + A[Q].

Write a function:

def solution(A):

that takes an array A of integers and returns the minimum cost of dividing the chain into three pieces.


Example:

A = [5, 2, 4, 6, 3, 7]
Possible valid breaks:

Break at (1, 3): Cost = 2 + 6 = 8
Break at (1, 4): Cost = 2 + 3 = 5 ← (minimum)
Break at (2, 4): Cost = 4 + 3 = 7

So the function should return:
5


Constraints:
N will be at least 5
You must write an efficient algorithm to handle large inputs


Tags: Microsoft
"""


def solution(A):
    N = len(A)
    min_cost = float("inf")

    # Precompute the minimum values of A[0]..A[i] for i = 1 to N-3
    min_prefix = [0] * N
    min_prefix[1] = A[1]
    for i in range(2, N - 2):
        min_prefix[i] = min(min_prefix[i - 1], A[i])

    # Try all valid Q from P + 2 to N - 2
    for Q in range(3, N - 1):
        P = Q - 2
        min_P = min_prefix[P]
        cost = min_P + A[Q]
        min_cost = min(min_cost, cost)

    return min_cost


A = [5, 2, 4, 6, 3, 7]
print(solution(A))  # Output: 5
