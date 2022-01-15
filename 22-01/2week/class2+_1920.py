# 1920. 수 찾기
# Level Silver4
# Link : https://www.acmicpc.net/problem/1920

N = int(input())
N_list = list(map(int, input().split()))
N_list.sort()
M = int(input())
M_list = list(map(int, input().split()))

result = list()
for m in M_list:
    start = 0
    end = len(N_list) - 1
    found = False
    while start <= end:
        mid = (start + end) // 2
        if m > N_list[mid]:
            start = mid + 1
        elif m == N_list[mid]:
            print(1)
            found = True
            break
        else:
            end = mid - 1
    if not found:
        print(0)

