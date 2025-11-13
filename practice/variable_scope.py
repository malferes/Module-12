'''
 The scope of a variable is the part of the program in which it is visible.
 A local variable is one defined within a function or code block.
 
 A global variable is defined outside of a function.
 A global variable is visible to all functions defined after it. 
 However, any function that wishes to update a global variable must 
 include a global declaration, like this:
'''
#Global Variable Example
balance = 10000   # A global variable
  
def withdraw(amount) :
   global balance   # This function intends to update the global balance variable
   if balance >= amount :
      balance = balance - amount 
# If you omit the global declaration, then the balance variable inside the withdraw 
# function is considered a local variable.

#Instructions:
# Define a function names sum()
# @param number_list
# Iterate number_list, convert each number to integer
# add the number to global variable total
# return None

total = 50 #Global variable

#enter syntax here
def sum(number_list):
    global total
    for number in number_list:
        total += int(number)
    return None

numbers = ["10", "20","30"]

# Call the sum() function and pass argument numbers
# Print global variable total
# The result should be 110

#enter syntax here
sum(numbers)
print(f"Total: {total}")