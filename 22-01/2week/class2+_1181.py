# 1181. 단어 정렬
# Level Silver5
# Link : https://www.acmicpc.net/problem/1085

N = int(input())
words = list()
for n in range(N):
    words.append(input())

words = list(set(words))
words.sort()
N = len(words)

max_len = 0
for word in words:
    if len(word) > max_len:
        max_len = len(word)

for word_len in range(1, max_len + 1):
    changed_words_idx = list()
    for i in range(N):
        if len(words[i]) == word_len:
            words.append(words[i])
            changed_words_idx.append(i)
    changed_words_idx.sort(reverse=True)
    for pop_idx in changed_words_idx:
        words.pop(pop_idx)

for word in words:
    print(word)