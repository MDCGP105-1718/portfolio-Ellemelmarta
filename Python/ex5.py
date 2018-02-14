n = 99
#for n in range(99,1,-1):
#working code for the range command as long as the while command is commented out
while n>1:
    print(f"{n} bottles of beer on the wall, {n} bottles of beer.")
    n-=1
    #this n-=1 takes 1 from n allowing me to use n still for the next line which means it is 1 lower than the line above
    print(f"Take one down, pass it around, {n} bottles of beer on the wall")
else:
    print(f"{n} bottle of beer on the wall, {n} more bottle of beer!")
    print("so take it down, pass it around, no more bottles of beer on the wall.")
    #this is the code for when n reaches >1 ive used the variable so its easily changeable
