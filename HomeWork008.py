import shelve as s
from Librare import *
print("Телефонный справочник")
num = input("Введите код справочника: ")

# add_contact(contacts)

print(contacts)

# save_phone(num)

r = load_phone(num)

print_phone(r)