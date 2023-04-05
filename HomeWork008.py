import shelve as s
from Librare import *

add_contact(contacts)

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