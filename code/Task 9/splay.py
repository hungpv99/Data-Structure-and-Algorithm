class Node():
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def rightRotate(x):
    y = x.left
    x.left = y.right
    y.right = x
    return y

def leftRotate(x):
    y = x.right
    x.right = y.left
    y.left = x
    return x

def splay(root, key):
    if root == None or root.key == key:
        return root

    if root.key > key:
        if root.left == None:
            return root
        if root.left.key > key:
            root.left.left = splay(root.left.left, key)
            root = rightRotate(root)
        elif root.left.key < key:
            root.left.right = splay(root.left.right, key)
            if root.left.right != None:
                root.left = leftRotate(root.left)

        if root.left == None:
            return root
        else:
            return rightRotate(root)
    else:
        if root.right == None:
            return root
        
        if root.right.key > key:
            root.right.left = splay(root.right.left, key)

            if root.right.left != None:
                root.right = rightRotate(root.right)

        elif root.right.key < key:
            root.right.right = splay(root.right.right, key)
            root = leftRotate(root)
        
        if root.right == None:
            return root
        else:
            return leftRotate(root)

def search(root, key):
    return splay(root, key)

def insert(root, k):
    if root == None:
        return Node(k)
    
    root = splay(root, k)

    if(root.key == k):
        return root

    newNode = Node(k)

    if root.key > k:
        newNode.right = root
        newNode.left = root.left
        root.left = None
    else:
        newNode.left = root
        newNode.right = root.right
        root.right = None
    
    return newNode

def preOrder(root):
    if root != None:
        print(str(root.key) + "  ")
        preOrder(root.left)
        preOrder(root.right)

if __name__ == '__main__':
    root = Node(100)
    root.left = Node(50)
    root.right = Node(200)
    root.left.left = Node(40)
    root.left.left.left = Node(30)
    root.left.left.left.left = Node(20)

    #root = search(root, 20)
    root = insert(root, 25)
    root = search(root, 200)
    preOrder(root)