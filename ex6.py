name = (input ("What's your name? "))
print(f"Nice to meet you {name}.")
#input allowing the user to answer to the question however this allows numbers as well

age = int(input("What's your age? "))
#Allowing the user to give an int input for the question
print(f"So youre {age} years old.")
if age > 20:
    print("You're so old :O full of wisdom")
else:
    print("You're so young o_o")
#This if statement allows for 2 outputs depending on the number the user enters

height = int(input("What's your height in cm? "))
if height > 180:
    print("You're taller than me but size isn't everything.")
else:
    print("You're small compared to me.")
#Same as previous if statement just with a different argument of >180

weight = int(input("What's your weight in kg? "))
bmi = weight/(height/100)/(height/100)
#This calculation is for checking bmi i divided by 100 as it needs the value in meters not cm.
#It also uses the values that the user input.

if ( bmi >= 18.5 and bmi < 25 ):
#Checking if bmi is inbetween these 2 values with an and statement to add more than one check
    print("Your bmi is within the healthy range.")
else:
    print("Your bmi is not within the healthy range.")

ecolour = input("What is your eye colour? ")
if ecolour in ['brown', 'Brown']:
#The in statement helps for me to be able to make sure it recognises both upper and lower case b as the answer
    print("Your eye colour is the same as mine, the best colour!")
elif ecolour in ['Blue', 'blue']:
#the elif statment then allows me to also check for blue as an answer
    print("Blue eyes are always nice, like looking at a tiny ocean.")
else:
    print("The rare species of man.")
#this final statement only takes place if the above 4 answers are not given and will cover every other colour
