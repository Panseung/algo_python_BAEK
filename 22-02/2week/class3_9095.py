# 9095. 1, 2, 3 더하기
# Level Silver 3
# Link : https://www.acmicpc.net/problem/9095

def solve(sum_res):
    global cnt
    if sum_res >= n:
        if sum_res == n:
            cnt += 1
        return
    else:
        solve(sum_res + 1)
        solve(sum_res + 2)
        solve(sum_res + 3)


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    cnt = 0
    solve(0)
    print(cnt)
