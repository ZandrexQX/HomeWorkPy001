import random as r

print('Task 30 \n ---------')

a = int(input("Введите первый элемент: "))
d = int(input("Введите разность: "))
n = int(input("Введите количество элементов: "))

list_result = [(a + (i-1)*d) for i in range(1, n+1)]

print(*list_result)

# ---------------------------------

print('Task 32 \n ---------')

n = int(input("Введите количество элементов: "))
min_1 = int(input("Введите минимум: "))
max_1 = int(input("Введите максимум: "))

list_1 = [r.randint(-20, 20) for i in range(n)]
list_index = []
def func_1(list_0,list_i,i=0):
    try:
        if list_0[i]>=min_1 and list_0[i]<=max_1:
            list_i.append(i)
        func_1(list_0, list_i,i+1)
    except:
        return

func_1(list_1, list_index)

print(*list_1)
print(f" Индексы: {list_index}")

# ---------------------------------