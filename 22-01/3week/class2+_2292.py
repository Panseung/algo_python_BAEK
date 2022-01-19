# 2292. 벌집
# Level Bronze2
# Link : https://www.acmicpc.net/problem/2292

N = int(input())

room_cnt = 1
N -= 1
while N > 0:
    N -= room_cnt * 6
    room_cnt += 1

print(room_cnt)

