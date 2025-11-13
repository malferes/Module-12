'''
Chapter 7.1 In Python, with is a keyword. It ensures files are closed properly
even if the syntax triggers an error, reducing bugs from forgetting to close them.
'''
def main():
    #Call the read_names function with no argument and assign to @var names_list.
    #Iterate the names_list and print each line, include the strip() method
    #Select Ctrl/F5 to run the file.
    #The result is a display of each line.

    #enter syntax here
    name_list = read_names()
    for name in name_list:
        print(name.strip())
 
##
# Define a function named read_names
# no parameter
# Description: Using the 'with' keyword, open a file 'names.txt' in read mode and assign 
# to @var file
# Assign file.readlines() to @var listObj 
# return listObj

#enter syntax here
def read_names():
    with open('names.txt', 'r') as file:
        listObj = file.readlines()
    return listObj


main()





