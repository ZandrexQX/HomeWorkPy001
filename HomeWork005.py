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
print('Task Add 1\n ---------')
def func():
   max1 = max2 = 0
   list_num = list()
   a = int(input("Введите число: "))
   
   while(len(list_num)<2 or (len(list_num)>=2 and a!=0)):
      while(a == 0 and len(list_num)<2):
         a = int(input("Введите число, отличное от нуля: "))
      list_num.append(a)
      a = int(input("Введите число: "))
   
   for i in list_num:
      if i > max1:
         max2 = max1
         max1 = i
      elif (i>max2 and i<max1): max2 = i
         
   return f"{list_num} -> {max2}"

print(func())

# ---------------------------------