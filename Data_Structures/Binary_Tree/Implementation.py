
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

    def addRecursive(self, root, value):
        if root == None:
            return Node(value)
        if root.value < value:
            root.right = self.addRecursive(root.right, value)
        elif root.value > value:
            root.left = self.addRecursive(root.left, value)
        return root

    def add(self, value):
        self.root = self.addRecursive(self.root, value)



if __name__ == '__main__':
    bt = BinaryTree(4)
    bt.add(5)
    bt.add(6)
    bt.add(10)
    bt.add(3)

    print(bt.root.left.value)
