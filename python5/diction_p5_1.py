#!/usr/bin/env python3

# --- Problem 1

fav_dict ={'book': 'Jitterbug Perfume', 'song':"Tom Petty - I Won't Back Down", 'tree': 'Cedar'}

# --- Problem 2

print(fav_dict['book'])

# --- Problem 3
fav_thing = 'book'
print(fav_dict[fav_thing])

# --- Problem 4
print(fav_dict['tree'])

# --- Problem 5
fav_dict['organism'] = 'Chlamydomonas'
fav_thing = 'organism'
print(fav_dict[fav_thing])

print('\n')

# --- Problem 6
# If you want to print the keys
for thing in fav_dict:
    print(thing)

print('\n')

# If you want to print the values
for thing in fav_dict:
    print(fav_dict[thing])

print('\n')

# If you want to print keys and values
for thing in fav_dict:
    print(thing, '\t', fav_dict[thing])

print('\n')

# --- Problem 7

print(fav_thing)
for thing in fav_dict:
    if fav_thing in fav_dict:
        print('Found')
        print(fav_dict[fav_thing])
        break

print('\n')

# --- Problem 8
for thing in fav_dict:
    print(thing)
print(f'What fav thing do yo want to see:')
key_things=input()
if key_things in fav_dict:
    print(fav_dict[key_things]) 
else:
    print('Is not included in the dic for fav things or check spelling')

# --- Problem 9
fav_dict['organism']='Any bacteria'
print(fav_dict['organism'])

# --- Problem 10
print('Indicate a new value for favorite thing (key):')
new_value_favThing=input()
fav_dict[fav_thing]=new_value_favThing
print(f'Now the key for favorite thing is {print(fav_dict[fav_thing])}')