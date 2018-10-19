

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


def Check(root, max, min):
    if(root == None):
        return True
    if(not(min <= root.value <= max)):
        return False


    left =  Check(root.left,root.value, min)


    right =  Check(root.right, max, root.value)

    return left and right




if __name__ == '__main__':
    bt = BinaryTree(4)
    # bt.add(5)
    # bt.add(6)
    # bt.add(10)
    # bt.add(3)
    bt.root.left = Node(5)

    print(Check(bt.root, 1000000, -1000000))



    #print(bt.root.left.value)
