def solve(y, x, d, r):
    global result
    if r == 0:
        if result > d:
            result = d
        return
    else:
        for i in range(1, 5):
            if not m_visit[i]:
                m_visit[i] = 1
                my = monster[i][0]
                mx = monster[i][1]
                nd = d + abs(my - y) + abs(mx - x)
                solve(my, mx, nd, r)
                m_visit[i] = 0
            elif not c_visit[i]:
                c_visit[i] = 1
                cy = customer[i][0]
                cx = customer[i][1]
                nd = d + abs(cy - y) + abs(cx - x)
                solve(cy, cx, nd, r - 1)
                c_visit[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    brd = list()
    cnt = 0
    for _ in range(N):
        line = list(map(int, input().split()))
        brd.append(line)
        if max(line) > cnt:
            cnt = max(line)
    monster = [[] for _ in range(5)]
    customer = [[] for _ in range(5)]
    for y in range(N):
        for x in range(N):
            if brd[y][x] > 0:
                monster[brd[y][x]] = [y, x]
            elif brd[y][x] < 0:
                customer[-brd[y][x]] = [y, x]
    m_visit = [1] * 5
    for i in range(5):
        if monster[i]:
            m_visit[i] = 0
    c_visit = [1] * 5
    for i in range(5):
        if customer[i]:
            c_visit[i] = 0

    result = N ** 3
    solve(0, 0, 0, cnt)
    print(f'#{tc} {result}')
