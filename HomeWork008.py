import shelve as s

keys = ("name",
        "family",
        "family_2",
        "phone")

with s.open("phonebook") as key:
    key[keys[1]] = "Aleksey"
    # states["Paris"] = "France"
    # states["Berlin"] = "Germany"
    # states["Madrid"] = "Spain"
    
with s.open("phonebook") as key:
    print(key[keys[1]])