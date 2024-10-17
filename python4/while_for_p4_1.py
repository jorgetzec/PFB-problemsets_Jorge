#!/usr/bin/env python3

# --- ITEM 4. While

count=0
while count<101:
  print('count:', count)
  count+=1
print('Done')

# --- ITEM 5. While
factorial=1
count=5

for i in range(1, count+1):
  factorial *= i

print(factorial) 


count=0
factorial_2=1

while count < 10:
  count += 1
  factorial_2 *= count
print(factorial_2)

