def inOrderParsing(root):
    if root:
        inOrderParsing(root.left)
        print(root.val, end=", ")
        inOrderParsing(root.right)

def preOrderParsing(t):
    tree = []
    def parsing(root):
        if root:
            tree.append(root.val)
            parsing(root.left)
            parsing(root.right)
    parsing(t)
    return tree

def postOrderParsing(root):
    if root:
        postOrderParsing(root.left)
        preOrderParsing(root.right)
        print(root.val, end=", ")
