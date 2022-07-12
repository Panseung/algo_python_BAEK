# 11726. 2xn 타일링
# Level Silver3
# Link : https://www.acmicpc.net/problem/11726


import sys

n = int(sys.stdin.readline().rstrip())
d = [0] * 1001
d[1] = 1
d[2] = 2
d[3] = 3
d[4] = 5

i = 4
while i < n:
    i += 1
    d[i] = d[i - 1] + d[i - 2]

print(d[n] % 10007)
