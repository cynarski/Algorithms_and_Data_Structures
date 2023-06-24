# Michał Cynarski
# skończone

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        if self.root is None:
            self.root = Node(key, value)
            return
        else:
            return self.insert_rec(self.root, key, value)

    def insert_rec(self, node, key, value):
        if node is None:
            node = Node(key,value)
        elif key == node.key:
            node.value = value
        elif key < node.key:
            node.left = self.insert_rec(node.left,key,value)
        elif key > node.key:
            node.right = self.insert_rec(node.right,key,value)
        return node

    def search(self,key):
        return self.search_rec(self.root,key)

    def search_rec(self, node: Node, key):
        if node is None:
            return None
        elif node.key == key:
            return node.value
        elif key < node.key:
            return self.search_rec(node.left, key)
        else:
            return self.search_rec(node.right, key)

    def delete(self, key):
        self.root = self.delete_rec(self.root, key)

    def delete_rec(self, node, key):
        if key < node.key:
            node.left = self.delete_rec(node.left,key)
        elif key > node.key:
            node.right = self.delete_rec(node.right, key)
        else:
            if node.left is None:
                tmp = node.right
                return tmp
            elif node.right is None:
                tmp = node.left
                return tmp
            tmp = node.right
            while tmp.left is not None:
                tmp = tmp.left

            node.key = tmp.key
            node.value = tmp.value

            node.right = self.delete_rec(node.right,tmp.key)
        return node

    def height(self):
        return self.height_rec(self.root)

    def height_rec(self,node):
        if node.left is not None and node.right is not None:
            return 1 + max(self.height_rec(node.left), (self.height_rec(node.right)))
        elif node.left is not None:
            return 1 + self.height_rec(node.left)

        elif node.right is not None:
            return 1 + self.height_rec(node.right)
        else:
            return 1

    def print(self):
        return self.print_rec(self.root)

    def print_rec(self,current:Node):
        if current.left:
            self.print_rec(current.left)
        print(f"{current.key} {current.value}", end=',')
        if current.right:
            self.print_rec(current.right)

    def print_tree(self):
        print("==============")
        self.__print_tree(self.root, 0)
        print("==============")

    def __print_tree(self, node, lvl):
        if node != None:
            self.__print_tree(node.right, lvl + 5)

            print()
            print(lvl * " ", node.key, node.value)

            self.__print_tree(node.left, lvl + 5)


if __name__ == '__main__':
    tree = BST()
    dict = {50: 'A', 15: 'B', 62: 'C', 5: 'D', 20: 'E', 58: 'F', 91: 'G', 3: 'H', 8: 'I', 37: 'J', 60: 'K', 24: 'L'}
    for k, v in dict.items():
        tree.insert(k,v)
    tree.print_tree()
    tree.print()
    print()
    print(tree.search(24))
    tree.insert(20,'AA')
    tree.insert(6, 'M')
    tree.delete(62)
    tree.insert(59, 'N')
    tree.insert(100,  'P')
    tree.delete(8)
    tree.delete(15)
    tree.insert(55, 'R')
    tree.delete(50)
    tree.delete(5)
    tree.delete(24)
    print(tree.height())
    tree.print()
    print()
    tree.print_tree()
