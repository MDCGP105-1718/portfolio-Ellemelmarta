annual_salary = float(input ("Please enter your annual salary: "))
portion_saved = float(input ("Please enter the percentage of your salary you wish to save, as a decimal: "))
total_cost = float(input ("What is the cost of your desired home: "))

monthly_salary = annual_salary/12
portion_deposit = 0.2*total_cost
#calculating the deposit required to be put down
current_savings = 0
r = 0.04
totalmonths = 0
monthlyr = current_savings*r/12
#monthly interest calculation
#added finalcost variable to work out what the cost is without the deposit

while current_savings < total_cost:
    current_savings += (monthly_salary * portion_saved + monthlyr)
#calculating the new current savings each month
    monthlyr += current_savings*r/12
#calculating the new monthlyr for next month this makes sure first month monthlyr is 0
    totalmonths += 1
#adding 1 month to the total months value that will be printed
else:
    print(f"The amount of months you need is: {totalmonths}")
    print(f"Your deposit will cost you: £{portion_deposit}")
#When the value of current_savings reaches what finalcost is then it will print this statement showing the count of loops as months


#switch this thing to an if/for loop
