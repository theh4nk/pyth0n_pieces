def say_hello():
    #belongs to the function
    print("Hello World")
    #end of function


#call the function
say_hello()


def say(message, times=1):
    print(message * times)

say('Hello')
say('World', 25)
