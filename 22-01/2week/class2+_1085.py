# 1085. 직사각형에서 탈출
# Level Bronze3
# Link : https://www.acmicpc.net/problem/1085

x, y, w, h = map(int, input().split())

result = min(abs(x - w), abs(y - h), x, y)
print(result)
