# 1259. 팰린드롬 수
# Level Bronze1
# Link : https://www.acmicpc.net/problem/1259

words = list()
while True:
    word = input()
    if word == '0':
        break
    else:
        words.append(word)

for word in words:
    palindrome = True
    for i in range((len(word) + 1) // 2):
        if word[i] != word[-1 - i]:
            palindrome = False
            break

    if palindrome:
        print('yes')
    else:
        print('no')
