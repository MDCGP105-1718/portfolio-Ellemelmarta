#Specifies the variable cars as 100.
cars = 100
#Specifies the variable space_in_a_car as 4.0.
#Changing 4.0 to 4 removes the .0 from the amount of people you can transport per car and how many people per car need to go so its less specific and could round down or up giving us an incorrect statement.
space_in_a_car = 4.0
#Specifies the variable drivers to be 30.
drivers = 30
#Specifies the variable passengers to be 90.
passengers = 90
#Specifies the variable cars_not_driven to be equal to cars variable minus the drivers variable.
cars_not_driven = cars - drivers
#Specifies the variable cars_driven to be equal to the drivers variable.
cars_driven = drivers
#Specifies the variable carpool_capacity to be equal to cars_driven variable multiplies by space_in_a_car variable.
carpool_capacity = cars_driven * space_in_a_car
#Specifies the variable average_passengers_per_car to be equal to passengers variable divided by the variable cars_driven.
average_passengers_per_car = passengers / cars_driven

#Printing the variables into a text line so they can be understood.
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
