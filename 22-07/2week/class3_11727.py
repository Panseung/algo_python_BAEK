# 11727. 2xn 타일링 2
# Level Silver3
# Link : https://www.acmicpc.net/problem/11727


n = int(input())

lst = [0, 1, 3]

idx = 2
while idx < n:
    idx += 1
    lst.append(lst[idx - 2] * 2 + lst[idx - 1])

print(lst[n] % 10007)
