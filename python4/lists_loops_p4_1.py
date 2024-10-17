#!/usr/bin/env python3

# --- ITEM 1. List

fav_thing=['Dance', 'Books','Plants','Science','GraphicDesign']
print(fav_thing)

fav_thing[2]='Computers'
print(fav_thing)

fav_thing.append('flowers')
print(fav_thing)

fav_thing.insert(0,'Forest')
print(fav_thing)

fav_thing.pop(-2) #indicates the possition to be removed 
print(fav_thing)

fav_thing.pop(0) #removing the first element #returns the first element and modifies the list 

stringFav=''.join(fav_thing) #this requires the 'thing' to be joined at the begining and the list to join as a parameter
print(stringFav)