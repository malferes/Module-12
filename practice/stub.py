'''
Stubs:
A stub is a function that returns a simple value that is sufficient for testing another function. 
'''

#Instructions:
# Complete the stub function, converting letters grades A+ to B-
# Otherwise retrun 60

#Example of stub functions, the syntax runs with the stub function as is.

# Function convert_to_score
# @param letter
# @return numeric score
# if A+ >= 97, A >= 93, A- >= 90, B+ >= 87, B >= 83 B- = 80...
# example: if A+ score = 97
def convert_to_score(letter):
    if letter == "A+":
        return 97
    elif letter == "A":
        return 93
    elif letter == "A-":
        return 90
    elif letter == "B+":
        return 87
    elif letter == "B":
        return 83
    elif letter == "B-":
        return 80
    return 60

# Function average_score
# @param grades_list
# Iterate the grades_list and call convert_to_score 
# using parameter grade. Return a numberic score.
# Calculate the average
# return average
def average_score(grades_list):
    sum = 0
    count = 0
    for grade in grades_list:
        sum += convert_to_score(grade)
        count += 1
    return sum/count

grades = ["B", "B+", "C", "A", "B-", "B", "A+", "A-", "C+", "C", "B"]
#Call average_score with argument @var grades
print("Average Score: ", round(average_score(grades),2))



