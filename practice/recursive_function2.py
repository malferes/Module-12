'''
Recursive Function
'''
##
# Define function named factorial 
# @param n
# The base case is n <= 1: return 1
# else @var result = n * factorial(n - 1) This is the recursive call
# return result

#enter syntax here
def factorial(n):
    if n <= 1:
        return 1
    else:
        result = n * factorial(n - 1)
        return result
    

n = 5
#Call factorial function and pass n as the argument
print(f"The factorial of {n} is: {factorial(n)}")
#enter syntax here

