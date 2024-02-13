'''
Name: Malcolm King
Class: COMP-3081-001

Goal: Write a Python program that uses a lambda function to compute the sum of the digits of a given number
'''
print("Welcome to the digit calculator!\n")
num = str(input("Please enter a number: "))
nums_break = [i for i in num] #Separates each digit of a number and adds them as list elements
#Ex. '15' becomes ['1', '5']

#print(nums_break)

total = sum(map(lambda x: int(x), nums_break))

print(f"The digits in {num} sum to {total}")

'''
Breakdown:
The lambda function was used to simultaneously convert the
strings back into integers AND sum the integers.
'''