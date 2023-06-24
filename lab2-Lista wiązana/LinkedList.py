#Michał Cynarski
# skończone

class Node:

    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def destroy(self):
        self.head = None

    def add(self,data):

        new = Node(data)
        new.next = self.head
        self.head = new

    def append(self,data):

        new = Node(data)
        if self.head is None:
            self.head = new
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new

    def remove(self):
        if self.is_empty():
            return
        if self.length() >= 1:
            self.head = self.head.next

    def remove_end(self):
        if self.is_empty():
            return
        if self.length() == 1:
            self.head = None
            return

        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None

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

    uczelnie = LinkedList()
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