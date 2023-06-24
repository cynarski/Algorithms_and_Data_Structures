#Skończone
#Michał Cynarski

def string_compare(P, T, i, j):
    if i == 0:
        return j
    if j == 0:
        return i

    changes = string_compare(P, T, i - 1, j - 1) + int(P[i] != T[j])
    inserts = string_compare(P, T, i, j - 1) + 1
    deletes = string_compare(P, T, i - 1, j) + 1

    lowest_cost = min(changes, inserts, deletes)

    return lowest_cost


def string_compare_pd(P, T, k, l):
    D = [[0] * (len(T)) for _ in range(len(P))]
    for i in range(len(T)):
        D[0][i] = i
    for i in range(len(P)):
        D[i][0] = i
    parents = [["X"] * len(T) for _ in range(len(P))]

    for i in range(1, len(parents[0])):
        parents[0][i] = "I"
    for j in range(1, len(parents)):
        parents[j][0] = "D"

    for i in range(1, k + 1):
        for j in range(1, l + 1):
            changes = D[i - 1][j - 1] + int(P[i] != T[j])
            inserts = D[i][j - 1] + 1
            deletes = D[i - 1][j] + 1
            lowest_cost = min(changes, inserts, deletes)
            D[i][j] = lowest_cost

            if changes <= inserts and changes <= deletes:
                if P[i] == T[j]:
                    parents[i][j] = "M"
                else:
                    parents[i][j] = "S"
            elif inserts < changes and inserts < deletes:
                parents[i][j] = "I"
            else:
                parents[i][j] = "D"
    return D[k][l], parents


def path_reconstruction(R):
    i = len(R) - 1
    j = len(R[0]) - 1
    result = []
    current = R[i][j]
    while current != "X":
        if current == "M" or current == "S":
            i -= 1
            j -= 1
        elif current == "D":
            i -= 1
        else:
            j -= 1
        result.append(current)
        current = R[i][j]
    result.reverse()
    return "".join(result)


def matching_strings(P, T, k, l):
    D = [[0] * (len(T)) for _ in range(len(P))]
    for i in range(len(P)):
        D[i][0] = i
    parents = [["X"] * len(T) for _ in range(len(P))]

    for j in range(1, len(parents)):
        parents[j][0] = "D"

    for i in range(1, len(P)):
        for j in range(1, len(T)):
            changes = D[i - 1][j - 1] + int(P[i] != T[j])
            inserts = D[i][j - 1] + 1
            deletes = D[i - 1][j] + 1
            lowest_cost = min(changes, inserts, deletes)
            D[i][j] = lowest_cost

            if changes <= inserts and changes <= deletes:
                if P[i] == T[j]:
                    parents[i][j] = "M"
                else:
                    parents[i][j] = "S"
            elif inserts < changes and inserts < deletes:
                parents[i][j] = "I"
            else:
                parents[i][j] = "D"
    i_ = len(P) - 1
    j_ = 0
    for k in range(1, len(T)):
        if D[i_][k] < D[i_][j_]:
            j_ = k
    return j_ - len(P) + 2

def longest_common_sequence(P, T, k, l):
    D = [[0] * (len(T)) for _ in range(len(P))]
    for i in range(len(T)):
        D[0][i] = i
    for i in range(len(P)):
        D[i][0] = i
    parents = [["X"] * len(T) for _ in range(len(P))]

    for i in range(1, len(parents[0])):
        parents[0][i] = "I"
    for j in range(1, len(parents)):
        parents[j][0] = "D"

    for i in range(1, k + 1):
        for j in range(1, l + 1):
            if P[i] != T[j]:

                changes = D[i - 1][j - 1] + float('inf')
            else:
                changes = D[i - 1][j - 1]
            inserts = D[i][j - 1] + 1
            deletes = D[i - 1][j] + 1
            lowest_cost = min(changes, inserts, deletes)
            D[i][j] = lowest_cost

            if changes <= inserts and changes <= deletes:
                if P[i] == T[j]:
                    parents[i][j] = "M"
                else:
                    parents[i][j] = "S"
            elif inserts < changes and inserts < deletes:
                parents[i][j] = "I"
            else:
                parents[i][j] = "D"

    result = ''
    for j in range(len(T)):
        for i in range(len(P)):
            if i <= j and parents[i][j] == "M":
                result += T[j]
    return result

def longest_monotonic_subsequence(P, T, k, l):
    D = [[0] * (len(T)) for _ in range(len(P))]
    for i in range(len(T)):
        D[0][i] = i
    for i in range(len(P)):
        D[i][0] = i
    parents = [["X"] * len(T) for _ in range(len(P))]

    for i in range(1, len(parents[0])):
        parents[0][i] = "I"
    for j in range(1, len(parents)):
        parents[j][0] = "D"

    for i in range(1, k + 1):
        for j in range(1, l + 1):
            if P[i] != T[j]:
                changes = D[i - 1][j - 1] + float('inf')
            else:
                changes = D[i - 1][j - 1]
            inserts = D[i][j - 1] + 1
            deletes = D[i - 1][j] + 1
            lowest_cost = min(changes, inserts, deletes)
            D[i][j] = lowest_cost

            if changes <= inserts and changes <= deletes:
                if P[i] == T[j]:
                    parents[i][j] = "M"
                else:
                    parents[i][j] = "S"
            elif inserts < changes and inserts < deletes:
                parents[i][j] = "I"
            else:
                parents[i][j] = "D"

    result = ''
    for j in range(len(T)):
        for i in range(len(P)):
            if j < i and parents[i][j] == "M":
                result += T[j]
    return result

if __name__ == '__main__':
    # a) wariant rekurencyjny
    P = ' kot'
    T = ' pies'
    print(string_compare(P, T, 3, 4))

    # b) wariant PD
    P = ' biały autobus'
    T = ' czarny autokar'
    print(string_compare_pd(P, T, len(P) - 1, len(T) - 1)[0])

    # c) odtwarzanie ścieżki
    P = ' thou shalt not'
    T = ' you should not'
    _, R = string_compare_pd(P, T, len(P) - 1, len(T) - 1)
    result = path_reconstruction(R)
    print(result)

    # d) dopasowanie podciągów
    P = ' ban'
    T = ' mokeyssbanana'
    start_index = matching_strings(P, T, len(P) - 1, len(T) - 1)
    print(start_index)

    # e) najdłuższa wspólna sekwencja
    P = ' democrat'
    T = ' republican'
    result = longest_common_sequence(P, T, len(P) - 1, len(T) - 1)
    print(result)

    # f) najdłuższa podsekwencja monotoniczna
    T = ' 243517698'

    lst = []
    for s in T.lstrip():
        lst.append(int(s))
    lst.sort()

    P = " "
    for v in lst:
        P += str(v)
    print(longest_monotonic_subsequence(P, T, len(P) - 1, len(T) - 1))
