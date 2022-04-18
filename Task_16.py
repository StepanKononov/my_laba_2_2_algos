# https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/?ref=gcse
# https://www.geeksforgeeks.org/kth-largest-element-in-bst-when-modification-to-bst-is-not-allowed/
import sys

sys.stdin = open("input.txt")
sys.stdout = open("output.txt", 'w')


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


def insert(node, key):
    # If the tree is empty,
    # return a new node
    if node is None:
        return Node(key)

    # Otherwise recur down the tree
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    # return the (unchanged) node pointer
    return node


def deleteNode(root, key):
    # Base Case
    if root is None:
        return root

    # Recursive calls for ancestors of
    # node to be deleted
    if key < root.key:
        root.left = deleteNode(root.left, key)
        return root

    elif (key > root.key):
        root.right = deleteNode(root.right, key)
        return root

    # We reach here when root is the node
    # to be deleted.

    # If root node is a leaf node

    if root.left is None and root.right is None:
        return None

    # If one of the children is empty

    if root.left is None:
        temp = root.right
        root = None
        return temp

    elif root.right is None:
        temp = root.left
        root = None
        return temp

    # If both children exist

    succParent = root

    # Find Successor

    succ = root.right

    while succ.left != None:
        succParent = succ
        succ = succ.left

    # Delete successor.Since successor
    # is always left child of its parent
    # we can safely make successor's right
    # right child as left of its parent.
    # If there is no succ, then assign
    # succ->right to succParent->right
    if succParent != root:
        succParent.left = succ.right
    else:
        succParent.right = succ.right

    # Copy Successor Data to root

    root.key = succ.key

    return root


def kthLargestUtil(root, k, c):
    # Base cases, the second condition
    # is important to avoid unnecessary
    # recursive calls
    if root == None or c[0] >= k:
        return

    # Follow reverse inorder traversal
    # so that the largest element is
    # visited first
    kthLargestUtil(root.right, k, c)

    # Increment count of visited nodes
    c[0] += 1

    # If c becomes k now, then this is
    # the k'th largest
    if c[0] == k:
        print(root.key)
        return

    # Recur for left subtree
    kthLargestUtil(root.left, k, c)


def kthLargest(root, k):
    # Initialize count of nodes
    # visited as 0
    c = [0]

    # Note that c is passed by reference
    kthLargestUtil(root, k, c)


n = int(input())
root = None
for i in range(n):

    command = list(input().split())
    match command[0]:
        case '+1':
            root = insert(root, int(command[1]))
        case '0':
            kthLargest(root, int(command[1]))
        case '-1':
            root = deleteNode(root, int(command[1]))
sys.stdout.close()
