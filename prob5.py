'''
Name: Malcolm King
Class: COMP-3081-001

Goal: Write a Python program that uses lambda to find x^n, where x is an integer in a list and n is any given integer.
'''

nums_list = [2, 8, 14]

n = 5

exponential = list(map(lambda x: pow(x, n), nums_list))

print(exponential)

'''
Breakdown:
Dig deep into your bag of tricks, and remember the existence of pow(), which is rarely used in classes.

For each iteration of nums_list, pow(x, n) is taking x and adding the exponent n, calculates the result,
and adds it to the list exponential.
'''