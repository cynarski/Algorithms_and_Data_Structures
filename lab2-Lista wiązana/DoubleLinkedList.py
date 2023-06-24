# Michał Cynarski
# skończone

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def destroy(self):
        self.head = None

    def add(self, data):

        new = Node(data)
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new

    def append(self, data):

        new = Node(data)
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            new.prev = self.tail
            self.tail.next = new
            self.tail = new

    def remove(self):
        if self.is_empty():
            return
        else:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            else:
                self.head.prev = None

    def remove_end(self):
        if self.is_empty():
            return

        else:
            self.tail = self.tail.prev
            if self.tail is None:
                self.head = None
            else:
                self.tail.next = None

    def is_empty(self):
        return self.head is None

    def length(self):
        current = self.head
        counter = 0
        while current:
            counter += 1
            current = current.next
        return counter

    def get(self):
        first = self.head
        return first.data

    def __str__(self):
        current = self.head
        result = ""

        while current.next:
            result += f"-> {current.data}\n"
            current = current.next
        result += f"-> {current.data}"
        return result


if __name__ == '__main__':
    lst = [('AGH', 'Kraków', 1919),
           ('UJ', 'Kraków', 1364),
           ('PW', 'Warszawa', 1915),
           ('UW', 'Warszawa', 1915),
           ('UP', 'Poznań', 1919),
           ('PG', 'Gdańsk', 1945)]

    uczelnie = DoubleLinkedList()
    uczelnie.append(lst[0])
    uczelnie.append(lst[1])
    uczelnie.append(lst[2])
    uczelnie.add(lst[3])
    uczelnie.add(lst[4])
    uczelnie.add(lst[5])
    print(uczelnie, '\n')
    print(uczelnie.length(), '\n')
    uczelnie.remove()
    print(uczelnie.get(), '\n')
    uczelnie.remove_end()
    print(uczelnie, '\n')
    uczelnie.destroy()
    print(uczelnie.is_empty())
    uczelnie.remove()
    uczelnie.remove_end()
