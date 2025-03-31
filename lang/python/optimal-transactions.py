from collections import defaultdict
from typing import List
from math import inf


def minTransfers(transactions: List[List[int]]) -> int:
    g = defaultdict(int)
    for f, t, x in transactions:
        g[f] -= x
        g[t] += x

    debts = [x for x in g.values() if x]
    n = len(debts)

    def find(i):
        while i < n and debts[i] == 0:
            i += 1

        if i == n:
            return 0

        res = inf

        for j in range(i + 1, n):
            if debts[i] * debts[j] < 0:
                debts[j] += debts[i]
                res = min(res, 1 + find(j))
                debts[j] -= debts[i]

        return res

    res = find(0)

    return res


print(minTransfers([[0, 1, 10], [2, 0, 5]]) == 2)
print(minTransfers([[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]]) == 1)
