import shelve as s

keys = ("name",
        "family",
        "phone")

contacts = list()

def add_contact(l):
    name = input("Введите имя: ")
    family = input("Введите фамилию: ")
    phone = input("Введите телефон: ")
    
    contact = {keys[0]:name, keys[1]: family, keys[2]: phone}
    l.append(contact)
    
def multi_add(l):
    add_contact(l)
    m = input("Введите add, если хотите добавить контакт: ").lower()
    if m == "add":
        multi_add(l)
    
def save_phone(num):
    with s.open("phonebook") as data: data[num] = contacts
    print("Контакты сохранены")

def load_phone(num):
    with s.open("phonebook") as data: return data[num]
    
def print_keys(r, i):
    print(f"Контакт № {i+1}")
    print("Name: " + r[i][keys[0]])
    print("Family: " + r[i][keys[1]])
    print("Phone: " + r[i][keys[2]])
    print("----------------------")

def print_phone(r):
    for i in range(len(r)):
        print_keys(r, i)
        
def choice_sort():
    ch = input("Введите параметр сортировки (Имя, фамилия, телефон): ").lower()
    if ch == "имя": return 0
    elif ch == "фамилия": return 1
    elif ch == "телефон": return 2
    else:
        print("Неизвестное значение. (Имя) - по умолчанию")
        return 0 # по умолчанию

def sort_phone(func_ch, r):
    ch = func_ch()
    n = input("Введите значение для сортировки: ")
    print(f"---------------------------\n Результат сортировки \n---------------------------")
    for i in range(len(r)):
        if r[i][keys[ch]] == n:
            print_keys(r, i)

def delete_phone(l):
    n = input("Введите номер контакта: ")
    while not n.isdigit():
        n = input("Неверно! Введите номер контакта: ")
    n = int(n)
    l.pop(n-1)

def change_phone():
    pass

def main_phone(l, num):
    flag = True
    command = input("Введите команду (help для справки): ").lower()
    if command == "help":
        print("Комманды:\nadd \nprint \nsort \nsave \ndelete \nchange \nexit")
    elif command == "add": multi_add(l)
    elif command == "sort": sort_phone(choice_sort, l)
    elif command == "save": 
        save_phone(num)
        r = load_phone(num)
    elif command == "print": print_phone(l)
    elif command == "delete": delete_phone(l)
    elif command == "change": pass
    elif command == "exit": flag = not flag
    if flag: main_phone(l, num)
    