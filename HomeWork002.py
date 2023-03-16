from random import randint as r

# print('Task 10 \n ---------')
# n = int(input("Введите число монет: "))

# list_1 = [r(0,1) for i in range(n)]
# count_0 = count_1 = result = 0

# for i in list_1:
#     if i == 0: count_0 += 1
#     else: count_1 += 1

# if (len(list_1) - count_1) > (len(list_1) - count_0):
#     result = len(list_1) - count_0
# else: result = len(list_1) - count_1

# print(f"Монеты: {list_1}")
# print(f"Надо перевернуть монет: {result}")

# input()

# # ---------------------------------

# print('Task 12 \n ---------')

# a = r(0,1000)
# b = r(0,1000)

# sum = a + b
# mult = a*b
# c = 0

# while c*(sum-c) != mult:
#     c += 1

# d = sum - c

# print(f"Петя загадал: {a} и {b}")
# print(f"Катя отгадала: {c} и {d}")

# input()

# # ---------------------------------

print('Task 14 \n ---------')

n = int(input("Введите число N: "))

count = 0
result = 1

while (result < n) and result != n:
     result *= 2
     count += 1
     if result <= n: 
        print(f"2 в степени {count} равна: {result}")   # Развернутый ответ
        # print(result)                                 # Просто вывод результата

input()

# ---------------------------------