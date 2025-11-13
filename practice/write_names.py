'''
Chapter 7.1 In Python, with is a keyword. It ensures files are closed properly
even if the syntax triggers an error, reducing bugs from forgetting to close them.
'''
def main():
    names_list = ["John Riley", "Conan Lorence", "Tammy Lopez", "Alan Franklin", "Inder Singh"]
    #Call the write_names function and pass @var names_list as the argument.
    #Select Ctrl/F5 to run the file.
    #The result is a new file named 'names.txt' which can be viewed in the Explorer pane.

    #enter syntax here
    write_names(names_list)
##
# Define a function named write_names
# @param names
# Description: Using the 'with' keyword, open a file 'names.txt' in write mode and assign 
# to @var file
# The parameter 'names' is a list.  Iterate 'names' and parse each name as firstName and 
# lastName and write the following to the file object: 
# f"first name is {firstName} and last name is {lastName}!\n"

#enter syntax here
def write_names(names):
    with open('names.txt', 'w') as file:
        for name in names:
            firstName, lastName = name.split()
            file.write(f"first name is {firstName} and last name is {lastName}!\n")



main()





