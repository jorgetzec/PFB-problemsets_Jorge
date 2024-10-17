#!/usr/bin/env python3

# --- ITEM 12. for and range use
import sys
min_num = int( sys.argv[1])
max_num = int(sys.argv[2]) + 1

for num in range(min_num, max_num):
    print(num)

print('\n')

for num in range(min_num, max_num):
    if num == min_num:
      print(min_num)
    elif num %2==0:
     print(num)
    elif num == max_num:
       print(max_num)

# --- ITEM 13. List with for

my_list_seq=['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

# Use a for loop to iterate through each element of this list
for seq in my_list_seq:
   print(seq)

print('\n')

# For each element in the list, print its length and sequence separated by a tab. 
for seq in my_list_seq:
   print(f'{len(seq)} \t {seq}')

print('\n')

IndexPos=0
for seq in my_list_seq:
   print(f'{IndexPos} \t {len(seq)} \t {seq}')
   IndexPos += 1
