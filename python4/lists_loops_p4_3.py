#!/usr/bin/env python3

# --- ITEM 3. List
my_list = ['a', 'bb', 'ccc']

list_copy = my_list

print(list_copy)

my_list.append('dddd')

print(my_list)
print(list_copy)

my_list2 = ['a', 'bb', 'ccc']
list_copy2=my_list2.copy()

print(my_list2)
print(list_copy2)

my_list2.append('dddd')

print(my_list2)
print(list_copy2)
