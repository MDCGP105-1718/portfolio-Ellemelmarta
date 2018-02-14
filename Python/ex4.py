name = 'Ben Carter'
#Changed variable name from my_name to name
my_age = 20 # 20 years young
my_height = 178 # CM
body_weight = 70 # KG
#Changed variable name from my_weight to body_weight
my_eyes = 'Brown'
my_hair = 'Brown'
is_heavy = body_weight > 80
print(f"Let's talk about {name}.")
# Swapped pronoun to 'I'
print(f"I am {my_height} CM tall.")
print(f"I am {body_weight} KG heavy.")
print(f"It is {is_heavy} that I am overweight.")
#It's checking if the variable body_weight is greater than 80 and then stating true or false
print(f"I have {my_eyes} eyes and {my_hair} hair.")
#Added new variable for total
total = my_age + my_height + body_weight
print(f"If I add my age {my_age}, my height {my_height} and my weight {body_weight}. I get {total}")
#f prefix allows us to put the variables in curly braces and then it will replace them with the value we have set for them.

#conversions for kg to pound
#kg to pound : kg/0.45359237 = pound
converted_weight = body_weight/0.45359237
#rounding up my weight the the nearest 1 DP and creating a new variable for it
rounded_weight = round(converted_weight,1)
print(f"This is my weight in pounds: {rounded_weight}")
#printed text for the variable rounded_weight showing my weight in pounds to the nearest 1 DP

#conversions for cm to inches
#cm to inch: __CM x 0.394 = __inch
converted_height = my_height*0.394
#rounding up my height the the nearest 1 DP and creating a new variable for it
rounded_height = round(converted_height,1)
print(f"This is my height in inches: {rounded_height}")
#printed text for the variable rounded_height showing my height in inches to the nearest 1 DP
