"""
Problem Statement:
A string `s` of length `n` consists solely of digits from 0–9. Characters in `s` are accessible sequentially, meaning the first occurrence of a digit must be taken from left to right.

You are also given an array `arr` containing `m` strings, where each string consists of digits from 0–9.

For each string in `arr`, determine the **minimum number of characters required from the beginning of `s`** such that a **permutation** of the string from `arr` can be formed using characters from that prefix of `s`.

If the string cannot be formed, return `-1` for that entry.

Return an array of integers where the *i-th* element is the minimum prefix length of `s` needed to form a permutation of the *i-th* string in `arr`. If not possible, return `-1` at that index.

Function Signature:
    def countMinimumCharacters(s: str, arr: List[str]) -> List[int]:

Input:
- s (1 <= len(s) <= 10^5): a string consisting of digits '0'-'9'
- arr (1 <= len(arr) <= 2 * 10^4): a list of strings, each consisting of digits '0'-'9'
- Total length of all strings in arr <= 5 * 10^5

Output:
- A list of integers of length len(arr), where each element is the required minimum prefix length or -1 if not possible.

Example:
    s = "064819848398"
    arr = ["088", "364", "07"]
    Output: [7, 10, -1]

Explanation:
- To form "088", the first 7 characters include '0', '8', '8'.
- To form "364", we need 10 characters from the start to get '3', '6', '4'.
- "07" cannot be formed as '7' is not in `s`.


Tags: Google
"""

from typing import List
from collections import Counter, defaultdict


def countMinimumCharacters(s: str, arr: List[str]) -> List[int]:
    needed_counts = [Counter(word) for word in arr]
    matched_counts = [defaultdict(int) for _ in arr]
    matched_complete = [0] * len(arr)
    result = [-1] * len(arr)

    total_to_match = [len(c) for c in needed_counts]
    completed = [False] * len(arr)
    active = set(range(len(arr)))

    for idx, ch in enumerate(s):
        remove_set = set()
        for i in active:
            if ch in needed_counts[i]:
                if matched_counts[i][ch] < needed_counts[i][ch]:
                    matched_counts[i][ch] += 1
                    if matched_counts[i][ch] == needed_counts[i][ch]:
                        matched_complete[i] += 1
                        if matched_complete[i] == total_to_match[i]:
                            result[i] = idx + 1
                            remove_set.add(i)
        active -= remove_set
        if not active:
            break

    return result


# Example usage
if __name__ == "__main__":
    s = "064819848398"
    arr = ["088", "364", "07"]
    print(countMinimumCharacters(s, arr))  # Output: [7, 10, -1]
