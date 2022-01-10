# 13460. 구슬 탈출 2
# Level Gold-1
# Link : https://www.acmicpc.net/problem/13460
# Time :

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def solve(blue, red, hole, cnt):
    global result

    if red == hole:
        if result > cnt or result == -1:
            result = cnt
        return
    elif blue == hole:
        return
    elif cnt == 10:
        return
    elif result == -1 or result != -1 and cnt < result:
        for d in range(4):
            blue_y, blue_x = blue[0], blue[1]
            red_y, red_x = red[0], red[1]
            if d == 0:  # 상
                blue_move, red_move = 0, 0
                blue_moving, red_moving = True, True
                for i in range(1, N):
                    if blue_moving and [blue_y + i][blue_x] == '#':
                        blue_moving = False
                    elif blue_moving:
                        blue_move += 1
                    if red_moving and [red_y + i][red_x] == '#':
                        red_moving = False
                    elif red_moving:
                        red_move += 1
                blue[0] += blue_y





N, M = map(int, input().split())
BRD = list()
for n in range(N):
    BRD.append(input())

blue_pos = [0, 0]
red_pos = [0, 0]
hole_pos = [0, 0]

for y in range(N):
    for x in range(M):
        pos = BRD[y][x]
        if pos == 'B':
            blue_pos = [y, x]
        elif pos == 'R':
            red_pos = [y, x]
        elif pos == 'O':
            hole_pos = [y, x]

result = -1
solve(blue_pos, red_pos, hole_pos, 0)
print(result)
