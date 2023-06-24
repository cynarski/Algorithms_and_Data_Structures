# skończone

class Element:

    def __init__(self, prio, data):
        self.__data = data
        self.__prio = prio

    def __str__(self):
        return f"{self.__prio} : {self.__data}"

    def __lt__(self, other):
        return self.__prio < other.__prio

    def __gt__(self, other):
        return self.__prio > other.__prio


class Heap:

    def __init__(self):
        self.tab = []

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

    def enqueue(self, element: Element):
        self.tab.append(element)
        idx = self.size - 1

        while idx > 0 and self.tab[idx] > self.tab[self.parent(idx)]:
            self.tab[idx], self.tab[self.parent(idx)] = self.tab[self.parent(idx)], self.tab[idx]
            idx = self.parent(idx)

    def dequeue(self):
        if self.is_empty():
            return None
        item = self.tab[0]
        self.tab[0] = self.tab[-1]
        self.tab = self.tab[:-1]

        self.deq_help(0)
        return item

    def deq_help(self, arr):
        left = self.left(arr)
        right = self.right(arr)
        largest = arr

        if left <= self.size - 1 and self.tab[left] > self.tab[largest]:
            largest = left
        if right <= self.size - 1 and self.tab[right] > self.tab[largest]:
            largest = right

        if largest != arr:
            self.tab[arr], self.tab[largest] = self.tab[largest], self.tab[arr]
            self.deq_help(largest)

    def print_tab(self):
        print('{', end=' ')
        print(*self.tab[:self.size], sep=', ', end=' ')
        print('}')

    def print_tree(self, idx, lvl):
        if idx < self.size:
            self.print_tree(self.right(idx), lvl + 1)
            print(2 * lvl * '  ', self.tab[idx] if self.tab[idx] else None)
            self.print_tree(self.left(idx), lvl + 1)


if __name__ == '__main__':
    h = Heap()
    lst = [7, 5, 1, 2, 5, 3, 4, 8, 9]
    word = "GRYMOTYLA"
    for i in range(len(lst)):
        h.enqueue(Element(lst[i], word[i]))
    h.print_tree(0, 0)
    h.print_tab()
    x = h.dequeue()
    print(h.peek())
    h.print_tab()
    print(x)
    while True:
        el = h.dequeue()
        if el is None:
            break
        print(el)
    h.print_tab()

