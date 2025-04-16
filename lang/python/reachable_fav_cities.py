from collections import defaultdict, deque


def reachable_fav_cities(n_cities, time_to_reach, fav_cities, start):
    graph = defaultdict(list)
    for u, v, t in time_to_reach:
        graph[u].append((v, t))

    results = defaultdict(list)

    min_times = [float("inf")] * n_cities
    q = deque([(0, start)])
    while q:
        time, city = q.popleft()

        if min_times[city] <= time:
            continue
        min_times[city] = time

        if city in fav_cities:
            results[time].append(city)

        for neighbor, t in graph[city]:
            q.append((time + t, neighbor))

    min_time = min(results.keys(), default=float("inf"))
    if min_time == float("inf"):
        res_cities = []
    else:
        res_cities = results[min_time] if results else []

    return min_time, res_cities


# Test cases
def test_reachable_fav_cities():
    n_cities = 5
    time_to_reach = [
        (0, 1, 2),
        (1, 2, 3),
        (0, 3, 4),
        (3, 4, 1),
        (2, 4, 5),
    ]
    # Graph:
    # 0 --2--> 1 --3--> 2
    # |         |        |
    # 4         4        5
    # |         |        |
    # 3 --1--> 4 <------|

    assert reachable_fav_cities(n_cities, time_to_reach, {2, 4}, 0) == (5, [2, 4])
    assert reachable_fav_cities(n_cities, time_to_reach, {2}, 0) == (5, [2])
    assert reachable_fav_cities(n_cities, time_to_reach, {4}, 0) == (5, [4])
    assert reachable_fav_cities(n_cities, time_to_reach, {1}, 0) == (2, [1])
    assert reachable_fav_cities(n_cities, time_to_reach, {0}, 0) == (0, [0])
    assert reachable_fav_cities(n_cities, time_to_reach, {3}, 0) == (4, [3])
    assert reachable_fav_cities(n_cities, time_to_reach, {5}, 0) == (float("inf"), [])
    assert reachable_fav_cities(n_cities, time_to_reach, {0, 1}, 0) == (0, [0])

test_reachable_fav_cities()