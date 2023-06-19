def bellmanford(graph, source, n):
    d = {}
    for s, dest, _ in graph:
        d[s] = float("inf")
        d[dest] = float("inf")
    d[source] = 0
    for i in range(n + 1):
        temp = dict(d)
        for start, end, cost in graph:
            temp[end] = min(temp[end], temp[start] + cost)
        if temp == d:
            break
        else:
            d = temp
    return d


graph = [["A", "B", 2], ["A", "C", 5], ["B", "C", 1], ["C", "D", 4], ["B", "D", 3]]

print(bellmanford(graph, "A", 4))
