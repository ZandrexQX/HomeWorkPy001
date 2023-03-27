print('Task 26 \n ---------')

a = int(input("Введите число: "))
b = int(input("Введите степень: "))
r = 1

def row(a, b):
   if (b!=1): return a * row (a,b-1)
   return a

print(f"{a} в степени {b} равно: {row(a, b)}")

# ---------------------------------

print('Task 28 \n ---------')

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
s = a

def sum(a, b):
   if (b!=0): return 1 + sum (a,b-1)
   return a

print(f"Сумма {a} и {b} равна: {sum(a, b)}")

# ---------------------------------