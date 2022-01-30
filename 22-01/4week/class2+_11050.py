# 11050. 이항 계수 1
# Level Bronze1
# Link : https://www.acmicpc.net/problem/11050

N, K = map(int, input().split())
L, R = 1, 1
for i in range(K):
    L *= N - i
    R *= K - i
print(L // R)
