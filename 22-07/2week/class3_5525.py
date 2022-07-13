# 5525. IOIOI
# Level Silver1
# Link : https://www.acmicpc.net/problem/5525

N = int(input())
M = int(input())
S = input()

P = 'I'
P += 'OI' * N
answer = 0
length = len(P)
for i in range(M - length):
    if S[i:i+length] == P:
        answer += 1

print(answer)
