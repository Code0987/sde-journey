"""
Problem:
There are N clients who have ordered N handmade items. The K-th client ordered exactly one item that takes T[K] hours to make.

There is only one employee who makes items for clients, and they work in the following manner:

Spend one hour making the first item;

If the item is finished, the employee delivers it to the client immediately;

If the item is not finished, it is placed at the end of the queue for further work;

The employee then starts working on the next item in line.


Example:
For example, if T = [3, 1, 2], the employee spends 6 hours making items in the following order:

Work order by hour: [1, 2, 3, 1, 3, 1]

Client 1's item (which takes 3 hours) is finished at hour 6.
Client 2's item (1 hour) is finished at hour 2.
Client 3's item (2 hours) is finished at hour 5.

Total waiting time = 6 + 2 + 5 = 13


solution([3, 1, 2]) should return 13
solution([1, 2, 3, 4]) should return 24
solution([7, 7, 7]) should return 60
solution([10000]) should return 10000


Constraints:
1 <= N <= 100,000
1 <= T[i] <= 10,000 for each i


Tags: Microsoft
"""


def solution(T):
    MOD = 10**9
    from collections import deque

    n = len(T)
    idx_T = list(enumerate(T))
    queue = deque(idx_T)

    time = 0
    wait_times = [0] * n

    while queue:
        i, t = queue.popleft()
        t -= 1
        time += 1
        if t == 0:
            wait_times[i] = time
        else:
            queue.append((i, t))

    return sum(wait_times) % MOD


print(solution([3, 1, 2]))  # Output: 13
print(solution([1, 2, 3, 4]))  # Output: 24
print(solution([7, 7, 7]))  # Output: 60
print(solution([10000]))  # Output: 10000
