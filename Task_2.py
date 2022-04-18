import sys


sys.stdin = open("input.txt")
sys.stdout = open("output.txt", 'w')

n, hight = input().split()
n = int(n)
hight = float(hight)

h = [None for i in range(n)]
h[0] = hight

l, r = 0, hight

while r - l > 0.0000000001:
    h[1] = (l + r) / 2
    Up = True
    for i in range(2, n):
        h[i] = 2 * h[i - 1] - h[i - 2] + 2
        if h[i] < 0:
            Up = False
            break

    if Up:
        r = h[1]
    else:
        l = h[1]

print(h[n - 1])
sys.stdout.close()





