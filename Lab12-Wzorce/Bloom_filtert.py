#Michał Cynarski
#skończone


import time
import math


with open("lotr.txt", encoding='utf-8') as f:
    text = f.readlines()

S = ' '.join(text).lower()

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


P = 0.001
n = 20

b = -1 * n * math.log(P)/(math.log(2))**2
k = b/n * math.log(2)


def RabinKarpSet(S, subs, N):

    set_hsubs = set()
    results = {}
    for sub in subs:
        h = hash(sub[:N])
        set_hsubs.add(h)
        results[sub] = 0

    hs = hash(S[:N])

    for m in range(len(S) - N):
        if hs in set_hsubs and S[m - 1 : m+N-1] in subs:
            results[S[m - 1 : m+N-1]] += 1
        hs = hash(S[m:m + N])

    return results


data = ['gandalf', 'looking', 'blocked', 'comment', 'pouring', 'finally', 'hundred', 'hobbits', 'however', 'popular', 'nothing', 'enjoyed', 'stuffed', 'relaxed', 'himself', 'present', 'deliver', 'welcome', 'baggins', 'further']

t_start = time.perf_counter()
for W in data:
    result = Rabin_Karp(S,W)
    print(W, result[0])
t_stop = time.perf_counter()
print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

t_start = time.perf_counter()

results = RabinKarpSet(S, data, len(data[0]))

t_stop = time.perf_counter()


for k, v in results.items():
    print(k, v)

print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))