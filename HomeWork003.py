from random import randint as r

print('Task 16 \n ---------')

n = int(input("Введите количество элементов N (от двух):"))
while n < 2: n = int(input("Введите количество элементов N (от двух):"))
list_num = [r(1,5) for i in range(1,n)]
num = r(1,5)
count = 0

for i in list_num:
    if num == i: count += 1
    
print(list_num)
print(num)
print(f"-> {count}")