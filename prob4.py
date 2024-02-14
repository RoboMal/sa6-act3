'''
Name: Malcolm King
Class: COMP-3081-001

Goal: Write a Python program that uses lambda & filter() to find the intersection of two lists
'''

sweet = ["apples", "oranges", "grapes", "watermelon", "bananas"]
sour = ["lemons", "limes", "grapefruit", "apples", "oranges", "grapes"]

sweet_n_sour = list(filter(lambda x: x in sweet, sour))

print(f"List 1: {sweet}\n")
print(f"List 2: {sour}\n")

print(f"Intersection: {sweet_n_sour}")

'''
Breakdown:
sweet_n_sour is being declared as a LIST, whose elements consists ONLY
of elements found in BOTH sweet and sour (hence the filter). 
'''