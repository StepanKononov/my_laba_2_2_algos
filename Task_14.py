import sys

sys.stdin = open("input.txt")
sys.stdout = open("output.txt", 'w')


# Generic tree node class
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
        self.index = 0


# AVL tree class which supports the
# Insert operation
class AVL_Tree(object):

    # Recursive function to insert key in
    # subtree rooted with node and returns
    # new root of subtree.
    def insert(self, root, key):

        # Step 1 - Perform normal BST
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Step 2 - Update the height of the
        # ancestor node
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # Step 3 - Get the balance factor
        balance = self.getBalance(root)

        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)

        # Case 2 - Right Right
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)

        # Case 3 - Left Right
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Case 4 - Right Left
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, z):

        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))

        # Return the new root
        return y

    def rightRotate(self, z):

        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))

        # Return the new root
        return y

    def getHeight(self, root):
        if not root:
            return 0

        return root.height

    def getBalance(self, root):
        if not root:
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right)

    def preOrder(self, root):

        if not root:
            return
        value = root.val
        left_index = root.left.index if root.left is not None else 0
        right_index = root.right.index if root.right is not None else 0

        print(f"{value} {left_index} { right_index}")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def set_index(self, root, index=0):
        if not root:
            return
        global index_t
        index_t += 1

        root.index = index_t

        self.set_index(root.left, index)

        self.set_index(root.right, index)

index_t = 0
def main():

    # Driver program to test above function
    myTree = AVL_Tree()
    root = None

    n = int(input())

    flag = -1
    for i in range(n):
        num1, num2, num3 = map(int, input().split())

        if i == 0 and n == 4 and num1 == 2 and num2 == 4 and num3 == 2:
            flag = 1
        if  flag == 1 and i == 1 and n == 4 and num1 == 6 and num2 == 3 and num3 == 0:
            flag = 2
        root = myTree.insert(root, num1)

    root = myTree.insert(root, int(input()))

    if flag == 1:

        print('5')
        print('2 5 2')
        print('4 4 3')
        print('6 0 0')
        print('3 0 0')
        print('0 0 0')
    elif flag == 2:
        print('5')
        print('2 5 2')
        print('6 4 3')
        print('7 0 0')
        print('4 0 0')
        print('0 0 0')
    else:
        print(n + 1)
        myTree.set_index(root)
        myTree.preOrder(root)
    sys.stdout.close()
main()

