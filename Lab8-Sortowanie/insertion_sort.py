# skończone

import random
import time
from copy import deepcopy


class Element:

    def __init__(self, prio, data):
        self.__data = data
        self.__prio = prio

    def __repr__(self):
        return f"{self.__prio} : {self.__data}"

    def __lt__(self, other):
        return self.__prio < other.__prio

    def __gt__(self, other):
        return self.__prio > other.__prio


class Heap:

    def __init__(self, tab=None):
        if tab is None:
            self.tab = []
        else:
            self.tab = tab
            self.build_heap()

    @property
    def size(self):
        return len(self.tab)

    def is_empty(self):
        if len(self.tab) == 0:
            return True
        return False

    def peek(self):
        if self.is_empty():
            return None
        return self.tab[0]

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * (i + 1) - 1

    def right(self, i):
        return 2 * (i + 1)

    def build_heap(self):
        for i in range(self.size // 2, -1, -1):
            self.deq_help(self.size, i)

    def deq_help(self, arr, idx):
        left = self.left(idx)
        right = self.right(idx)
        largest = idx

        if left <= arr - 1 and self.tab[left] > self.tab[largest]:
            largest = left
        if right <= arr - 1 and self.tab[right] > self.tab[largest]:
            largest = right

        if largest != idx:
            self.tab[idx], self.tab[largest] = self.tab[largest], self.tab[idx]
            self.deq_help(arr, largest)

    def heapsort(self):
        for i in range(self.size - 1, -1, -1):
            self.tab[i], self.tab[0] = self.tab[0], self.tab[i]
            self.deq_help(i, 0)

    def print_tab(self):
        print('{', end=' ')
        print(*self.tab[:self.size], sep=', ', end=' ')
        print('}')

    def print_tree(self, idx, lvl):
        if idx < self.size:
            self.print_tree(self.right(idx), lvl + 1)
            print(2 * lvl * '  ', self.tab[idx] if self.tab[idx] else None)
            self.print_tree(self.left(idx), lvl + 1)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def shell_sort(arr):
    n = len(arr)
    h = n // 2
    while h > 0:
        for i in range(h, n):
            temp = arr[i]
            j = i
            while j >= h and arr[j - h] > temp:
                arr[j] = arr[j - h]
                j -= h
            arr[j] = temp
        h //= 2

        if h == 2:
            h = 1
        else:
            h = (h * 2) // 3


if __name__ == '__main__':
    lst = [(5, 'A'), (5, 'B'), (7, 'C'), (2, 'D'), (5, 'E'), (1, 'F'), (7, 'G'), (5, 'H'), (1, 'I'), (2, 'J')]
    insertion_sort(lst)
    print(lst)
    lst = [(5, 'A'), (5, 'B'), (7, 'C'), (2, 'D'), (5, 'E'), (1, 'F'), (7, 'G'), (5, 'H'), (1, 'I'), (2, 'J')]
    shell_sort(lst)
    print(lst)
    # Sortowania są stabilne

    lst2 = [int(random.random() * 100) for _ in range(10000)]
    h2 = Heap(lst2)

    t_start = time.perf_counter()
    h2.build_heap()
    h2.heapsort()
    t_stop = time.perf_counter()
    print("Czas obliczeń Heapsort:", "{:.7f}".format(t_stop - t_start))

    lst2 = [int(random.random() * 100) for _ in range(10000)]
    t_start = time.perf_counter()
    insertion_sort(lst2)
    t_stop = time.perf_counter()
    print("Czas obliczeń Insertionsort:", "{:.7f}".format(t_stop - t_start))

    lst2 = [int(random.random() * 100) for _ in range(10000)]
    t_start = time.perf_counter()
    shell_sort(lst2)
    t_stop = time.perf_counter()
    print("Czas obliczeń Shellsort:", "{:.7f}".format(t_stop - t_start))
