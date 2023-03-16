from random import randint as r

print('Task 10 \n ---------')
n = int(input("Введите число монет: "))

list_1 = [r(0,1) for i in range(n)]
count_0 = count_1 = result = 0

for i in list_1:
    if i == 0: count_0 += 1
    else: count_1 += 1

if (len(list_1) - count_1) > (len(list_1) - count_0):
    result = len(list_1) - count_0
else: result = len(list_1) - count_1

print(f"Монеты: {list_1}")
print(f"Надо перевернуть монет: {result}")

input()

# ---------------------------------

print('Task 12 \n ---------')
n = int(input("Введите число монет: "))

list_1 = [r(0,1) for i in range(n)]
count_0 = count_1 = result = 0

for i in list_1:
    if i == 0: count_0 += 1
    else: count_1 += 1

if (len(list_1) - count_1) > (len(list_1) - count_0):
    result = len(list_1) - count_0
else: result = len(list_1) - count_1

print(f"Монеты: {list_1}")
print(f"Надо перевернуть монет: {result}")

input()

# ---------------------------------