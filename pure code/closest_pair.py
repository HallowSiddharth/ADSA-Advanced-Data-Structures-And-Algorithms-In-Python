def findmin(l):
    if len(l) == 1:
        return 0
    m = float("inf")
    for i in l:
        for j in l:
            if i != j:
                dist = ((i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2) ** 0.5
                if dist < m:
                    m = dist
    return m


def closestpair(points):
    if len(points) <= 3:
        return findmin(points)
    mid = len(points) // 2
    left = points[:mid]
    right = points[mid:]
    ld = closestpair(left)
    rd = closestpair(right)
    d = min(ld, rd)
    midpt = points[mid]
    strip = []
    for i in points:
        if abs(i[0] - midpt[0]) < d:
            strip.append(i)
    new_d = findmin(strip)
    return min(d, new_d)


points = [[1, 2], [2, 3], [5, 6], [7, 9], [4, 5]]
points = sorted(points, key=lambda x: x[0])
print("minimum distance: ", closestpair(points))
