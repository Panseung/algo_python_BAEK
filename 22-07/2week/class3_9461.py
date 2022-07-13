# 9461. 파도반 수열
# Level Silver3
# Link : https://www.acmicpc.net/problem/9461


lst = [0, 1, 1, 1]
while len(lst) < 101:
    lst.append(lst[-3] + lst[-2])

T = int(input())
for _ in range(T):
    print(lst[int(input())])
