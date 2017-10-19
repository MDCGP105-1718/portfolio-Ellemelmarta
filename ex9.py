annual_salary = float(input ("Please enter your annual salary: "))
#Use bisection search in presentation on learn
monthly_salary = annual_salary/12
current_savings = 0.0
semi_annual_raise = 0.07
annual_r = 0.04
monthlyr = current_savings*annual_r/12
house_cost = 1000000
down_payment = 0.25 * house_cost
epsilon = 100
num_guesses = 0
low = 0
high = 10000
guess = (high + low)/2.0
monthlyr = current_savings*annual_r/12
#36 months to get the million pounds so find the most efficent saving to get there in this time
#leeway of 100 pounds either way
#limit savings to 2 dp
#current_savings += ((monthly_salary * portion_saved) + monthlyr)
#monthlyr += current_savings*r/12




#keep trying different solutions and he will slow me a soloution next week
#add range loop to the one below going through the 36 months until it understands
#a while loop within a while loop of some sort?


while (house_cost - guess) >= epsilon and num_guesses != 36:
    current_savings += ((monthly_salary * guess) + monthlyr)

    if guess < 1000000:
        low = guess
    elif current_savings > 1000000:
        high = guess
        guess = (high + low)/2.0
        num_guesses += 1
print(num_guesses)
print("test")
