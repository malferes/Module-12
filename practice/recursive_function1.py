'''
A recursive computation solves a problem by using the solution to the same problem 
with simpler inputs.

For a recursion to terminate, there must be special cases for the simplest inputs.

The printTriangle function, listed on section 5.10, calls itself again with smaller 
and smaller side lengths. Eventually the sideLength must reach 0, and the function 
stops calling itself.
'''

##
# Define the printTriangle function as listed in Section 5.10 of your eBook.
# @param sideLength
# The special case is 0, if sideLength == 0 return nothing
# Call the printTriangle(sideLength - 1)
# print "[]" multiplied by sideLength

#enter syntax here
def printTriangle(sideLength):
    if sideLength == 0:
        return
    printTriangle(sideLength - 1)
    print("[]" * sideLength)

sideLength = 4
#Call function printTriangle and pass argument sideLength
printTriangle(sideLength)
#enter syntax here
