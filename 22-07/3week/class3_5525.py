# 5525. IOIOI
# Level Silver1
# Link : https://www.acmicpc.net/problem/5525

N = int(input())
M = int(input())
S = input()

P = 'I'
P += 'OI' * N
length = len(P)
answer = 0
idx = 0
cnt = 0
while idx < M - 2:
    if S[idx] == 'I' and S[idx + 1] == 'O' and S[idx + 2] == 'I':
        cnt += 1
        if cnt == N:
            cnt -= 1
            answer += 1
        idx += 2
    else:
        cnt = 0
        idx += 1
print(answer)