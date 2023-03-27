print('Task 26 \n ---------')

a = int(input("Введите число: "))
b = int(input("Введите степень: "))
r = 1

def func(a, b):
    global r
    if (b>0):
        r *= a
        func(a,b-1)
        
func(a,b)

print(r)

# ---------------------------------