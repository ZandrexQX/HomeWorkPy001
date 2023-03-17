from random import randint as r

# print('Task 16 \n ---------')

# n = int(input("Введите количество элементов N (от двух):"))
# while n < 2: n = int(input("Введите количество элементов N (от двух):"))
# list_num = [r(1,5) for i in range(1,n)]
# num = r(1,5)
# count = 0

# for i in list_num:
#     if num == i: count += 1
    
# print(list_num)
# print(num)
# print(f"-> {count}")

# input()

# # ---------------------------------

print('Task 18 \n ---------')

n = int(input("Введите количество элементов N (от двух):"))
while n < 2: n = int(input("Введите количество элементов N (от двух):"))
list_num = [r(1,50) for i in range(1,n)]
num_temp = num = r(1,50)
num_in_list = list_num[0]
count = 0

while(num_temp != num_in_list):
    num_temp = num
    num_temp += count
    if num_temp in list_num: num_in_list = num_temp
    else:
        num_temp = num
        num_temp -= count
        if num_temp in list_num: num_in_list = num_temp
        else: count += 1
    
print(list_num)
print(num)
print(f"-> {num_in_list}")

input()

# ---------------------------------