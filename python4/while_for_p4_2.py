#!/usr/bin/env python3

# --- ITEM 6. iteraction with for
numbers= [101,2,15,22,95,33,2,27,72,15,52]
for i in numbers:
    print(i)

print('\n')

numbers= [101,2,15,22,95,33,2,27,72,15,52]
for i in numbers:
    if i%2==0:
        print(i)


# --- ITEM 7. Sorting with for
print('\n')

sum_even=0
sum_odd=0
numbers_sorted=sorted(numbers)
print(numbers_sorted)

for number in numbers_sorted:
     if number % 2 == 0:
        sum_even+=number
        # print(sum_even)
     if number % 2 != 0:
         sum_odd+=number
         # print(sum_odd)
print(f'Sum of even: {sum_even} \nSum of odds: {sum_odd}')

# --- ITEM 8. Sorting with for
for number in range(100):
    print(number)

# Modification to star at 1


