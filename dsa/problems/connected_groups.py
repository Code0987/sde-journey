# Problem: Count Groups of Connected People
#
# Relationships between people may be represented in a matrix as a series of binary digits.
# For example, the direct relationships for person 0 with persons 0 through 2 might be shown as "110".
# This means that person 0 knows persons 0 and 1.
#
# A relationship is transitive: if person 0 knows person 1, and person 1 knows person 2,
# then person 0 knows person 2 (even if not directly).
#
# A group is composed of all people who know one another (either directly or transitively).
#
# Task:
# Given an array of binary strings representing the relationship matrix, determine
# the number of groups (connected components) in the graph.

# Function Signature:
# def countGroups(related: List[str]) -> int

# Example:
# Input:
# related = [
#     "110",
#     "110",
#     "001"
# ]
# Output: 2
# Explanation:
# - Persons 0 and 1 are connected (group 1)
# - Person 2 is alone (group 2)

from typing import List


def countGroups(related: List[str]) -> int:
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # Path compression
        return parent[x]

    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            parent[rootY] = rootX  # Union

    n = len(related)
    parent = list(range(n))

    for i in range(n):
        for j in range(n):
            if related[i][j] == "1":
                union(i, j)

    # Count unique roots
    unique_groups = len(set(find(i) for i in range(n)))
    return unique_groups


# Test case
if __name__ == "__main__":
    related = ["110", "110", "001"]
    print("Number of groups:", countGroups(related))  # Expected output: 2
