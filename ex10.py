#Defining what FizzBuzz is and its conditions
def FizzBuzz(x):
    if x%5 == 0 and x%3 == 0:
        return "FizzBuzz"
    elif x%3 == 0:
        return "Fizz"
    elif x%5 == 0:
        return "Buzz"
    return(x)

Low = int(input("Enter the lowest value: "))
High = int(input("Enter the highest value: "))

#While in range of users input Low and High, does FizzBuzz
for x in range (Low, High+1):
    print (FizzBuzz(x))
