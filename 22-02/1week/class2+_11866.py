# 11866. 요세푸스 문제 0
# Level Silver4
# Link : https://www.acmicpc.net/problem/11866

N, K = map(int, input().split())

lst = [0] * N

turn = N
person = 0
result = []
while turn:
    turn -= 1
    move = K
    while move:
        person += 1
        if person > N:
            person = 1
        while lst[person - 1]:
            person += 1
            if person > N:
                person = 1
        move -= 1
    lst[person - 1] = 1
    result.append(person)
print('<', end='')
print(*result, sep=', ', end='')
print('>')
