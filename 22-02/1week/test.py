new_num = 1
num = 1
result = 0
lst = list()
while new_num <= 1000:
    bunmo = 1
    for i in range(1, new_num + 1):
        bunmo *= i
    result += 1 / bunmo
    lst.append(bunmo)
    new_num += 1

print(result)


