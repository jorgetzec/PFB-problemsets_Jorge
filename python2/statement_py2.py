#!/usr/bin/env python3
import sys
number= int(sys.argv[1])

# Test 1. Testing the sense

if number > 0: 
  message= 'then is postive'
  print(f'The nummber is {number}, {message}')
elif number < 0:
  message= 'the number is negative'
  print(f'The number is {number}, {message}')
else: 
  message='then it has no sense'
  print(f'You failed, the number is {number}, {message}')

# Test 2. Comparing with 50

if number <50:
  message='smaller than 50'
  print(f'The number is {number}, then {message}')
elif number > 50:
  message='larger than 50'
  print(f'The number is {number}, then {message}')
else:
 print(f'The number must be iqual to {number}')


# Test 3. About even

if number%2 ==0:
  message='is even'
  print(f'The number is {number}, so {message}')
else:
  message='is odd'
  print(f'The number is {number}, so {message}')

# Test 4. Comparing to 50 and defining even numbers

if number<50 and number%2==0:
  message='it is an even number that is smaller than 50'
  print(message) 

# Test 5. 

if number>50 and number%3==0:
  message='it is larger than 50 and divisible by 3'
  print(message)
else:
 print('The number is not larger than 50 and not divible by 3')
