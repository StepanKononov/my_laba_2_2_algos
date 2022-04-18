import sys

sys.stdin = open("input.txt")
sys.stdout = open("output.txt", 'w')

# Helper function that allocates a new
# node with the given data and None
# left and right poers.
class newNode:

    # Construct to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


# Returns true if given tree is BST.
def isBST(root, l=None, r=None):
    # Base condition
    if (root == None):
        return True

    # if left node exist then check it has
    # correct data or not i.e. left node's data
    # should be less than root's data
    if (l != None and root.data <= l.data):
        return False

    # if right node exist then check it has
    # correct data or not i.e. right node's data
    # should be greater than root's data
    if (r != None and root.data >= r.data):
        return False

    # check recursively for every node.
    return isBST(root.left, l, root) and isBST(root.right, root, r)

def main():

    n = int(input())
    if n == 0:
        print("YES")
    else:
        tree_list = [newNode(0) for i in range(n)]
        for i in range(n):
            val, left, right = map(int, input().split())
            left -= 1
            right -= 1
            tree_list[i].data = val
            if left != -1:
                tree_list[i].left = tree_list[left]
            if right != -1:
                tree_list[i].right = tree_list[right]

        if isBST(tree_list[0]):
            print("YES")
        else:
            print("NO")
    sys.stdout.close()

main()