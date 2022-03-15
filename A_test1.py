def solve(turn, visited, d):
    global result
    if turn == 3:
        if result > d:
            result = d
        return
    turn_num = turn_lst[turn]  # 0, 1, 2
    gate_num = entrance[turn_num][0]
    people = entrance[turn_num][1]

    if visited[gate_num] == 0:  # 방문x
        visited[gate_num] = 1
        people -= 1
        d += 1

    res_d = 1
    l_pos = gate_num
    r_pos = gate_num
    while people > 1:
        res_d += 1
        l_pos -= 1
        r_pos += 1
        if l_pos > 0 and visited[l_pos] == 0:
            visited[l_pos] = 1
            people -= 1
            d += res_d
        if r_pos <= N and visited[r_pos] == 0:
            visited[r_pos] = 1
            people -= 1
            d += res_d

    if people == 0:
        visited2 = visited[::]
        solve(turn + 1, visited2, d)
        return
    else:
        finish = False
        while not finish:
            res_d += 1
            l_pos -= 1
            r_pos += 1
            if l_pos > 0 and visited[l_pos] == 0 and r_pos <= N and visited[r_pos] == 0:  # 둘 다 들어갈 수 있으면
                d += res_d
                visited2 = visited[::]
                visited2[l_pos] = 1
                solve(turn + 1, visited2, d)

                visited2 = visited[::]
                visited2[r_pos] = 1
                solve(turn + 1, visited2, d)
                visited2[r_pos] = 0
                finish = True
                return
            elif l_pos > 0 and visited[l_pos] == 0:
                visited[l_pos] = 1
                d += res_d
                visited2 = visited[::]
                solve(turn + 1, visited2, d)
                finish = True
                return
            elif r_pos <= N and visited[r_pos] == 0:
                visited[r_pos] = 1
                d += res_d
                visited2 = visited[::]
                solve(turn + 1, visited2, d)
                finish = True
                return
        return


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    entrance = list()
    for _ in range(3):
        a, b = map(int, input().split())
        entrance.append([a, b])
    result = 999999999999999999999

    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            for k in range(3):
                if k == j or i == k:
                    continue
                turn_lst = [i, j, k]
                places = [0] * (N + 1)
                places[0] = 1
                solve(0, places, 0)
    print(f'#{tc} {result}')
