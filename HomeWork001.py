print('Task 2 \n ---------')

num = int(input("Введите число: "))
result = 0

while num > 0:
    result += num%10
    num = int(num/10)

print(int(result))
input()

# ---------------------------------

print('Task 4 \n ---------')

num = int(input("Введите число: "))
print(f"Петя: {int(num/6)}  Катя: {int(num/6*4)}  Сережа: {int(num/6)}")

# ---------------------------------

print('Task 6 \n ---------')