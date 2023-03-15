# print('Task 2 \n ---------')

# num = int(input("Введите число: "))
# result = 0

# while num > 0:
#     result += num%10
#     num = int(num/10)

# print(int(result))
# input()

# # ---------------------------------

# print('Task 4 \n ---------')

# num = int(input("Введите число журавликов: "))
# print(f"Петя: {int(num/6)}  Катя: {int(num/6*4)}  Сережа: {int(num/6)}")

# # ---------------------------------

print('Task 6 \n ---------')

num = int(input("Введите номер билета: "))

lenNum = len(str(num))
middle = float(lenNum/2)
a = 0
b = 0

while lenNum > 0:
    if lenNum >= middle+1: a += int(num%10)
    elif lenNum <= middle: b += int(num%10)
    num /= 10
    lenNum -= 1
    
if a == b: print("Yes")
else: print("No")