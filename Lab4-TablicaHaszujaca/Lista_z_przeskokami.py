# Michał Cynarski
# skończone

from random import random


class Element:
    def __init__(self, key, value, level):
        self.key = key
        self.value = value
        self.level = level
        self.next = [None] * (level + 1)


class SkipList:
    def __init__(self, maxLevel=5):
        self.maxLevel = maxLevel
        self.head = Element(None, None, self.maxLevel)

    def randomLevel(self, p=0.5):
        lvl = 0
        while random() < p and lvl < self.maxLevel:
            lvl = lvl + 1
        return lvl

    def search(self, key):
        node = self.head.next[0]
        while node is not None:
            if node.key == key:
                return node.value
            node = node.next[0]

    def insert(self, key, value):
        pre = [None] * (self.maxLevel + 1)
        node = self.head
        my_lvl = self.maxLevel - 1
        for i in range(my_lvl, -1, -1):
            while node.next[i] is not None and node.next[i].key < key:
                node = node.next[i]
            pre[i] = node

        node = node.next[0]
        if node is None or node.key != key:
            random_lvl = self.randomLevel()

            if random_lvl > my_lvl:
                for i in range(my_lvl, random_lvl + 1):
                    pre[i] = self.head
                my_lvl = random_lvl
            elem = Element(key, value, random_lvl)

            for k in range(random_lvl + 1):
                elem.next[k] = pre[k].next[k]
                pre[k].next[k] = elem
        elif node.key == key:
            node.value = value

        for i in range(len(pre)):
            if pre[i] is None:
                pre[i] = self.head
        return pre

    def remove(self, key):
        pre = [None] * (self.maxLevel + 1)
        node = self.head
        my_lvl = self.maxLevel - 1
        for i in range(my_lvl, -1, -1):
            while node.next[i] and node.next[i].key < key:
                node = node.next[i]
            pre[i] = node

        node = node.next[0]
        if node is not None and node.key == key:
            for y in range(my_lvl + 1):
                if pre[y].next[y] != node:
                    break
                pre[y].next[y] = node.next[y]

            if self.head.next[my_lvl] is None and my_lvl > 0:
                my_lvl -= 1

    def displayList_(self):
        node = self.head.next[0]  # pierwszy element na poziomie 0
        keys = []  # lista kluczy na tym poziomie
        while (node != None):
            keys.append(node.key)
            node = node.next[0]

        for lvl in range(self.maxLevel - 1, -1, -1):
            print("{}: ".format(lvl), end=" ")
            node = self.head.next[lvl]
            idx = 0
            while (node != None):
                while node.key > keys[idx]:
                    print("  ", end=" ")
                    idx += 1
                idx += 1
                print("{:2d}".format(node.key), end=" ")
                node = node.next[lvl]
            print("")

    def __str__(self):
        result = []
        node = self.head.next[0]
        while node:
            result.append((node.key, node.value))
            node = node.next[0]
        return str(result)


if __name__ == '__main__':
    sk = SkipList()
    for i in range(1, 16):
        sk.insert(i, chr(i + 64))
    print(sk)
    print(sk.search(2))
    sk.insert(2, 'Z')
    print(sk.search(2))
    sk.remove(5)
    sk.remove(6)
    sk.remove(7)
    sk.displayList_()
    sk.insert(6, 'W')
    sk.displayList_()

    sk2 = SkipList()
    for i in range(15, 0, -1):
        sk2.insert(i, chr(i + 64))
    print(sk2)
    print(sk2.search(2))
    sk2.insert(2, 'Z')
    print(sk2.search(2))
    sk2.remove(5)
    sk2.remove(6)
    sk2.remove(7)
    sk2.displayList_()
    sk2.insert(6, 'W')
    sk2.displayList_()