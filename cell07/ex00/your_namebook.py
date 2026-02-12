#!/usr/bin/env python3

def array_of_names(dict_person):
    new_array = []

    for f_name, l_name in dict_person.items():
        new_array.append(f_name.capitalize() + " " + l_name.capitalize())
    return new_array

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}
print(array_of_names(persons))
