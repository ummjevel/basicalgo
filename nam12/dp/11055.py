import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))

d = [0 for i in range(n+5)]

for i in range(n):
    d[i] += a[i]
    temp = 0
    for j in range(i):
        if temp < a[j] and a[j] < a[i]:
            d[i] += a[j]
            temp = a[j]


print(max(d))