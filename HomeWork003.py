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

input()

# ---------------------------------

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

print('Task 20 \n ---------')

n = input("Введите слово:").upper()

letters_1 = {'A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T',
             'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т' }

letters_2 = {'D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У'}
letters_3 = {'B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я'}
letters_4 = {'F', 'H', 'V', 'W', 'Y', 'Й', 'Ы'}
letters_5 = {'K', 'Ж', 'З', 'Х', 'Ц', 'Ч'}
letters_8 = {'J', 'X', 'Ш', 'Э', 'Ю'}
letters_10 = {'Q', 'Z', 'Ф', 'Щ', 'Ъ'}

count = 0
for i in n:
    if i in letters_1: count += 1
    elif i in letters_2: count += 2
    elif i in letters_3: count += 3
    elif i in letters_4: count += 4
    elif i in letters_5: count += 5
    elif i in letters_8: count += 8
    elif i in letters_10: count += 10

print(count)

input()

# ---------------------------------

print('Task Add 1 \n ---------')

string_1 = [i for i in input("Введите первую фразу: ").
            strip().lower() if i.isalpha()]
string_2 = [i for i in input("Введите вторую фразу: ").
            strip().lower() if i.isalpha()]

for i in string_1:
    if i in string_2: string_2.remove(i)
    else: 
        print("NO")
        break
    
if len(string_2) == 0: print("YES")

input()

# ---------------------------------

print('Task Add 2 \n ---------')

keys = [i for i in input("Введите ключи:").split()] # для примера: cd ca ab ad
values = [i for i in input("Введите значения: ").split()] # для примера: 1 2 3 4

dict_str = dict()
if len(keys) == len(values):
    for i in range(len(keys)): dict_str[keys[i]] = values[i]
else: print("Ключи и значения не совпадают!")

str_list = list()

for i in dict_str.keys():
    str_list.append(str(i) + "="+ str(dict_str[i]))

str_list.sort()

print("&".join(str_list))

input()

# ---------------------------------