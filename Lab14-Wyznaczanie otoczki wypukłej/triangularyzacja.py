#Michał Cynarski
#skończone

import time
import math


def calculate_triangle_cost(p1, p2, p3):
    side1 = math.dist(p1, p2)
    side2 = math.dist(p2, p3)
    side3 = math.dist(p3, p1)
    triangle_cost = side1 + side2 + side3
    return triangle_cost

def triangle_cost_recursive(points, i, j):
    if j - i + 1 < 3:
        return 0

    min_cost = math.inf

    for k in range(i + 1, j):
        triangle_cost = calculate_triangle_cost(points[i], points[k], points[j])
        left_cost = triangle_cost_recursive(points, i, k)
        right_cost = triangle_cost_recursive(points, k, j)
        total_cost = triangle_cost + left_cost + right_cost

        if total_cost < min_cost:
            min_cost = total_cost

    return min_cost

def triangle_cost_dynamic(points):
    n = len(points)
    dp = [[0] * n for _ in range(n)]

    for gap in range(2, n):
        for i in range(n - gap):
            j = i + gap
            dp[i][j] = math.inf

            for k in range(i + 1, j):
                triangle_cost = calculate_triangle_cost(points[i], points[k], points[j])
                total_cost = triangle_cost + dp[i][k] + dp[k][j]

                if total_cost < dp[i][j]:
                    dp[i][j] = total_cost

    return dp[0][n-1]


figure1 = [[0, 0], [1, 0], [2, 1], [1, 2], [0, 2]]
figure2 = [[0, 0], [4, 0], [5, 4], [4, 5], [2, 5], [1, 4], [0, 3], [0, 2]]
t_start = time.perf_counter()
print("Koszt:", round(triangle_cost_recursive(figure1, 0, len(figure1) - 1),4))
t_stop = time.perf_counter()
print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

t_start = time.perf_counter()
print("Koszt:", round(triangle_cost_recursive(figure2, 0, len(figure2) - 1),4))
t_stop = time.perf_counter()
print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

t_start = time.perf_counter()
print("Koszt:", round(triangle_cost_dynamic(figure1),4))
t_stop = time.perf_counter()
print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

t_start = time.perf_counter()
print("Koszt:", round(triangle_cost_dynamic(figure2),4))
t_stop = time.perf_counter()
print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
