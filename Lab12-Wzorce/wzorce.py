import time

with open("lotr.txt", encoding='utf-8') as f:
    text = f.readlines()

S = ' '.join(text).lower()

def naiwna(S, W):
    m, i = 0, 0
    counter = 0
    found = []
    while m + len(W) < len(S) + 1:
        flag = True
        i = 0
        while i < len(W):
            counter += 1
            if not S[m + i] == W[i]:
                flag = False
                break
            else:
                i += 1
        if flag:
            found.append(m)
        m += 1
    return len(found), counter



def hash(word):
    N = len(word)
    d = 256
    q = 101
    hw = 0
    for i in range(N):
        hw = (hw*d + ord(word[i])) % q
    return hw

def Rabin_Karp(S,W):
    M = len(S)
    N = len(W)
    d = 256
    q = 101
    found = []
    counter = 0
    collisions = 0
    hW = hash(W)

    h = 1
    for i in range(N - 1):
        h = (h * d) % q

    for m in range(M - N + 1):
        hS = hash(S[m: m + N])
        counter += 1
        if hS == hW:
            if S[m: m + N] == W:
                found.append(m)
            else:
                collisions += 1
        if m + N < M:
            hS = (d * (hS - ord(S[m]) * h) + ord(S[m + N])) % q
    return len(found), counter, collisions


def KPM_search(S, W):
    i = 0
    j = 0
    T = KPM_table(W)
    counter = 0
    found = []
    n = len(W)
    m = len(S)
    while j < m:
        counter += 1
        if W[i] == S[j]:
            j += 1
            i += 1
            if i == n:
                found.append(j-i)
                i = 0
        else:
            i = T[i]
            if i < 0:
                j += 1
                i += 1
    return len(found), counter, T


def KPM_table(W):
    m = len(W)
    T = [0 for _ in range(m)]
    pos = 1
    cnd = 0
    T[0] = -1

    while pos < m:
        if W[pos] == W[cnd]:
            T[pos] = T[cnd]
        else:
            T[pos] = cnd
            cnd = T[cnd]
            while cnd >= 0 and W[pos] != W[cnd]:
                cnd = T[cnd]
        pos += 1
        cnd += 1
    return T


print(naiwna(S, "time.")[0], ";", naiwna(S, "time.")[1])
# t_start = time.perf_counter()
# result = naiwna(S, "time.")
# t_stop = time.perf_counter()
# print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
print(Rabin_Karp(S, "time.")[0], ';', Rabin_Karp(S, "time.")[1], ';', Rabin_Karp(S, "time.")[2])
# t_start = time.perf_counter()
# result = Rabin_Karp(S, "time.")
# t_stop = time.perf_counter()
# print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
print(KPM_search(S, "time.")[0], ';', KPM_search(S, "time.")[1],';', KPM_search(S, "time.")[2])
# t_start = time.perf_counter()
# result = KPM_search(S, "time.")
# t_stop = time.perf_counter()
# print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))