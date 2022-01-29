import sys

my_input = sys.stdin.readline

N = int(input())
lst = list()
for _ in range(N):
    lst.append(my_input())
print(lst)