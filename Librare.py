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
    
def save_phone(num):
    with s.open("phonebook") as data:
        data[num] = contacts

def load_phone(num):
    with s.open("phonebook") as data:
        return data[num]

def print_phone(r):
    for i in r:
        print("Name: " + i[keys[0]])
        print("Family: " + i[keys[1]])
        print("Phone: " + i[keys[2]])
        print()