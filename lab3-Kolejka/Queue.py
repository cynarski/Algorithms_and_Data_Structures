def realloc(tab, size):
    oldSize = len(tab)
    return [tab[i] if i < oldSize else None for i in range(size)]


class Queue:

    def __init__(self,size=5):
        self.__tab = [None for _ in range(5)]
        self.id_deq = 0
        self.id_enq = 0
        self.size = size

    def is_empty(self):
        return self.id_deq == self.id_enq

    def peek(self):
        return self.__tab[self.id_deq]

    def dequeue(self):
        if self.is_empty():
            return None
        result = self.peek()
        self.id_deq += 1
        if self.id_deq == self.size:
            self.id_deq = 0
        return result

    def enqueue(self, par):

        self.__tab[self.id_enq] = par

        self.id_enq += 1
        if self.id_enq == self.size:
            self.id_enq = 0

        if self.id_deq == self.id_enq:
            self.__tab = realloc(self.__tab, 2 * self.size)

            old = self.size
            self.size = 2 * self.size
            last = self.size
            for i in range(self.id_deq, old):
                i = old - i
                self.__tab[last - 1] = self.__tab[i]
                last -= 1
            self.id_deq = last

    def print_tab(self): # wypisywanie tablicy
        return f"{self.__tab}"

    def __str__(self): # wypisanie kolejki
        result = "["
        if self.id_deq < self.id_enq:
            for i in range(self.id_deq, self.id_enq):
                if self.__tab[i] is not None:
                    result += str(self.__tab[i]) + " "
        elif self.id_deq > self.id_enq:
            for i in range(self.id_deq, self.size):
                if self.__tab[i] is not None:
                    result += str(self.__tab[i]) + " "
            for i in range(self.id_enq):
                if self.__tab[i] is not None:
                    result += str(self.__tab[i]) + " "
        if len(result) > 2:
            result = result[0:-1]
        result += "]"
        return result


if __name__ == '__main__':

    queue = Queue()
    for i in range(1,5):
        queue.enqueue(i)
    print(queue.dequeue())
    print(queue.peek())
    print(queue)
    for i in range(5,9):
        queue.enqueue(i)
    print(queue.print_tab())
    while not queue.is_empty():
        print(queue.dequeue())
    print(queue)