#creates a text file and saves to desktop path
#open(filename, mode).


filehandler = open("/Users/hank/Desktop/testing123bomber.txt", "a")
filehandler.write("Let's append some text to the file")
filehandler.close()


