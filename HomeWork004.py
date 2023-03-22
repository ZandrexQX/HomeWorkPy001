from random import randint as r

print('Task 22 \n ---------')

n = int(input("Введите количество элементов N (от 15):"))
while n < 15: n = int(input("Введите количество элементов N (от 15):"))
m = int(input("Введите количество элементов N (от 15):"))
while m < 15: m = int(input("Введите количество элементов N (от 15):"))
set_num_1 = set(r(1,50) for i in range(1,n))
set_num_2 = set(r(1,50) for i in range(1,m))
print(*set_num_1)
print(*set_num_2)
list_result = list(set_num_1.intersection(set_num_2))
list_result.sort()
print(*list_result)

input()

# --------------------------------------------------------

print('Task 24 \n ---------')

n = int(input("Введите количество элементов N (от 3):"))
while n < 3: n = int(input("Введите количество элементов N (от 3):"))

list_num_1 = [r(1,50) for i in range(1,n)]

max_count = list_num_1[0] + list_num_1[1] + list_num_1[2]
for i in range(len(list_num_1)-1):
    temp = list_num_1[i-1] + list_num_1[i] + list_num_1[i+1]
    if temp > max_count: max_count = temp

print(list_num_1)
print(max_count)