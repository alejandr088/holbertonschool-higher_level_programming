#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = my_list.copy()
    uniq_list = list(set(new_list))
    total = sum(uniq_list)
    return total
