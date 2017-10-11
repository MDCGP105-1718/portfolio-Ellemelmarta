portion_deposit = 0.2
current_savings = 0
#At the end of each month, your savings will be increased by the return of your investment,
#plus a percentage of your monthly_salary
r = 0.04
monthlyr = current_savings*r/12

annual_salary = float(input ("Please enter your annual salary: "))

monthly_salary = annual_salary/12

portion_saved = float(input ("Please enter the percentage of your salary you wish to save, as a decimal: "))

total_cost = float(input ("What is the cost of your desired home: "))

totalmonths = 0

#monthly_salary * portion_saved + monthlyr + current_savings


while current_savings < total_cost:
    current_savings += (monthly_salary * portion_saved + monthlyr)
    totalmonths += 1
    print(f"{current_savings}")
else:
    print(f"{totalmonths}")
#this is gunna be used for working out actual monthly income
