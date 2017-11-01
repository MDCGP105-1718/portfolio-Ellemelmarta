def remove_dups(L1, L2):
    for e in L3:
        if e in L2:
            L1.remove(e)
L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
L3 = L1[:]
remove_dups(L1, L2)
#This code removes the numbers from L3 that are within L2 from L1 but it only works this way because I had to make
#L3 into a copy of L3 by the code L3 = L1[:] if i was to do it for e in l1 if e in l2 then it would only do it for
#first number within l2 thats in l1
print (L1)
print (L2)
