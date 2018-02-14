from random import randint

x = int(randint (1,100))

#make user guess a number with input
guess = int(input("Guess a number between 1 - 100: "))

num_guesses = 1
#tell them higher or lower

while guess != x:
    if guess > x and guess != x:
        print ("wrong, too high")
        guess = int(input("Guess again: "))
        num_guesses += 1
    #if statement to make sure the guess isnt equal to input and is higher than it to then tell the user
    if guess < x and guess != x:
        print ("wrong, too low")
        guess = int(input("Guess again: "))
        num_guesses += 1
        #if statement to make sure the guess isnt equal to input and is lower than it to then tell the user
else:
    print (f"Congratulations you got it in {num_guesses} guesses. Number = {x}")
