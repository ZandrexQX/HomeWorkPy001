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
