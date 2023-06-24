#Michał Cynarski
#skończone

def orientation(p, q, r):
    return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])


def left_point(points):
    return min(points, key=lambda p: (p[0], p[1]))


def convex_hull(points):
    hull = []
    start = points.index(left_point(points))
    p = start

    while True:
        hull.append(points[p])
        q = (p + 1) % len(points)

        for r in range(len(points)):
            if orientation(points[p], points[r], points[q]) < 0:
                q = r
        p = q
        if p == start:
            break

    return hull

def convex_hull_v2(points):
    hull = []
    start = points.index(left_point(points))
    p = start

    while True:
        hull.append(points[p])
        q = (p + 1) % len(points)

        for r in range(len(points)):
            if orientation(points[p], points[r], points[q]) == 0:
                if points[p][0] < points[q][0] < points[r][0]:
                    q = r
                elif points[p][0] == points[q][0] == points[r][0] and points[p][1] < points[q][1] < points[r][1]:
                    q = r
                elif points[r][0] < points[q][0] < points[p][0]:
                    q = r
                elif points[r][0] == points[q][0] == points[p][0] and points[r][1] < points[q][1] < points[p][1]:
                    q = r

            elif orientation(points[p], points[r], points[q]) < 0:
                q = r
        p = q
        if p == start:
            break

    return hull


lst = [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]
print(convex_hull(lst))
print(convex_hull_v2(lst))