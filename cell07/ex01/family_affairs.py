#!/usr/bin/env python3

def find_the_redheads(dict_hair_color):
    red_hair_list = []
    for key, value in dict_hair_color.items():
        if value == "red":
            red_hair_list.append(key)
    return red_hair_list

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
print(find_the_redheads(dupont_family))