# 2869. 달팽이는 올라가고 싶다
# Level Bronze1
# Link : https://www.acmicpc.net/problem/2869

import sys
import math

my_input = sys.stdin.readline

A, B, V = map(int, my_input().split())

day = math.ceil((V - A) / (A - B) + 1)
print(day)