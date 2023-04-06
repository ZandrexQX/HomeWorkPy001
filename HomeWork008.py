import shelve as s
from Librare import *
print("Телефонный справочник")
num = input("Введите код справочника: ")
print("---------------------")
contacts = load_phone(num)

main_phone(contacts, num)