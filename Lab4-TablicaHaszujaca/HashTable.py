# skończone

class Element:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self, size, c1=1, c2=0):
        self._tab = [None for _ in range(size)]
        self.size = size
        self.c1 = c1
        self.c2 = c2

    def hash_function(self, key):
        result = 0
        if isinstance(key, int):
            result = key
        if isinstance(key, str):
            tab = [ord(i) for i in key]
            result = sum(tab)
        return result % self.size

    def collision(self, arr, i):
        idx = self.hash_function(arr)
        return (idx + self.c1 * i + self.c2 * (i ** 2)) % self.size

    def search(self, key):
        idx = self.hash_function(key)
        i = 0
        while True:
            if i >= self.size:
                break
            if self._tab[idx] is not None and self._tab[idx].key == key:
                return self._tab[idx].value
            else:
                i += 1
                idx = self.collision(key, i)
        return None

    def insert(self, elem):

        key = elem.key
        idx = self.hash_function(key)
        i = 0
        while True:
            if i >= self.size:
                idx = self.hash_function(i) % self.size
            if i >= self.size and None not in self._tab:
                print('Brak miejsca')
                return None
            if self._tab[idx] is None or self._tab[idx].key == key:
                self._tab[idx] = elem
                break
            else:
                i += 1
                idx = self.collision(key, i)

    def remove(self, key):
        idx = self.hash_function(key)
        if self._tab[idx] is None:
            print("Brak danej")
            return None
        self._tab[idx] = None

    def __str__(self):
        result = []
        for i, arr in enumerate(self._tab):
            if arr is None:
                result.append("None")
            else:
                result.append(f"{arr.key}:{arr.value}")
        return "{" + ", ".join(result) + "}"


if __name__ == '__main__':
    def hashtable_test1(size, c1=1, c2=0):
        h = HashTable(size, c1, c2)
        keys = [i for i in range(1, 16)]
        for i in range(len(keys)):
            if keys[i] == 6:
                keys[i] = 18
            if keys[i] == 7:
                keys[i] = 31
        values = [chr(i) for i in range(65, 81)]
        for i in range(len(keys)):
            elem = Element(keys[i], values[i])
            h.insert(elem)
        print(h)
        print(h.search(5))
        print(h.search(14))
        h.insert(Element(5, 'Z'))
        print(h.search(5))
        h.remove(5)
        print(h)
        print(h.search(31))
        h.insert(Element('test', 'W'))
        print(h)


    def hashtable_test2(size, c1=1, c2=0):
        h = HashTable(size, c1, c2)
        keys = [13 * n for n in range(1, 16)]
        values = [chr(i) for i in range(65, 81)]
        for i in range(len(keys)):
            elem = Element(keys[i], values[i])
            h.insert(elem)
        print(h)


    hashtable_test1(13, 1, 0)
    print()
    hashtable_test2(13, 1, 0)
    print()
    hashtable_test2(13, 0, 1)
    print()
    hashtable_test1(13, 0, 1)
