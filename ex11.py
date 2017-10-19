from random import randint

x = int(randint (1,100))

#make user guess a number with input
guess = int(input("Guess a number between 1 - 100: "))

num_guesses = 0
#tell them higher or lower
while guess != x:
    if guess > x and guess != x:
        print ("wrong, too high")
        guess = int(input("Guess again: "))
        num_guesses += 1
    if guess < x and guess != x:
        print ("wrong, too low")
        guess = int(input("Guess again: "))
        num_guesses += 1
    elif guess == x:
        print (f"congratulations you got it in {num_guesses} guesses. x = {x}")
#track the number of guesses they do till correct
#this doesnt even work how you want it to sometimes it canceles out early for some reason
#try find a different way to do it
