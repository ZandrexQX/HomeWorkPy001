from random import randint as r

print('Task 10 \n ---------')
n = int(input("Введите число монет: "))

list_1 = [r(0,1) for i in range(n)]
count_0 = count_1 = result = 0

for i in list_1:
    if i == 0: count_0 += 1
    else: count_1 += 1

if count_0 > count_1: result = count_1
else: result = count_0

print(f"Монеты: {list_1}")
print(f"Надо перевернуть монет: {result}")

input()

# ---------------------------------

print('Task 12 \n ---------')

a = r(0,1000)
b = r(0,1000)

sum = a + b
mult = a*b
c = 0

while c*(sum-c) != mult:
    c += 1

d = sum - c

print(f"Петя загадал: {a} и {b}")
print(f"Катя отгадала: {c} и {d}")

input()

# ---------------------------------

print('Task 14 \n ---------')

n = int(input("Введите число N: "))

count = 0
result = 1

while result <= n:
    print(f"2 в степени {count} равна: {result}")   # Развернутый ответ
    # print(result)                                 # Просто вывод результата
    result *= 2
    count += 1 
    
input()

# ---------------------------------

print('Task Add 1 \n ---------')

list_1 = [r(1,1000) for i in range(r(2,5))]
print(*list_1)
str_1 =""
def action(list_1):
    global str_1
    if len(list_1) == 0: 
        print(str_1)
        return
    max = max_i = a = 0
    for i in range(len(list_1)):
        x = list_1[i]
        while x/10 > 1: x = x/10
        if x > max: 
            max = x
            max_i = i
    print(list_1[max_i])
    str_1 += str(list_1[max_i])
    list_1.remove(list_1[max_i])
    action(list_1)

action(list_1)