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

n = int(input("Введите количество: "))

list_0 = [[0] * n for _ in range(n)]

for i in range(n):
   list_0[i][0] = i+1
   list_0[0][i] = i+1
   if i>0:
       for j in range(i,n):
           list_0[i][j] = (i+1)*(j+1)
           if i!=j: list_0[j][i] = (i+1)*(j+1)
    

def print_matrix(list):
    for i in list_0:
        for j in i:
            print(j, end = "\t")
        print()

print_matrix(list_0)


def print_operation_table(f, num_rows, num_columns):
    pass
    


print_operation_table(lambda x, y: x * y, num_rows=6, num_columns=6)