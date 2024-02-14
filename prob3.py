'''
Name: Malcolm King
Class: COMP-3081-001

Goal: Write a Python program that uses lambda to find the maximum (highest) number in a list of integers
'''
from functools import reduce

list = [1, 3, 13, 909, 77, 5]
maximum = list[0] #initialize maximum as 1st element in list

maximum = reduce(lambda x, y: x if x > y else y, list)


print(maximum)

'''
Breakdown:
Reduce is an imported operation that, as the name implies, reduces a list down
to a single element given a condition.

In this case, lambda is being used to iterate through the list and set assigns higher numbers to maximum
Before loop: maximum = 1
Loop 1: maximum = 3
Loop 2: maximum = 13
Loop 3: maximum = 909
Loop 4: maximum = 909
Loop 5: maximum = 909
'''