import time


def shortest(start, graph, n):

    INF = 1_000_000_000

    dist = [INF] * n
    visited = [False] * n

    dist[start] = 0

    for _ in range(n):

        u = -1
        best = INF

        for i in range(n):

            if not visited[i] and dist[i] < best:
                best = dist[i]
                u = i

        if u == -1:
            break

        visited[u] = True

        for v, w in graph[u]:

            new_dist = dist[u] + w

            if new_dist < dist[v]:
                dist[v] = new_dist

    return dist


n = 100

graph = [[] for _ in range(n)]


for i in range(n):

    for j in range(n):

        if i != j:

            weight = (
                ((i + 1) * 37 + (j + 1) * 17)
                % 97
            ) + 1

            graph[i].append((j, weight))


start = time.perf_counter()

distances = shortest(0, graph, n)

end = time.perf_counter()


print("RESULT:", distances[99])
print("TIME:", (end - start) * 1000.0)
