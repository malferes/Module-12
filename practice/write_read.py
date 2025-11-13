'''
 w+ (Write and Read)

Opens the file for reading and writing.
Creates the file if it doesn’t exist.

The seek() method in Python is used with file objects to move the file pointer (cursor)
to a specific position within the file. 
This allows you to control where the next read or write operation will occur.
'''
def main():
    string = "programming\ndatabase\njson\nFlask\nlocalhost\nPython Script\nbreakpoint"

    #Call the write_read_file function and pass argument @var string
    
    #enter syntax here
    write_read_file(string)
 
##
# Define function named write_read_file
# @param string
# Using the with keyword open file named "words.txt" in write and read mode,
# assign to @var file. 
# Write the 'string' parameter to the file object.
# position the file pointer to the first line by entering the following:
# file.seek(0)
# Iterate the file object and print each line using the strip() method.

#enter syntax here
def write_read_file(string):
    with open('words.txt', 'w+') as file:
        file.write(string)
        file.seek(0)
        for line in file:
            print(line.strip())


main()