print('Task 30 \n ---------')

a = int(input("Введите первый элемент: "))
d = int(input("Введите разность: "))
n = int(input("Введите количество элементов: "))

list_result = [(a + (i-1)*d) for i in range(1, n+1)]

print(*list_result)

# ---------------------------------