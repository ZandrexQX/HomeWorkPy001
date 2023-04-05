keys = ("name",
        "family",
        "phone")

contacts = list()
reading_list = list()

def add_contact(l):
    name = input("Введите имя: ")
    family = input("Введите фамилию: ")
    phone = input("Введите телефон: ")
    
    contact = {keys[0]:name, keys[1]: family, keys[2]: phone}
    l.append(contact)