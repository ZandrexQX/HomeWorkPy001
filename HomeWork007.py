print('Task 34 \n ---------')

chars=('а','е','и','о','у','ё','ю','я')
list_words = input("Введите фразу: ").split()
    
def count_chars(word):
    count = 0
    for j in word:
        if j in chars:
            count += 1
    return count

if len(set(map(lambda x: count_chars(x), list_words))) == 1:
    print("Парам пам-пам")
else: print("Пам парам")

# ---------------------------------