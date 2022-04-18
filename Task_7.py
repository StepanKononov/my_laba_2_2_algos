import sys


sys.stdin = open("input.txt")
sys.stdout = open("output.txt", 'w')


n = int(input())

tree = []

if n != 0:
    for i in range(n):
        k, l, r = map(int, input().split())
        tree.append([k, l, r])

    is_correct_tree = True


    for i in range(n):
        cur_value = tree[i][0]
        left_index = tree[i][1]
        right_index = tree[i][2]

        if left_index != -1 and tree[left_index][0] >= cur_value:
            is_correct_tree = False
            break
        if right_index != -1 and tree[right_index][0] < cur_value:
            is_correct_tree = False
            break

    if is_correct_tree:
        print("CORRECT")
    else:
        print("INCORRECT")
else:
    print("CORRECT")
sys.stdout.close()