'''
5.7 Problem Solving: Stepwise Refinement
Use the process of stepwise refinement to decompose complex tasks into simpler ones.
A function may require simpler functions to carry out its work.
Keypoint: break down problems in smaller subproblems (functions) that are easier to solve and manage.
'''
def main():
    grade_dictionary = {
        "Alice": ["85", "90", "78"],    
        "Bob": ["92", "88", "95"],      
        "Charlie": ["70", "75", "80"],
        "Diana": ["100", "98", "95"],
        "Ethan": ["60", "65", "70"]
    }   
    for student, grades in grade_dictionary.items():
        average = calculate_average(grades)
        grade = get_letter_grade(average)
        print(f"{student}'s average grade is: {grade}")   

# Use stepwise refinement to break down the problem
# Define a function calculate_average()
# @param grade_list

# Define a function get_letter_grade()
# @param average    
# return letter grade based on average
def get_letter_grade(average):
    if average >= 97:
        grade ='A+'
    elif average >= 93:
        grade ='A'
    elif average >= 90:
        grade ='A-'
    elif average >= 87:
        grade ='B+'
    elif average >= 83:
        grade ='B'
    elif average >= 80:
        grade ='B-'
    elif average >= 77:
        grade ='C+'
    elif average >= 73:
        grade ='C'
    elif average >= 70:
        grade ='C-'
    elif average >= 67:
        grade ='D+'
    elif average >= 63:
        grade ='D'
    elif average >= 60:
        grade ='D-'
    else:
        grade ='F'
    return grade

def calculate_average(grade_list):
    total = 0
    grade = ""
    for grade in grade_list:
        total += int(grade)
    average = total / len(grade_list)
    return average 
    

        
if __name__ == "__main__": # main entry point execution
    main()
