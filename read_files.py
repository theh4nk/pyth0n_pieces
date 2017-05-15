# You can open and use files for reading or writing by creating an object of the file class and using its read,
# readline or write methods appropriately to read from or write to the file. The ability to read or write to the
# file depends on the mode you have specified for the file opening. Then finally, when you are finished with the
# file, you call the close method to tell Python that we are done using the file.+

poem = '''\
Tell me something good dude. Hi how are you today Hank?
1234567890-
        indent!
'''

# Open for 'w'riting
f = open('poem.txt', 'w')
# Write text to file
f.write(poem)
# Close the file
f.close()

f = open('poem.txt')
while True:
    line = f.readline()
    # Zero length indicates EOF
    if len(line) == 0:
        break
    # The `line` already has a newline
    # at the end of each line
    # since it is reading from a file.
    print(line, end='')
# close the file
f.close()
