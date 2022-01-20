# 2609. 최대공약수와 최소공배수
# Level Silver5
# Link : https://www.acmicpc.net/problem/2609

lst = list(map(int, input().split()))

small = min(lst)
big = max(lst)

found = False
big_num = big
while not found:
    if big_num % small == 0:
        found = True
    else:
        big_num += big

found = False
small_num = small
while not found:
    if big % small_num == 0:
        found = True
    else:
        small_num -= 1
        while small % small_num > 0:
            small_num -= 1

print(small_num)
print(big_num)
