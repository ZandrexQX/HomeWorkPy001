import shelve as s

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

add_contact(contacts)

# contacts.append(contact_1)
# contacts.append(contact_2)

print(contacts)

with s.open("phonebook") as data:
    data["0"] = contacts
        
with s.open("phonebook") as data:
    reading_list = data["0"]
    
print(reading_list)

for i in reading_list:
    print("Name: " + i[keys[0]])
    print("Family: " + i[keys[1]])
    print("Phone: " + i[keys[2]])
    print()