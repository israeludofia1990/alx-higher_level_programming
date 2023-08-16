#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = []
    [unique.append(i) for i in my_list if i not in unique]
    return sum(unique)
