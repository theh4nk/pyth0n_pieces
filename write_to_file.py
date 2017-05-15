

#and creates a new file all in one
filehandler = open("/Users/hank/Desktop/test9999_hg.txt", "w")
filehandler.close()

file = open("/Users/hank/Desktop/test999_hg.txt", "a")
file.write("\nHey dude this is a text")
file.close()
