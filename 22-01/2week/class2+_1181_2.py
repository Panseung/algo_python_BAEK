# 1181. 단어 정렬
# Level Silver5
# Link : https://www.acmicpc.net/problem/1085

N = int(input())
words = list()
for n in range(N):
    words.append(input())

words = list(set(words))
words.sort()
words.sort(key=len)
print(*words, sep='\n')