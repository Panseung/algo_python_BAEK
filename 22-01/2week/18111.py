# 18111. 마인크래프트
# Level Silver2
# Link : https://www.acmicpc.net/problem/18111

from sys import stdin

N, M, B = map(int, stdin.readline().split())
tiles = [0] * 257
max_goal = 0
min_goal = 256

for _ in range(N):
    tile_x = list(map(int, stdin.readline().split()))
    for tile in tile_x:
        tiles[tile] += 1
        if tile > max_goal:
            max_goal = tile
        if tile < min_goal:
            min_goal = tile

idx_lst = list()
for i in range(min_goal, max_goal + 1):
    if tiles[i]:
        idx_lst.append(i)

result_sec = 500 * 500 * 256
result_height = 0

for goal in range(min_goal, max_goal + 1):
    filling_block = 0
    mining_block = 0
    for i in idx_lst:
        if i > goal:
            mining_block += tiles[i] * (i - goal)
        else:
            filling_block += tiles[i] * (goal - i)
    if B + mining_block < filling_block:
        continue
    need_time = filling_block + mining_block * 2
    if result_sec == 0:
        result_sec = need_time
    if need_time <= result_sec:
        result_sec = need_time
        result_height = goal

print(result_sec, result_height)
