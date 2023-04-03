print('Task 34 \n ---------')

chars=('а','е','и','о','у','ё','ю','я')
list_words = input("Введите фразу: ").split()
    
def count_chars(word):
    count = 0
    for j in word:
        if j.lower() in chars:
            count += 1
    return count

if len(set(map(lambda x: count_chars(x), list_words))) == 1:
    print("Парам пам-пам")
else: print("Пам парам")

# ---------------------------------

print('Task 36 \n ---------')

n = int(input("Введите строки: "))
m = int(input("Введите солбцы: "))

def matrix(n,m):
    l = [[0] * m for _ in range(n)]
    for i in range(n):
        l[i][0] = i+1
        for j in (range(m)):
            l[0][j] = j+1
            if i>0 and j>0:
                for i in range(1,n):
                    l[i][j] = (i+1)*(j+1)
    return l
    

def print_matrix(l):
    for i in l:
        for j in i:
            print(j, end = "\t")
        print()

# print_matrix(matrix(n,m))

def print_operation_table(f, num_rows, num_columns):
    print_matrix(f(num_rows,num_columns))

print_operation_table(lambda x, y: matrix(x,y), num_rows=n, num_columns=m)