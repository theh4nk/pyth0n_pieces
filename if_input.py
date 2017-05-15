number = 23
guess = int(input('Enter an integer : '))

if guess == number:
    print("Yay")

elif guess < number:
    print("Nope, keep trying")

else:
    print('No, it is a little lower than that')

print('Done')


