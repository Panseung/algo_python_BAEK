# 10250. ACM호텔
# Level Bronze3
# Link : https://www.acmicpc.net/problem/10250

TC = int(input())
for tc in range(TC):
    H, W, N = map(int, input().split())
    h, w = 0, 1
    for i in range(N):
        h += 1
        if h > H:
            h = 1
            w += 1
    if w < 10:
        print(str(h) + '0' + str(w))
    else:
        print(str(h) + str(w))